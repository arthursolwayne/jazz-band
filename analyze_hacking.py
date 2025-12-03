#!/usr/bin/env python3
"""Detect reward hacking patterns in feature evolution."""

import json
from pathlib import Path
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

def load_all_rollouts(base_path: Path, run_id: str = None) -> list[dict]:
    """Load all meta.json files from rollouts."""
    rollouts = []
    for meta_file in base_path.rglob("meta.json"):
        try:
            with open(meta_file) as f:
                data = json.load(f)
                parts = meta_file.parts
                for i, part in enumerate(parts):
                    if part == "rollouts" and i + 1 < len(parts):
                        data["run_id"] = parts[i + 1]
                        break
                if run_id is None or data.get("run_id") == run_id:
                    rollouts.append(data)
        except Exception as e:
            pass
    return rollouts


def extract_feature_trajectories(rollouts: list[dict]) -> dict:
    """Extract per-feature values over training steps."""
    by_step = defaultdict(list)
    for r in rollouts:
        step = r.get("step", 0)
        by_step[step].append(r)

    features = {
        "sax": ["melodic_entropy", "dur_cv", "sax_arpeggio_runs", "peak_not_late", "blue_ratio", "rhythm_2grams"],
        "bass": ["duration_variety", "velocity_variance", "non_chromatic_ratio"],
        "piano": ["unique_chords", "avg_chord_duration", "cluster_ratio", "out_of_key_ratio", "chord_duration_variety"],
        "drums": ["duration_variety", "kick_off_beat_ratio", "velocity_variance"],
    }

    trajectories = {inst: {f: {"raw": [], "z": [], "steps": []} for f in feats}
                    for inst, feats in features.items()}

    for step in sorted(by_step.keys()):
        for r in by_step[step]:
            if not r.get("has_midi") or "breakdown" not in r:
                continue
            bd = r["breakdown"]

            for inst, feats in features.items():
                detail = bd.get(f"{inst}_detail", {})
                feature_dict = detail.get("features", {})

                for f in feats:
                    if f in feature_dict:
                        trajectories[inst][f]["steps"].append(step)
                        trajectories[inst][f]["raw"].append(feature_dict[f].get("raw", 0))
                        trajectories[inst][f]["z"].append(feature_dict[f].get("z_score", 0))

    return trajectories


def compute_step_means(trajectories: dict) -> dict:
    """Aggregate features by step."""
    result = {}
    for inst, feats in trajectories.items():
        result[inst] = {}
        for f, data in feats.items():
            if not data["steps"]:
                continue
            by_step = defaultdict(list)
            for s, raw, z in zip(data["steps"], data["raw"], data["z"]):
                by_step[s].append((raw, z))

            steps = sorted(by_step.keys())
            result[inst][f] = {
                "steps": steps,
                "raw_mean": [np.mean([x[0] for x in by_step[s]]) for s in steps],
                "raw_std": [np.std([x[0] for x in by_step[s]]) for s in steps],
                "z_mean": [np.mean([x[1] for x in by_step[s]]) for s in steps],
                "z_std": [np.std([x[1] for x in by_step[s]]) for s in steps],
            }
    return result


def detect_hacking_patterns(agg: dict) -> dict:
    """Identify potential reward hacking signals."""
    issues = []

    for inst, feats in agg.items():
        for f, data in feats.items():
            if not data["steps"]:
                continue

            # 1. Z-score saturation (hitting clamp at ±3)
            final_z = data["z_mean"][-1] if data["z_mean"] else 0
            if abs(final_z) > 2.8:
                issues.append({
                    "type": "z_saturation",
                    "instrument": inst,
                    "feature": f,
                    "final_z": final_z,
                    "severity": "high" if abs(final_z) > 2.95 else "medium"
                })

            # 2. Unrealistic raw values (e.g., always 0 or 1)
            raw_vals = data["raw_mean"]
            if len(raw_vals) > 10:
                late_vals = raw_vals[-10:]
                if all(v == 0 for v in late_vals) or all(v == 1 for v in late_vals):
                    issues.append({
                        "type": "degenerate_raw",
                        "instrument": inst,
                        "feature": f,
                        "value": late_vals[-1],
                        "severity": "high"
                    })

            # 3. Variance collapse (all rollouts same value)
            if len(data["raw_std"]) > 10:
                late_std = data["raw_std"][-10:]
                if np.mean(late_std) < 0.01:
                    issues.append({
                        "type": "variance_collapse",
                        "instrument": inst,
                        "feature": f,
                        "mean_std": np.mean(late_std),
                        "severity": "medium"
                    })

            # 4. Sudden jumps (exploitation discovery)
            if len(data["z_mean"]) > 5:
                diffs = np.diff(data["z_mean"])
                max_jump = np.max(np.abs(diffs))
                if max_jump > 1.5:
                    jump_idx = np.argmax(np.abs(diffs))
                    issues.append({
                        "type": "sudden_jump",
                        "instrument": inst,
                        "feature": f,
                        "step": data["steps"][jump_idx + 1],
                        "magnitude": max_jump,
                        "severity": "medium"
                    })

    return issues


