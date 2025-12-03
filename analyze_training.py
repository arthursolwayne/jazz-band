#!/usr/bin/env python3
"""Analyze RLVR training dynamics with line graphs."""

import json
from pathlib import Path
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

def load_all_rollouts(base_path: Path) -> list[dict]:
    """Load all meta.json files from rollouts."""
    rollouts = []
    for meta_file in base_path.rglob("meta.json"):
        try:
            with open(meta_file) as f:
                data = json.load(f)
                # Extract run_id from path
                parts = meta_file.parts
                for i, part in enumerate(parts):
                    if part == "rollouts" and i + 1 < len(parts):
                        data["run_id"] = parts[i + 1]
                        break
                rollouts.append(data)
        except Exception as e:
            print(f"Error loading {meta_file}: {e}")
    return rollouts


def aggregate_by_step(rollouts: list[dict], run_id: str = None) -> dict:
    """Aggregate rollout data by step."""
    if run_id:
        rollouts = [r for r in rollouts if r.get("run_id") == run_id]

    by_step = defaultdict(list)
    for r in rollouts:
        step = r.get("step", 0)
        by_step[step].append(r)
    return dict(sorted(by_step.items()))


def extract_metrics(step_data: dict) -> dict:
    """Extract metrics with mean/std for each step."""
    metrics = {
        "reward": [],
        "sax_sig": [],
        "bass_sig": [],
        "piano_sig": [],
        "drums_sig": [],
        "sax_z": [],
        "bass_z": [],
        "piano_z": [],
        "drums_z": [],
        "ensemble_mult": [],
        "z_sum": [],
        # Gates
        "sax_variety_gate": [],
        "bass_chromatic_gate": [],
        "bass_direction_gate": [],
        "piano_tonic_bonus": [],
    }

    result = {}
    for step, rollouts in step_data.items():
        step_metrics = {k: [] for k in metrics}

        for r in rollouts:
            if not r.get("has_midi") or "breakdown" not in r:
                continue
            bd = r["breakdown"]

            step_metrics["reward"].append(r.get("reward", 0))
            step_metrics["sax_sig"].append(bd.get("sax_sig", 0))
            step_metrics["bass_sig"].append(bd.get("bass_sig", 0))
            step_metrics["piano_sig"].append(bd.get("piano_sig", 0))
            step_metrics["drums_sig"].append(bd.get("drums_sig", 0))
            step_metrics["sax_z"].append(bd.get("sax", 0))
            step_metrics["bass_z"].append(bd.get("bass", 0))
            step_metrics["piano_z"].append(bd.get("piano", 0))
            step_metrics["drums_z"].append(bd.get("drums", 0))
            step_metrics["ensemble_mult"].append(bd.get("ensemble_mult", 1.0))
            step_metrics["z_sum"].append(bd.get("z_sum", 0))

            # Gates from detail sections
            sax_detail = bd.get("sax_detail", {})
            bass_detail = bd.get("bass_detail", {})
            piano_detail = bd.get("piano_detail", {})

            step_metrics["sax_variety_gate"].append(sax_detail.get("variety_gate", 1.0))
            step_metrics["bass_chromatic_gate"].append(bass_detail.get("chromatic_gate", 1.0))
            step_metrics["bass_direction_gate"].append(bass_detail.get("direction_gate", 1.0))
            step_metrics["piano_tonic_bonus"].append(piano_detail.get("tonic_bonus", 1.0))

        result[step] = {}
        for k, vals in step_metrics.items():
            if vals:
                result[step][k] = {
                    "mean": np.mean(vals),
                    "std": np.std(vals),
                    "min": np.min(vals),
                    "max": np.max(vals),
                    "n": len(vals),
                }
            else:
                result[step][k] = {"mean": 0, "std": 0, "min": 0, "max": 0, "n": 0}

    return result


