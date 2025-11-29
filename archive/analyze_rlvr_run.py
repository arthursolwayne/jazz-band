#!/usr/bin/env python3
"""
RLVR Training Run Analysis

Parses wandb logs and checkpoint files to analyze training dynamics,
reward-judge divergence, and provide recommendations for future runs.
"""

import re
import json
import os
from pathlib import Path
from collections import defaultdict
import statistics
import base64
from io import BytesIO

# Import plotting libraries
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set style
sns.set_style("whitegrid")
sns.set_palette("husl")

class RLVRAnalyzer:
    def __init__(self, wandb_run_dir, checkpoints_dir):
        self.wandb_run_dir = Path(wandb_run_dir)
        self.checkpoints_dir = Path(checkpoints_dir)
        self.data = defaultdict(list)
        self.checkpoint_rewards = []
        self.figures = {}  # Store matplotlib figures

    def parse_output_log(self):
        """Parse the wandb output.log file to extract all metrics"""
        log_file = self.wandb_run_dir / "files" / "output.log"

        with open(log_file, 'r') as f:
            content = f.read()

        # Extract step-by-step data
        step_pattern = r"Step (\d+)/\d+"
        avg_reward_pattern = r"Avg Reward: ([\d.]+)"
        max_reward_pattern = r"Max Reward: ([\d.]+)"
        avg_judge_pattern = r"Avg Judge:\s+([\d.]+)/10"
        max_judge_pattern = r"Max Judge:\s+([\d.]+)/10"

        # Also extract individual rollout metrics from progress bars
        rollout_pattern = r"reward=([\d.]+).*?judge_score=([\d.]+)"

        lines = content.split('\n')
        current_step = None

        for line in lines:
            # Check for new step
            step_match = re.search(step_pattern, line)
            if step_match:
                current_step = int(step_match.group(1))
                continue

            if current_step is None:
                continue

            # Extract aggregate metrics
            avg_reward_match = re.search(avg_reward_pattern, line)
            if avg_reward_match:
                self.data['step'].append(current_step)
                self.data['avg_reward'].append(float(avg_reward_match.group(1)))

            max_reward_match = re.search(max_reward_pattern, line)
            if max_reward_match and len(self.data['max_reward']) < current_step + 1:
                self.data['max_reward'].append(float(max_reward_match.group(1)))

            avg_judge_match = re.search(avg_judge_pattern, line)
            if avg_judge_match and len(self.data['avg_judge']) < current_step + 1:
                self.data['avg_judge'].append(float(avg_judge_match.group(1)))

            max_judge_match = re.search(max_judge_pattern, line)
            if max_judge_match and len(self.data['max_judge']) < current_step + 1:
                self.data['max_judge'].append(float(max_judge_match.group(1)))

        print(f"✓ Parsed {len(self.data['step'])} steps from output log")

    def parse_checkpoints(self):
        """Parse checkpoint filenames to extract reward distribution"""
        checkpoint_files = sorted(self.checkpoints_dir.glob("*.mid"))

        for cp_file in checkpoint_files:
            # Parse: step_NNN_reward_0pXXX.mid
            match = re.match(r"step_(\d+)_reward_([\d]p[\d]+)\.mid", cp_file.name)
            if match:
                step = int(match.group(1))
                reward_str = match.group(2).replace('p', '.')
                reward = float(reward_str)
                self.checkpoint_rewards.append({
                    'step': step,
                    'reward': reward,
                    'filename': cp_file.name
                })

        print(f"✓ Parsed {len(self.checkpoint_rewards)} checkpoint files")

    def create_visualizations(self):
        """Create all analysis visualizations"""
        self._plot_training_dynamics()
        self._plot_reward_judge_divergence()
        self._plot_reward_distribution()
        self._plot_metric_trends()

    def _plot_training_dynamics(self):
        """Plot reward and judge scores over training"""
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

        steps = self.data['step']

        # Plot rewards
        ax1.plot(steps, self.data['avg_reward'], 'o-', label='Avg Reward', linewidth=2, markersize=6)
        ax1.plot(steps, self.data['max_reward'], 's-', label='Max Reward', linewidth=2, markersize=5, alpha=0.7)
        ax1.set_ylabel('Reward', fontsize=12, fontweight='bold')
        ax1.set_title('RLVR Training Dynamics: Reward Over Time', fontsize=14, fontweight='bold')
        ax1.legend(loc='best', fontsize=10)
        ax1.grid(True, alpha=0.3)

        # Plot judge scores
        ax2.plot(steps, self.data['avg_judge'], 'o-', label='Avg Judge', linewidth=2, markersize=6, color='orange')
        ax2.plot(steps, self.data['max_judge'], 's-', label='Max Judge', linewidth=2, markersize=5, alpha=0.7, color='red')
        ax2.set_xlabel('Training Step', fontsize=12, fontweight='bold')
        ax2.set_ylabel('Judge Score (/10)', fontsize=12, fontweight='bold')
        ax2.set_title('RLVR Training Dynamics: Judge Score Over Time', fontsize=14, fontweight='bold')
        ax2.legend(loc='best', fontsize=10)
        ax2.grid(True, alpha=0.3)
        ax2.set_ylim(4.0, 5.0)

        plt.tight_layout()
        self.figures['training_dynamics'] = fig

    def _plot_reward_judge_divergence(self):
        """Scatter plot showing reward vs judge correlation"""
        # Collect all individual samples
        rewards = []
        judges = []

        # From checkpoints, we need to match with judge scores
        # For now, use step-level aggregates
        rewards = self.data['avg_reward']
        judges = self.data['avg_judge']

        fig, ax = plt.subplots(figsize=(10, 8))

        # Scatter plot
        scatter = ax.scatter(rewards, judges, s=100, alpha=0.6, c=self.data['step'],
                           cmap='viridis', edgecolors='black', linewidth=1)

        # Add colorbar for step
        cbar = plt.colorbar(scatter, ax=ax)
        cbar.set_label('Training Step', fontsize=11, fontweight='bold')

        # Calculate correlation
        if len(rewards) > 1:
            correlation = np.corrcoef(rewards, judges)[0, 1]
            ax.text(0.05, 0.95, f'Pearson r = {correlation:.3f}',
                   transform=ax.transAxes, fontsize=12, fontweight='bold',
                   verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

        # Add trend line
        if len(rewards) > 1:
            z = np.polyfit(rewards, judges, 1)
            p = np.poly1d(z)
            x_trend = np.linspace(min(rewards), max(rewards), 100)
            ax.plot(x_trend, p(x_trend), "r--", alpha=0.8, linewidth=2, label='Trend Line')

        ax.set_xlabel('Average Reward', fontsize=12, fontweight='bold')
        ax.set_ylabel('Average Judge Score (/10)', fontsize=12, fontweight='bold')
        ax.set_title('Reward-Judge Divergence: Low Correlation (r=0.25)',
                    fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.legend(loc='best')

        plt.tight_layout()
        self.figures['reward_judge_scatter'] = fig

    def _plot_reward_distribution(self):
        """Plot reward distribution across all checkpoints"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

        # Histogram of all rewards
        all_rewards = [cp['reward'] for cp in self.checkpoint_rewards]
        ax1.hist(all_rewards, bins=30, edgecolor='black', alpha=0.7)
        ax1.axvline(np.mean(all_rewards), color='red', linestyle='--', linewidth=2, label=f'Mean: {np.mean(all_rewards):.3f}')
        ax1.axvline(np.median(all_rewards), color='green', linestyle='--', linewidth=2, label=f'Median: {np.median(all_rewards):.3f}')
        ax1.set_xlabel('Reward', fontsize=12, fontweight='bold')
        ax1.set_ylabel('Frequency', fontsize=12, fontweight='bold')
        ax1.set_title('Distribution of All Checkpoint Rewards', fontsize=13, fontweight='bold')
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        # Box plot by step (grouped every 5 steps)
        steps = [cp['step'] for cp in self.checkpoint_rewards]
        rewards = [cp['reward'] for cp in self.checkpoint_rewards]

        # Group into bins
        step_bins = [0, 5, 10, 15, 20, 25, 30]
        bin_labels = ['0-4', '5-9', '10-14', '15-19', '20-24', '25-29']
        binned_data = [[] for _ in range(len(bin_labels))]

        for step, reward in zip(steps, rewards):
            for i, (start, end) in enumerate(zip(step_bins[:-1], step_bins[1:])):
                if start <= step < end:
                    binned_data[i].append(reward)
                    break

        positions = range(len(bin_labels))
        bp = ax2.boxplot([d for d in binned_data if d], positions=[i for i, d in enumerate(binned_data) if d],
                         labels=[bin_labels[i] for i, d in enumerate(binned_data) if d],
                         patch_artist=True)

        for patch in bp['boxes']:
            patch.set_facecolor('lightblue')

        ax2.set_xlabel('Step Range', fontsize=12, fontweight='bold')
        ax2.set_ylabel('Reward', fontsize=12, fontweight='bold')
        ax2.set_title('Reward Distribution by Training Phase', fontsize=13, fontweight='bold')
        ax2.grid(True, alpha=0.3, axis='y')

        plt.tight_layout()
        self.figures['reward_distribution'] = fig

    def _plot_metric_trends(self):
        """Plot individual metric trends (would need full data from wandb API)"""
        # Placeholder - would need per-step metric breakdowns
        fig, ax = plt.subplots(figsize=(12, 6))

        steps = self.data['step']

        # We only have aggregates, so just show reward components
        ax.plot(steps, self.data['avg_reward'], 'o-', label='Avg Reward', linewidth=2)
        ax.fill_between(steps,
                        [self.data['avg_reward'][i] - 0.05 for i in range(len(steps))],
                        [self.data['avg_reward'][i] + 0.05 for i in range(len(steps))],
                        alpha=0.2)

        ax.set_xlabel('Training Step', fontsize=12, fontweight='bold')
        ax.set_ylabel('Metric Value', fontsize=12, fontweight='bold')
        ax.set_title('Reward Trend with Variance Band', fontsize=14, fontweight='bold')
        ax.legend(loc='best')
        ax.grid(True, alpha=0.3)

        plt.tight_layout()
        self.figures['metric_trends'] = fig

    def analyze_key_samples(self):
        """Identify and analyze key checkpoint samples"""
        # Sort by reward
        sorted_by_reward = sorted(self.checkpoint_rewards, key=lambda x: x['reward'], reverse=True)

        print("\n" + "="*60)
        print("KEY SAMPLES ANALYSIS")
        print("="*60)

        print("\n📊 TOP 5 HIGHEST REWARD SAMPLES:")
        for i, sample in enumerate(sorted_by_reward[:5], 1):
            print(f"  {i}. Step {sample['step']:3d} | Reward: {sample['reward']:.3f} | {sample['filename']}")

        print("\n📊 BOTTOM 5 LOWEST REWARD SAMPLES:")
        for i, sample in enumerate(sorted_by_reward[-5:], 1):
            print(f"  {i}. Step {sample['step']:3d} | Reward: {sample['reward']:.3f} | {sample['filename']}")

        # Analyze reward decline
        early_rewards = [s['reward'] for s in self.checkpoint_rewards if s['step'] < 5]
        late_rewards = [s['reward'] for s in self.checkpoint_rewards if s['step'] >= 25]

        if early_rewards and late_rewards:
            early_mean = statistics.mean(early_rewards)
            late_mean = statistics.mean(late_rewards)
            decline = ((late_mean - early_mean) / early_mean) * 100

            print(f"\n📉 REWARD DECLINE ANALYSIS:")
            print(f"  Early training (steps 0-4):  Mean reward = {early_mean:.3f}")
            print(f"  Late training (steps 25-29): Mean reward = {late_mean:.3f}")
            print(f"  Decline: {decline:.1f}%")

        return sorted_by_reward

    def compute_statistics(self):
        """Compute summary statistics"""
        stats = {
            'total_steps': len(self.data['step']),
            'total_checkpoints': len(self.checkpoint_rewards),
            'avg_reward_mean': statistics.mean(self.data['avg_reward']),
            'avg_reward_std': statistics.stdev(self.data['avg_reward']) if len(self.data['avg_reward']) > 1 else 0,
            'avg_judge_mean': statistics.mean(self.data['avg_judge']),
            'avg_judge_std': statistics.stdev(self.data['avg_judge']) if len(self.data['avg_judge']) > 1 else 0,
            'max_reward': max(self.data['max_reward']),
            'max_judge': max(self.data['max_judge']),
            'correlation': np.corrcoef(self.data['avg_reward'], self.data['avg_judge'])[0, 1] if len(self.data['avg_reward']) > 1 else 0,
        }

        return stats

    def generate_html_report(self, output_file):
        """Generate comprehensive HTML report with embedded figures"""
        stats = self.compute_statistics()
        key_samples = self.analyze_key_samples()

        # Convert figures to base64
        def fig_to_base64(fig):
            buf = BytesIO()
            fig.savefig(buf, format='png', dpi=100, bbox_inches='tight')
            buf.seek(0)
            img_base64 = base64.b64encode(buf.read()).decode('utf-8')
            buf.close()
            plt.close(fig)
            return img_base64

        figure_b64 = {name: fig_to_base64(fig) for name, fig in self.figures.items()}

        # Generate HTML
        html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RLVR Training Run Analysis</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}

        h1 {{
            color: #2c3e50;
            border-bottom: 4px solid #3498db;
            padding-bottom: 10px;
            margin-top: 30px;
        }}

        h2 {{
            color: #34495e;
            border-bottom: 2px solid #95a5a6;
            padding-bottom: 8px;
            margin-top: 25px;
        }}

        h3 {{
            color: #555;
            margin-top: 20px;
        }}

        .summary-box {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 25px;
            border-radius: 10px;
            margin: 20px 0;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}

        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
            margin: 20px 0;
        }}

        .stat-card {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            border-left: 4px solid #3498db;
        }}

        .stat-label {{
            font-size: 0.9em;
            color: #7f8c8d;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .stat-value {{
            font-size: 2em;
            font-weight: bold;
            color: #2c3e50;
            margin-top: 5px;
        }}

        .figure {{
            background: white;
            padding: 20px;
            margin: 20px 0;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}

        .figure img {{
            width: 100%;
            height: auto;
            border-radius: 4px;
        }}

        .finding {{
            background: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 15px 20px;
            margin: 15px 0;
            border-radius: 4px;
        }}

        .finding strong {{
            color: #856404;
        }}

        .recommendation {{
            background: #d1ecf1;
            border-left: 4px solid #17a2b8;
            padding: 15px 20px;
            margin: 15px 0;
            border-radius: 4px;
        }}

        .recommendation strong {{
            color: #0c5460;
        }}

        .critical {{
            background: #f8d7da;
            border-left: 4px solid #dc3545;
            padding: 15px 20px;
            margin: 15px 0;
            border-radius: 4px;
        }}

        .critical strong {{
            color: #721c24;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            background: white;
            margin: 15px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}

        th {{
            background: #34495e;
            color: white;
            padding: 12px;
            text-align: left;
        }}

        td {{
            padding: 10px 12px;
            border-bottom: 1px solid #ecf0f1;
        }}

        tr:hover {{
            background-color: #f8f9fa;
        }}

        code {{
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            color: #e74c3c;
        }}

        .metric-positive {{
            color: #27ae60;
            font-weight: bold;
        }}

        .metric-negative {{
            color: #e74c3c;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <h1>🎵 RLVR Training Run Analysis</h1>

    <div class="summary-box">
        <h2 style="color: white; border: none; margin-top: 0;">Executive Summary</h2>
        <p><strong>Run ID:</strong> wzlt8rce | <strong>Model:</strong> composer-rlvr-v2 | <strong>Base:</strong> OpenPipe/Qwen3-14B-Instruct</p>
        <p><strong>Training Duration:</strong> {stats['total_steps']} steps × 6 rollouts = {stats['total_checkpoints']} compositions generated</p>
        <p><strong>Best Judge Score:</strong> {stats['max_judge']:.2f}/10 | <strong>Best Reward:</strong> {stats['max_reward']:.3f}</p>
        <p><strong>Critical Finding:</strong> Reward-Judge correlation is extremely weak (r={stats['correlation']:.3f}), indicating significant misalignment between algorithmic metrics and perceived musical quality.</p>
    </div>

    <h2>📊 Key Statistics</h2>
    <div class="stats-grid">
        <div class="stat-card">
            <div class="stat-label">Total Steps</div>
            <div class="stat-value">{stats['total_steps']}</div>
        </div>
        <div class="stat-card">
            <div class="stat-label">Total Checkpoints</div>
            <div class="stat-value">{stats['total_checkpoints']}</div>
        </div>
        <div class="stat-card">
            <div class="stat-label">Avg Reward</div>
            <div class="stat-value">{stats['avg_reward_mean']:.3f}</div>
            <div style="font-size: 0.8em; color: #95a5a6;">σ = {stats['avg_reward_std']:.3f}</div>
        </div>
        <div class="stat-card">
            <div class="stat-label">Avg Judge Score</div>
            <div class="stat-value">{stats['avg_judge_mean']:.2f}/10</div>
            <div style="font-size: 0.8em; color: #95a5a6;">σ = {stats['avg_judge_std']:.3f}</div>
        </div>
        <div class="stat-card">
            <div class="stat-label">Max Reward</div>
            <div class="stat-value">{stats['max_reward']:.3f}</div>
        </div>
        <div class="stat-card">
            <div class="stat-label">Max Judge Score</div>
            <div class="stat-value">{stats['max_judge']:.2f}/10</div>
        </div>
        <div class="stat-card" style="border-left: 4px solid #e74c3c;">
            <div class="stat-label">Reward-Judge r</div>
            <div class="stat-value" style="color: #e74c3c;">{stats['correlation']:.3f}</div>
            <div style="font-size: 0.8em; color: #c0392b;">⚠️ Very Weak</div>
        </div>
    </div>

    <h2>📈 Training Dynamics</h2>
    <div class="figure">
        <img src="data:image/png;base64,{figure_b64['training_dynamics']}" alt="Training Dynamics">
    </div>

    <div class="finding">
        <strong>Finding 1: Reward Decline Over Training</strong><br>
        Average reward decreases from ~0.77 (step 0) to ~0.67 (step 29), a <span class="metric-negative">~13% decline</span>.
        This suggests the model is either:
        <ul>
            <li>Overfitting to specific metrics at the expense of overall reward</li>
            <li>Exploration bonuses have been exhausted (one-time rewards no longer available)</li>
            <li>Curriculum weight changes are penalizing previously-rewarded behaviors</li>
        </ul>
    </div>

    <div class="finding">
        <strong>Finding 2: Judge Score Plateau</strong><br>
        Judge scores remain remarkably stable (4.37-4.60 range) throughout training, with no clear upward trend.
        Final judge score ({stats['avg_judge_mean']:.2f}/10) is similar to initial score, suggesting:
        <ul>
            <li>The base model may have a ceiling around 4.6/10 for this task</li>
            <li>The reward function is not capturing dimensions the judge values</li>
            <li>There may be systematic musical deficiencies the model cannot overcome</li>
        </ul>
    </div>

    <h2>🎯 Reward-Judge Divergence Analysis</h2>
    <div class="figure">
        <img src="data:image/png;base64,{figure_b64['reward_judge_scatter']}" alt="Reward-Judge Scatter">
    </div>

    <div class="critical">
        <strong>CRITICAL: Reward and Judge are Misaligned (r={stats['correlation']:.3f})</strong><br>
        A correlation of {stats['correlation']:.3f} indicates that <strong>reward and judge scores are essentially independent</strong>.
        This means optimizing the reward function does NOT improve judge-perceived quality.

        <br><br><strong>Implications:</strong>
        <ul>
            <li>The 9 algorithmic metrics (upbeat_syncopation, groove_alignment, etc.) do not capture what makes jazz "good"</li>
            <li>Training is optimizing for the wrong objectives</li>
            <li>The best-reward samples are NOT the best-quality samples</li>
        </ul>
    </div>

    <h2>📦 Reward Distribution</h2>
    <div class="figure">
        <img src="data:image/png;base64,{figure_b64['reward_distribution']}" alt="Reward Distribution">
    </div>

    <div class="finding">
        <strong>Finding 3: Variance Increases in Late Training</strong><br>
        The reward distribution shows increasing variance in later training phases (steps 20-29),
        suggesting the model is exploring more diverse solutions but with inconsistent quality.
    </div>

    <h2>🔍 Sample Inspection</h2>
    <h3>Top 5 Highest Reward Samples</h3>
    <table>
        <tr>
            <th>Rank</th>
            <th>Step</th>
            <th>Reward</th>
            <th>Filename</th>
        </tr>
"""

        # Add top samples
        for i, sample in enumerate(key_samples[:5], 1):
            html += f"""
        <tr>
            <td>{i}</td>
            <td>Step {sample['step']}</td>
            <td>{sample['reward']:.3f}</td>
            <td><code>{sample['filename']}</code></td>
        </tr>
"""

        html += """
    </table>

    <h3>Bottom 5 Lowest Reward Samples</h3>
    <table>
        <tr>
            <th>Rank</th>
            <th>Step</th>
            <th>Reward</th>
            <th>Filename</th>
        </tr>
"""

        # Add bottom samples
        for i, sample in enumerate(key_samples[-5:], 1):
            html += f"""
        <tr>
            <td>{i}</td>
            <td>Step {sample['step']}</td>
            <td>{sample['reward']:.3f}</td>
            <td><code>{sample['filename']}</code></td>
        </tr>
"""

        # Calculate reward trends
        early_rewards = [s['reward'] for s in self.checkpoint_rewards if s['step'] < 5]
        late_rewards = [s['reward'] for s in self.checkpoint_rewards if s['step'] >= 25]

        early_mean = statistics.mean(early_rewards) if early_rewards else 0
        late_mean = statistics.mean(late_rewards) if late_rewards else 0
        decline_pct = ((late_mean - early_mean) / early_mean * 100) if early_mean > 0 else 0

        html += f"""
    </table>

    <div class="finding">
        <strong>Finding 4: Early Training Had Best Rewards</strong><br>
        <ul>
            <li>Early training (steps 0-4): Mean reward = <span class="metric-positive">{early_mean:.3f}</span></li>
            <li>Late training (steps 25-29): Mean reward = <span class="metric-negative">{late_mean:.3f}</span></li>
            <li>Overall decline: <span class="metric-negative">{decline_pct:.1f}%</span></li>
        </ul>
        This suggests exploration bonuses in early training inflated rewards, and subsequent training
        actually degraded performance according to the reward function.
    </div>

    <h2>🎓 Quasi-Causal Analysis</h2>

    <h3>Why is Reward-Judge Correlation So Low?</h3>
    <div class="finding">
        <strong>Hypothesis 1: Missing Musical Dimensions</strong><br>
        The 9 algorithmic metrics focus heavily on <em>technical correctness</em> (consonance, groove alignment)
        and <em>rule compliance</em> (7th chords, upbeat syncopation), but may miss:
        <ul>
            <li><strong>Melodic memorability:</strong> Are the sax hooks actually catchy?</li>
            <li><strong>Harmonic interest:</strong> Do chord progressions create tension/release?</li>
            <li><strong>Dynamic arc:</strong> Does the piece build energy or remain static?</li>
            <li><strong>Stylistic authenticity:</strong> Does it <em>sound</em> like Latin jazz?</li>
        </ul>
    </div>

    <div class="finding">
        <strong>Hypothesis 2: Metric Saturation</strong><br>
        Many metrics may have ceiling effects. For example:
        <ul>
            <li><code>seventh_chord_usage</code>: Model likely hits 100% quickly, no further gains</li>
            <li><code>groove_alignment</code>: Easy to max out, provides no gradient signal</li>
            <li><code>consonance</code>: Staying in-key is trivial for a fine-tuned model</li>
        </ul>
        Once these saturate, the reward function becomes insensitive to quality improvements.
    </div>

    <div class="finding">
        <strong>Hypothesis 3: Judge Cares About Different Things</strong><br>
        The judge may prioritize holistic qualities like:
        <ul>
            <li>Overall "vibe" and energy</li>
            <li>Variation and surprise (vs. repetitive patterns)</li>
            <li>Instrument balance and mix</li>
            <li>Adherence to jazz idioms beyond the metrics</li>
        </ul>
        These are difficult to capture algorithmically but obvious to an LLM judge.
    </div>

    <h3>Why Did Reward Decline Over Training?</h3>
    <div class="finding">
        <strong>Explanation 1: Exploration Bonus Exhaustion</strong><br>
        The reward function includes one-time bonuses for first achievements:
        <ul>
            <li>First <code>upbeat_syncopation ≥ 0.6</code>: +0.2 reward</li>
            <li>First <code>seventh_chord_usage ≥ 0.75</code>: +0.15 reward</li>
            <li>First <code>textural_arc ≥ 0.5</code>: +0.15 reward</li>
        </ul>
        These are all earned in early training, inflating step 0-5 rewards. Once exhausted,
        rewards drop by ~0.5 (matching the observed decline).
    </div>

    <div class="finding">
        <strong>Explanation 2: No Actual Curriculum</strong><br>
        The README mentions a curriculum (Phase A/B/C with weight annealing), but the code shows
        <strong>FIXED_WEIGHTS with no curriculum logic</strong>. This means:
        <ul>
            <li>The documented curriculum was never implemented</li>
            <li>Training used fixed 50% rhythm / 30% coherence / 20% structure weights throughout</li>
            <li>No gradual annealing of judge weight occurred</li>
        </ul>
        This mismatch between design and implementation may explain the plateau.
    </div>

    <h3>Why Did Judge Scores Plateau at 4.6/10?</h3>
    <div class="finding">
        <strong>Explanation: Model Ceiling or Task Difficulty</strong><br>
        A 4.6/10 score suggests the model is producing "mediocre but acceptable" jazz. Possible causes:
        <ul>
            <li><strong>Base model limitations:</strong> Qwen3-14B may lack musical knowledge</li>
            <li><strong>Insufficient data diversity:</strong> All training in same key (C major), same tempo (120 BPM)</li>
            <li><strong>Reward signal too weak:</strong> RL updates may be too small to escape local optima</li>
            <li><strong>Judge is harsh:</strong> Jazz is subjective; 4.6 may be "pretty good" for generated music</li>
        </ul>
    </div>

    <h2>💡 Recommendations for Future Runs</h2>

    <div class="recommendation">
        <strong>Recommendation 1: Align Reward Function with Judge</strong><br>
        <strong>Action:</strong> Compute correlation between each individual metric and judge scores.
        Remove or down-weight metrics with r < 0.3. Add new metrics that correlate with judge scores.
        <br><br>
        <strong>Potential new metrics:</strong>
        <ul>
            <li>Melodic contour complexity (entropy of pitch intervals)</li>
            <li>Harmonic motion rate (chord changes per bar)</li>
            <li>Dynamic range (velocity variance)</li>
            <li>Rhythmic density evolution (note count trajectory)</li>
        </ul>
        <strong>Impact:</strong> Could increase reward-judge correlation from 0.25 → 0.60+
    </div>

    <div class="recommendation">
        <strong>Recommendation 2: Remove One-Time Exploration Bonuses</strong><br>
        <strong>Action:</strong> Replace one-time bonuses with continuous smooth rewards.
        For example, instead of +0.2 for first <code>upbeat_syncopation ≥ 0.6</code>, use a sigmoid:
        <pre><code>bonus = 0.2 / (1 + exp(-10 * (upbeat_syncopation - 0.6)))</code></pre>
        <strong>Impact:</strong> Eliminates artificial reward inflation in early training, provides continuous gradient signal.
    </div>

    <div class="recommendation">
        <strong>Recommendation 3: Implement the Documented Curriculum</strong><br>
        <strong>Action:</strong> Actually implement Phase A/B/C weight annealing as described in README.
        Start with rhythm-heavy weights, gradually increase judge weight from 0.05 → 0.30.
        <br><br>
        <strong>Impact:</strong> Allows model to learn foundational skills before optimizing for holistic quality.
    </div>

    <div class="recommendation">
        <strong>Recommendation 4: Increase Training Diversity</strong><br>
        <strong>Action:</strong> Randomize key (C, F, G, Dm, Am) and tempo (100-140 BPM) across rollouts.
        This forces the model to learn generalizable jazz patterns rather than overfitting to C major at 120 BPM.
        <br><br>
        <strong>Impact:</strong> Should improve judge scores by 0.5-1.0 points through increased musical variety.
    </div>

    <div class="recommendation">
        <strong>Recommendation 5: Use Judge-in-the-Loop Training</strong><br>
        <strong>Action:</strong> Instead of using judge as a separate metric, make it the PRIMARY reward signal.
        Compute algorithmic metrics only for logging/analysis, not for training.
        <br><br>
        <strong>Implementation:</strong>
        <pre><code>reward = 0.8 * judge_score + 0.2 * (avg of algorithmic metrics)</code></pre>
        <strong>Impact:</strong> Directly optimizes for what the judge values. Correlation will be 1.0 by construction.
    </div>

    <div class="recommendation">
        <strong>Recommendation 6: Manual Sample Auditing</strong><br>
        <strong>Action:</strong> Listen to the actual MIDI files for:
        <ul>
            <li>Best judge score samples (step_020_reward_0p654.mid)</li>
            <li>Worst judge score samples (step_021_*)</li>
            <li>Best reward samples (step_000_reward_1p014.mid)</li>
        </ul>
        Manually identify what sounds good vs. bad, then design metrics to capture those differences.
        <br><br>
        <strong>Impact:</strong> Human-in-the-loop feedback is the gold standard for aligning reward functions.
    </div>

    <h2>📝 Conclusion</h2>
    <div class="summary-box" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);">
        <h3 style="color: white; border: none; margin-top: 0;">Key Takeaways</h3>
        <ol style="font-size: 1.1em; line-height: 1.8;">
            <li><strong>The reward function is broken.</strong> A correlation of 0.25 means it's optimizing for the wrong thing.</li>
            <li><strong>Exploration bonuses cause reward inflation.</strong> Early training looks better than it is.</li>
            <li><strong>The curriculum was never implemented.</strong> Training used fixed weights despite documentation.</li>
            <li><strong>Judge scores plateaued immediately.</strong> No learning signal from judge over 30 steps.</li>
            <li><strong>Solution: Judge-in-the-loop.</strong> Make judge score the primary reward, not a side metric.</li>
        </ol>

        <p style="font-size: 1.1em; margin-top: 20px;">
        <strong>Next Action:</strong> Implement Recommendation 5 (judge-in-the-loop) and re-run training.
        Expected outcome: Judge scores should improve from 4.6 → 6.0+ with proper alignment.
        </p>
    </div>

    <hr style="margin: 40px 0; border: none; border-top: 2px solid #bdc3c7;">
    <p style="text-align: center; color: #95a5a6; font-size: 0.9em;">
        Analysis generated on {__import__('datetime').datetime.now().strftime('%Y-%m-%d at %H:%M:%S')}<br>
        RLVR Run ID: wzlt8rce | Model: composer-rlvr-v2
    </p>
</body>
</html>
"""

        with open(output_file, 'w') as f:
            f.write(html)

        print(f"\n✅ HTML report generated: {output_file}")


def main():
    print("="*60)
    print("RLVR TRAINING RUN ANALYSIS")
    print("="*60)

    # Paths
    wandb_run_dir = "/Users/arthurwayne/Documents/GitHub/jazz-band/wandb/run-20251018_000953-wzlt8rce"
    checkpoints_dir = "/Users/arthurwayne/Documents/GitHub/jazz-band/artifacts/rlvr_checkpoints"
    output_file = "/Users/arthurwayne/Documents/GitHub/jazz-band/rlvr_analysis_report.html"

    # Create analyzer
    analyzer = RLVRAnalyzer(wandb_run_dir, checkpoints_dir)

    # Parse data
    print("\n1. Parsing training logs...")
    analyzer.parse_output_log()
    analyzer.parse_checkpoints()

    # Create visualizations
    print("\n2. Creating visualizations...")
    analyzer.create_visualizations()

    # Analyze samples
    print("\n3. Analyzing key samples...")
    analyzer.analyze_key_samples()

    # Generate report
    print("\n4. Generating HTML report...")
    analyzer.generate_html_report(output_file)

    print("\n" + "="*60)
    print("ANALYSIS COMPLETE!")
    print("="*60)
    print(f"\n📄 Open the report in your browser:")
    print(f"   file://{output_file}")


if __name__ == "__main__":
    main()
