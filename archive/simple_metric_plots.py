#!/usr/bin/env python3
"""
Simple 9-panel plot showing each metric's reward contribution across 30 steps.
"""

import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path
import base64
from io import BytesIO

sns.set_style("whitegrid")

# FIXED_WEIGHTS from rlvr/reward.py
WEIGHTS = {
    'upbeat_syncopation': 0.25,
    'groove_alignment': 0.15,
    'seventh_chords': 0.10,
    'textural_arc': 0.10,
    'rhythmic_variety': 0.10,
    'dynamic_contrast': 0.10,
    'melodic_exploration': 0.10,
    'harmonic_movement': 0.05,
    'consonance': 0.05,
}

def parse_metrics_from_log():
    """Extract all metrics for each step from the wandb output log"""
    log_file = Path("/Users/arthurwayne/Documents/GitHub/jazz-band/wandb/run-20251018_000953-wzlt8rce/files/output.log")

    with open(log_file, 'r') as f:
        content = f.read()

    pattern = r"Step (\d+): 100%.*?reward=([\d.]+).*?upbeat_syncopation=([\d.]+).*?groove_alignment=([\d.]+).*?seventh_chord_usage=([\d.]+).*?textural_arc=([\d.]+).*?rhythmic_variety=([\d.]+).*?dynamic_contrast=([\d.]+).*?melodic_exploration=([\d.]+).*?harmonic_movement=([\d.]+).*?consonance=([\d.]+)"

    matches = re.findall(pattern, content)

    data = {
        'step': [],
        'upbeat_syncopation': [],
        'groove_alignment': [],
        'seventh_chords': [],
        'textural_arc': [],
        'rhythmic_variety': [],
        'dynamic_contrast': [],
        'melodic_exploration': [],
        'harmonic_movement': [],
        'consonance': [],
    }

    for match in matches:
        data['step'].append(int(match[0]))
        data['upbeat_syncopation'].append(float(match[2]) * WEIGHTS['upbeat_syncopation'])
        data['groove_alignment'].append(float(match[3]) * WEIGHTS['groove_alignment'])
        data['seventh_chords'].append(float(match[4]) * WEIGHTS['seventh_chords'])
        data['textural_arc'].append(float(match[5]) * WEIGHTS['textural_arc'])
        data['rhythmic_variety'].append(float(match[6]) * WEIGHTS['rhythmic_variety'])
        data['dynamic_contrast'].append(float(match[7]) * WEIGHTS['dynamic_contrast'])
        data['melodic_exploration'].append(float(match[8]) * WEIGHTS['melodic_exploration'])
        data['harmonic_movement'].append(float(match[9]) * WEIGHTS['harmonic_movement'])
        data['consonance'].append(float(match[10]) * WEIGHTS['consonance'])

    return data