def plot_training_dynamics(metrics: dict, run_id: str, output_dir: Path):
    """Create line graphs for training dynamics."""
    output_dir.mkdir(parents=True, exist_ok=True)

    steps = sorted(metrics.keys())
    if not steps:
        print("No data to plot!")
        return

    # Style settings
    plt.style.use('seaborn-v0_8-darkgrid')

    # Color palette
    colors = {
        "reward": "#2ecc71",
        "sax": "#e74c3c",
        "bass": "#3498db",
        "piano": "#9b59b6",
        "drums": "#f39c12",
        "ensemble": "#1abc9c",
    }

    # === FIGURE 1: Top-Level Reward ===
    fig, ax = plt.subplots(figsize=(12, 6))

    means = [metrics[s]["reward"]["mean"] for s in steps]
    stds = [metrics[s]["reward"]["std"] for s in steps]

    ax.plot(steps, means, color=colors["reward"], linewidth=2.5, marker='o', markersize=4, label="Mean Reward")
    ax.fill_between(steps,
                    np.array(means) - np.array(stds),
                    np.array(means) + np.array(stds),
                    alpha=0.2, color=colors["reward"])

    ax.set_xlabel("Training Step", fontsize=12)
    ax.set_ylabel("Combined Reward", fontsize=12)
    ax.set_title(f"Training Dynamics: Combined Reward\n{run_id}", fontsize=14, fontweight='bold')
    ax.legend(loc="lower right")
    ax.set_ylim(0, 1.15)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_dir / "01_reward_toplevel.png", dpi=150)
    plt.close()
    print(f"Saved: {output_dir / '01_reward_toplevel.png'}")

    # === FIGURE 2: Per-Instrument Sigmoid Scores ===
    fig, ax = plt.subplots(figsize=(12, 6))

    instruments = [("sax_sig", "Sax", "sax"),
                   ("bass_sig", "Bass", "bass"),
                   ("piano_sig", "Piano", "piano"),
                   ("drums_sig", "Drums", "drums")]

    for key, label, color_key in instruments:
        means = [metrics[s][key]["mean"] for s in steps]
        stds = [metrics[s][key]["std"] for s in steps]
        ax.plot(steps, means, color=colors[color_key], linewidth=2, marker='o', markersize=3, label=label)
        ax.fill_between(steps,
                        np.array(means) - np.array(stds),
                        np.array(means) + np.array(stds),
                        alpha=0.15, color=colors[color_key])

    ax.set_xlabel("Training Step", fontsize=12)
    ax.set_ylabel("Sigmoid Score (0-1)", fontsize=12)
    ax.set_title(f"Per-Instrument Sigmoid Scores\n{run_id}", fontsize=14, fontweight='bold')
    ax.legend(loc="lower right", ncol=2)
    ax.set_ylim(0, 1.05)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_dir / "02_instrument_sigmoid.png", dpi=150)
    plt.close()
    print(f"Saved: {output_dir / '02_instrument_sigmoid.png'}")

    # === FIGURE 3: Per-Instrument Raw Z-Scores ===
    fig, ax = plt.subplots(figsize=(12, 6))

    z_instruments = [("sax_z", "Sax", "sax"),
                     ("bass_z", "Bass", "bass"),
                     ("piano_z", "Piano", "piano"),
                     ("drums_z", "Drums", "drums")]

    for key, label, color_key in z_instruments:
        means = [metrics[s][key]["mean"] for s in steps]
        stds = [metrics[s][key]["std"] for s in steps]
        ax.plot(steps, means, color=colors[color_key], linewidth=2, marker='o', markersize=3, label=label)
        ax.fill_between(steps,
                        np.array(means) - np.array(stds),
                        np.array(means) + np.array(stds),
                        alpha=0.15, color=colors[color_key])

    ax.axhline(y=0, color='gray', linestyle='--', linewidth=1, alpha=0.7)
    ax.set_xlabel("Training Step", fontsize=12)
    ax.set_ylabel("Z-Score (raw)", fontsize=12)
    ax.set_title(f"Per-Instrument Z-Scores (before sigmoid)\n{run_id}", fontsize=14, fontweight='bold')
    ax.legend(loc="lower right", ncol=2)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_dir / "03_instrument_zscore.png", dpi=150)
    plt.close()
    print(f"Saved: {output_dir / '03_instrument_zscore.png'}")

    # === FIGURE 4: Gate Activations ===
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Sax Variety Gate
    ax = axes[0, 0]
    means = [metrics[s]["sax_variety_gate"]["mean"] for s in steps]
    ax.plot(steps, means, color=colors["sax"], linewidth=2, marker='o', markersize=4)
    ax.axhline(y=1.0, color='green', linestyle='--', alpha=0.5, label="No penalty")
    ax.axhline(y=0.5, color='red', linestyle='--', alpha=0.5, label="50% penalty")
    ax.set_xlabel("Step")
    ax.set_ylabel("Gate Value")
    ax.set_title("Sax: Variety Gate", fontweight='bold')
    ax.set_ylim(0.4, 1.1)
    ax.legend(loc="lower right", fontsize=9)
    ax.grid(True, alpha=0.3)

    # Bass Chromatic Gate
    ax = axes[0, 1]
    means = [metrics[s]["bass_chromatic_gate"]["mean"] for s in steps]
    ax.plot(steps, means, color=colors["bass"], linewidth=2, marker='o', markersize=4)
    ax.axhline(y=1.0, color='green', linestyle='--', alpha=0.5)
    ax.axhline(y=0.5, color='red', linestyle='--', alpha=0.5)
    ax.set_xlabel("Step")
    ax.set_ylabel("Gate Value")
    ax.set_title("Bass: Chromatic Gate", fontweight='bold')
    ax.set_ylim(0.4, 1.1)
    ax.grid(True, alpha=0.3)

    # Bass Direction Gate
    ax = axes[1, 0]
    means = [metrics[s]["bass_direction_gate"]["mean"] for s in steps]
    ax.plot(steps, means, color=colors["bass"], linewidth=2, marker='o', markersize=4, linestyle='--')
    ax.axhline(y=1.0, color='green', linestyle='--', alpha=0.5)
    ax.axhline(y=0.5, color='red', linestyle='--', alpha=0.5)
    ax.set_xlabel("Step")
    ax.set_ylabel("Gate Value")
    ax.set_title("Bass: Direction Gate", fontweight='bold')
    ax.set_ylim(0.4, 1.1)
    ax.grid(True, alpha=0.3)

    # Piano Tonic Bonus
    ax = axes[1, 1]
    means = [metrics[s]["piano_tonic_bonus"]["mean"] for s in steps]
    ax.plot(steps, means, color=colors["piano"], linewidth=2, marker='o', markersize=4)
    ax.axhline(y=1.2, color='green', linestyle='--', alpha=0.5, label="Full bonus (1.2x)")
    ax.axhline(y=1.0, color='gray', linestyle='--', alpha=0.5, label="No bonus")
    ax.set_xlabel("Step")
    ax.set_ylabel("Bonus Multiplier")
    ax.set_title("Piano: Tonic Bonus", fontweight='bold')
    ax.set_ylim(0.9, 1.25)
    ax.legend(loc="lower right", fontsize=9)
    ax.grid(True, alpha=0.3)

    plt.suptitle(f"Gate Activations Over Training\n{run_id}", fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig(output_dir / "04_gates.png", dpi=150)
    plt.close()
    print(f"Saved: {output_dir / '04_gates.png'}")

    # === FIGURE 5: Ensemble Multiplier ===
    fig, ax = plt.subplots(figsize=(12, 5))

    means = [metrics[s]["ensemble_mult"]["mean"] for s in steps]
    stds = [metrics[s]["ensemble_mult"]["std"] for s in steps]

    ax.plot(steps, means, color=colors["ensemble"], linewidth=2.5, marker='o', markersize=4)
    ax.fill_between(steps,
                    np.array(means) - np.array(stds),
                    np.array(means) + np.array(stds),
                    alpha=0.2, color=colors["ensemble"])

    ax.axhline(y=1.0, color='gray', linestyle='--', alpha=0.5, label="Baseline (no coherence)")
    ax.axhline(y=1.1, color='green', linestyle='--', alpha=0.5, label="Max bonus (1.1x)")

    ax.set_xlabel("Training Step", fontsize=12)
    ax.set_ylabel("Ensemble Multiplier", fontsize=12)
    ax.set_title(f"Ensemble Coherence Multiplier\n{run_id}", fontsize=14, fontweight='bold')
    ax.legend(loc="lower right")
    ax.set_ylim(0.98, 1.12)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_dir / "05_ensemble.png", dpi=150)
    plt.close()
    print(f"Saved: {output_dir / '05_ensemble.png'}")

    # === FIGURE 6: Z-Sum Distribution ===
    fig, ax = plt.subplots(figsize=(12, 5))

    means = [metrics[s]["z_sum"]["mean"] for s in steps]
    stds = [metrics[s]["z_sum"]["std"] for s in steps]
    mins = [metrics[s]["z_sum"]["min"] for s in steps]
    maxs = [metrics[s]["z_sum"]["max"] for s in steps]

    ax.plot(steps, means, color=colors["reward"], linewidth=2.5, marker='o', markersize=4, label="Mean")
    ax.fill_between(steps, mins, maxs, alpha=0.15, color=colors["reward"], label="Min-Max Range")
    ax.fill_between(steps,
                    np.array(means) - np.array(stds),
                    np.array(means) + np.array(stds),
                    alpha=0.3, color=colors["reward"], label="±1 Std")

    ax.axhline(y=0, color='gray', linestyle='--', linewidth=1, alpha=0.7)
    ax.set_xlabel("Training Step", fontsize=12)
    ax.set_ylabel("Total Z-Sum", fontsize=12)
    ax.set_title(f"Z-Score Sum Distribution\n{run_id}", fontsize=14, fontweight='bold')
    ax.legend(loc="lower right")
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_dir / "06_zsum_distribution.png", dpi=150)
    plt.close()
    print(f"Saved: {output_dir / '06_zsum_distribution.png'}")