def plot_feature_heatmap(agg: dict, output_dir: Path):
    """Create heatmap of feature z-scores over training."""
    output_dir.mkdir(parents=True, exist_ok=True)

    for inst, feats in agg.items():
        feat_names = list(feats.keys())
        if not feat_names:
            continue

        # Get common steps
        all_steps = set()
        for f in feat_names:
            all_steps.update(feats[f]["steps"])
        steps = sorted(all_steps)

        if len(steps) < 2:
            continue

        # Build matrix
        matrix = np.zeros((len(feat_names), len(steps)))
        for i, f in enumerate(feat_names):
            step_to_z = dict(zip(feats[f]["steps"], feats[f]["z_mean"]))
            for j, s in enumerate(steps):
                matrix[i, j] = step_to_z.get(s, 0)

        # Plot
        fig, ax = plt.subplots(figsize=(14, max(3, len(feat_names) * 0.6)))

        im = ax.imshow(matrix, aspect='auto', cmap='RdYlGn', vmin=-3, vmax=3)
        ax.set_yticks(range(len(feat_names)))
        ax.set_yticklabels(feat_names)

        # X-axis ticks
        tick_spacing = max(1, len(steps) // 10)
        ax.set_xticks(range(0, len(steps), tick_spacing))
        ax.set_xticklabels([steps[i] for i in range(0, len(steps), tick_spacing)])

        ax.set_xlabel("Training Step")
        ax.set_title(f"{inst.upper()} Feature Z-Scores", fontweight='bold', fontsize=14)

        plt.colorbar(im, ax=ax, label="Z-Score")
        plt.tight_layout()
        plt.savefig(output_dir / f"heatmap_{inst}.png", dpi=150)
        plt.close()
        print(f"Saved: {output_dir / f'heatmap_{inst}.png'}")


def plot_feature_lines(agg: dict, output_dir: Path):
    """Create line plots for each instrument's features."""
    output_dir.mkdir(parents=True, exist_ok=True)

    colors = plt.cm.tab10.colors

    for inst, feats in agg.items():
        feat_names = list(feats.keys())
        if not feat_names:
            continue

        # Z-score plot
        fig, ax = plt.subplots(figsize=(12, 6))

        for i, f in enumerate(feat_names):
            if not feats[f]["steps"]:
                continue
            ax.plot(feats[f]["steps"], feats[f]["z_mean"],
                    color=colors[i % len(colors)], linewidth=2,
                    marker='o', markersize=2, label=f)

        ax.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
        ax.axhline(y=3, color='red', linestyle='--', alpha=0.3, label="Clamp +3")
        ax.axhline(y=-3, color='red', linestyle='--', alpha=0.3)
        ax.set_xlabel("Training Step")
        ax.set_ylabel("Z-Score")
        ax.set_title(f"{inst.upper()} Feature Z-Scores Over Training", fontweight='bold')
        ax.legend(loc="upper left", fontsize=9, ncol=2)
        ax.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig(output_dir / f"features_{inst}_zscore.png", dpi=150)
        plt.close()
        print(f"Saved: {output_dir / f'features_{inst}_zscore.png'}")

        # Raw values plot
        fig, ax = plt.subplots(figsize=(12, 6))

        for i, f in enumerate(feat_names):
            if not feats[f]["steps"]:
                continue
            ax.plot(feats[f]["steps"], feats[f]["raw_mean"],
                    color=colors[i % len(colors)], linewidth=2,
                    marker='o', markersize=2, label=f)

        ax.set_xlabel("Training Step")
        ax.set_ylabel("Raw Value")
        ax.set_title(f"{inst.upper()} Feature Raw Values Over Training", fontweight='bold')
        ax.legend(loc="upper left", fontsize=9, ncol=2)
        ax.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig(output_dir / f"features_{inst}_raw.png", dpi=150)
        plt.close()
        print(f"Saved: {output_dir / f'features_{inst}_raw.png'}")


def main():
    base_path = Path("artifacts/rollouts")
    run_id = "composer-001_20251201_201755"  # Latest 100-step run

    print(f"Loading data for run: {run_id}")
    rollouts = load_all_rollouts(base_path, run_id)
    print(f"Loaded {len(rollouts)} rollouts")

    print("\nExtracting feature trajectories...")
    trajectories = extract_feature_trajectories(rollouts)

    print("Aggregating by step...")
    agg = compute_step_means(trajectories)

    print("\n" + "=" * 60)
    print("REWARD HACKING ANALYSIS")
    print("=" * 60)

    issues = detect_hacking_patterns(agg)

    if issues:
        print(f"\nFound {len(issues)} potential issues:\n")
        for issue in sorted(issues, key=lambda x: (x["severity"], x["instrument"])):
            sev = "⚠️ " if issue["severity"] == "high" else "⚡ "
            print(f"{sev}[{issue['type']}] {issue['instrument']}.{issue['feature']}")
            for k, v in issue.items():
                if k not in ["type", "instrument", "feature"]:
                    print(f"    {k}: {v}")
            print()
    else:
        print("\nNo obvious reward hacking patterns detected.")

    # Print feature summary
    print("\n" + "=" * 60)
    print("FEATURE TRAJECTORY SUMMARY (start → end)")
    print("=" * 60)

    for inst in ["sax", "bass", "piano", "drums"]:
        print(f"\n{inst.upper()}:")
        for f, data in agg.get(inst, {}).items():
            if data["steps"]:
                start_z = data["z_mean"][0]
                end_z = data["z_mean"][-1]
                start_raw = data["raw_mean"][0]
                end_raw = data["raw_mean"][-1]
                sat = " [SATURATED]" if abs(end_z) > 2.8 else ""
                print(f"  {f:25s} z: {start_z:+6.2f} → {end_z:+6.2f}  raw: {start_raw:6.2f} → {end_raw:6.2f}{sat}")

    output_dir = Path("artifacts/analysis") / run_id
    print(f"\nGenerating feature plots...")
    plot_feature_heatmap(agg, output_dir)
    plot_feature_lines(agg, output_dir)


if __name__ == "__main__":
    main()