def create_9_panel_plot(data):
    """Create 3x3 grid of individual metric plots"""
    fig, axes = plt.subplots(3, 3, figsize=(18, 12))
    fig.suptitle('Individual Metric Reward Contributions Across Training Steps',
                 fontsize=18, fontweight='bold', y=0.995)

    steps = data['step']
    metrics = list(WEIGHTS.keys())

    for idx, (ax, metric) in enumerate(zip(axes.flat, metrics)):
        values = data[metric]
        weight = WEIGHTS[metric]

        # Plot line
        ax.plot(steps, values, 'o-', linewidth=2, markersize=5, color=f'C{idx}', alpha=0.8)

        # Add horizontal mean line
        mean_val = np.mean(values)
        ax.axhline(y=mean_val, color='red', linestyle='--', linewidth=1.5, alpha=0.6,
                   label=f'Mean: {mean_val:.4f}')

        # Styling
        ax.set_xlabel('Training Step', fontsize=11, fontweight='bold')
        ax.set_ylabel('Reward Contribution', fontsize=11, fontweight='bold')
        ax.set_title(f'{metric}\n(weight={weight:.2f})', fontsize=12, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.legend(loc='best', fontsize=9)

        # Set consistent x-axis
        ax.set_xlim(-1, 30)
        ax.set_xticks(range(0, 31, 5))

    plt.tight_layout()
    return fig

def generate_html_report(fig_base64, data):
    """Generate simple HTML report with the 9-panel plot"""

    # Calculate stats for each metric
    stats = []
    for metric in WEIGHTS.keys():
        values = data[metric]
        stats.append({
            'metric': metric,
            'weight': WEIGHTS[metric],
            'mean': np.mean(values),
            'std': np.std(values),
            'min': np.min(values),
            'max': np.max(values),
            'range': np.max(values) - np.min(values),
        })

    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Individual Metric Rewards Over Training</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            max-width: 1800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}

        h1 {{
            color: #2c3e50;
            text-align: center;
        }}

        .figure {{
            background: white;
            padding: 20px;
            margin: 30px 0;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}

        .figure img {{
            width: 100%;
            height: auto;
            border-radius: 4px;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            background: white;
            margin: 20px 0;
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

        .note {{
            background: #d1ecf1;
            border-left: 4px solid #17a2b8;
            padding: 15px 20px;
            margin: 20px 0;
            border-radius: 4px;
        }}
    </style>
</head>
<body>
    <h1>📊 Individual Metric Rewards Over 30 Training Steps</h1>

    <div class="note">
        <p><strong>What you're seeing:</strong> Each subplot shows one metric's weighted reward contribution (metric_value × weight) across all 30 training steps.</p>
        <p>The red dashed line shows the mean contribution. Flat lines indicate saturated metrics with no learning.</p>
    </div>

    <div class="figure">
        <img src="data:image/png;base64,{fig_base64}" alt="9 Panel Metric Plot">
    </div>

    <h2>📈 Statistics Summary</h2>
    <table>
        <thead>
            <tr>
                <th>Metric</th>
                <th>Weight</th>
                <th>Mean Contribution</th>
                <th>Std Dev</th>
                <th>Min</th>
                <th>Max</th>
                <th>Range</th>
            </tr>
        </thead>
        <tbody>
"""

    for stat in stats:
        html += f"""
            <tr>
                <td><strong>{stat['metric']}</strong></td>
                <td>{stat['weight']:.2f}</td>
                <td>{stat['mean']:.4f}</td>
                <td>{stat['std']:.4f}</td>
                <td>{stat['min']:.4f}</td>
                <td>{stat['max']:.4f}</td>
                <td>{stat['range']:.4f}</td>
            </tr>
"""

    html += """
        </tbody>
    </table>

    <div class="note">
        <strong>Key Observations:</strong>
        <ul>
            <li>Metrics with low std dev and range are saturated (not learning)</li>
            <li>Metrics with higher std dev show actual learning dynamics</li>
            <li>The x-axis goes from 0 (first step) to 29 (final step)</li>
        </ul>
    </div>

    <hr style="margin: 40px 0;">
    <p style="text-align: center; color: #95a5a6; font-size: 0.9em;">
        Generated on 2025-10-18 | 9 metrics × 30 steps
    </p>
</body>
</html>
"""

    return html

def main():
    print("="*60)
    print("SIMPLE 9-PANEL METRIC PLOT")
    print("="*60)

    # Parse data
    print("\n1. Parsing metrics from training log...")
    data = parse_metrics_from_log()
    print(f"   ✓ Extracted {len(data['step'])} steps")

    # Create plot
    print("\n2. Creating 9-panel plot...")
    fig = create_9_panel_plot(data)

    # Convert to base64
    print("\n3. Generating HTML report...")
    buf = BytesIO()
    fig.savefig(buf, format='png', dpi=150, bbox_inches='tight')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    plt.close(fig)

    html = generate_html_report(img_base64, data)

    output_file = Path("/Users/arthurwayne/Documents/GitHub/jazz-band/metric_rewards_simple.html")
    with open(output_file, 'w') as f:
        f.write(html)

    print(f"\n✅ Report generated: {output_file}")
    print(f"\n📄 Open in browser:")
    print(f"   file://{output_file.absolute()}")

if __name__ == "__main__":
    main()