def print_summary(metrics: dict, run_id: str):
    """Print summary statistics."""
    steps = sorted(metrics.keys())
    if not steps:
        return

    print(f"\n{'='*60}")
    print(f"TRAINING DYNAMICS SUMMARY: {run_id}")
    print(f"{'='*60}")
    print(f"Total steps: {len(steps)} (from {min(steps)} to {max(steps)})")

    first = metrics[steps[0]]
    last = metrics[steps[-1]]

    print(f"\n{'Metric':<25} {'Start':>10} {'End':>10} {'Change':>10}")
    print("-" * 55)

    for key in ["reward", "sax_sig", "bass_sig", "piano_sig", "drums_sig", "ensemble_mult"]:
        start = first[key]["mean"]
        end = last[key]["mean"]
        change = end - start
        sign = "+" if change > 0 else ""
        print(f"{key:<25} {start:>10.4f} {end:>10.4f} {sign}{change:>9.4f}")

    print(f"\n{'='*60}")


def main():
    base_path = Path("artifacts/rollouts")
    output_base = Path("artifacts/analysis")

    print("Loading rollout data...")
    all_rollouts = load_all_rollouts(base_path)
    print(f"Loaded {len(all_rollouts)} rollouts")

    # Get unique run IDs
    run_ids = sorted(set(r.get("run_id", "unknown") for r in all_rollouts))
    print(f"Found runs: {run_ids}")

    # Analyze each run
    for run_id in run_ids:
        print(f"\nAnalyzing run: {run_id}")
        step_data = aggregate_by_step(all_rollouts, run_id)

        if not step_data:
            print(f"  No data for {run_id}")
            continue

        metrics = extract_metrics(step_data)
        print_summary(metrics, run_id)

        output_dir = output_base / run_id
        plot_training_dynamics(metrics, run_id, output_dir)

    # Also create combined analysis for latest/longest run
    if run_ids:
        # Find run with most steps
        best_run = max(run_ids, key=lambda rid: len(aggregate_by_step(all_rollouts, rid)))
        print(f"\n{'='*60}")
        print(f"PRIMARY RUN FOR ANALYSIS: {best_run}")
        print(f"{'='*60}")


if __name__ == "__main__":
    main()
