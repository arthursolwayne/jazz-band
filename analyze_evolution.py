#!/usr/bin/env python3
"""Analyze GEPA evolution results across generations."""

import json
from pathlib import Path
from collections import defaultdict

def main():
    elites_dir = Path("artifacts/elites")

    # Collect all metrics by generation
    gen_data = defaultdict(list)

    for metrics_path in sorted(elites_dir.glob("*/metrics.json")):
        with open(metrics_path) as f:
            data = json.load(f)
        gen = data["generation"]
        gen_data[gen].append(data)

    print("=" * 80)
    print("GEPA EVOLUTION ANALYSIS - 15 Generations with Strict Jazz Judge")
    print("=" * 80)
    print()

    # Overall statistics
    print("OVERALL STATISTICS:")
    print(f"Total generations: {max(gen_data.keys()) + 1}")
    print(f"Total elites archived: {sum(len(v) for v in gen_data.values())}")
    print()

    # Best individual per generation
    print("BEST INDIVIDUAL PER GENERATION (by judge_score):")
    print("-" * 80)
    print(f"{'Gen':<5} {'Best Judge':<12} {'Consonance':<12} {'Groove':<8} {'Motif':<8} {'Interplay':<10} {'Density':<8}")
    print("-" * 80)

    best_per_gen = []
    for gen in sorted(gen_data.keys()):
        individuals = gen_data[gen]
        best = max(individuals, key=lambda x: x["objectives"]["judge_score"])
        best_per_gen.append(best)

        obj = best["objectives"]
        print(f"{gen:<5} {obj['judge_score']:<12.2f} {obj['consonance']:<12.2f} "
              f"{obj['groove_alignment']:<8.2f} {obj['motif_coherence']:<8.2f} "
              f"{obj['interplay']:<10.2f} {obj['density_regularity']:<8.2f}")

    print()
    print("-" * 80)
    print()

    # Score progression analysis
    print("JUDGE SCORE PROGRESSION:")
    print("-" * 80)
    early_gens = [d for gen, individuals in gen_data.items() if gen < 5
                  for d in individuals]
    mid_gens = [d for gen, individuals in gen_data.items() if 5 <= gen < 10
                for d in individuals]
    late_gens = [d for gen, individuals in gen_data.items() if gen >= 10
                 for d in individuals]

    def avg_judge(individuals):
        scores = [d["objectives"]["judge_score"] for d in individuals]
        return sum(scores) / len(scores) if scores else 0

    print(f"Early gens (0-4):  avg = {avg_judge(early_gens):.2f}, "
          f"max = {max((d['objectives']['judge_score'] for d in early_gens), default=0):.2f}")
    print(f"Mid gens (5-9):    avg = {avg_judge(mid_gens):.2f}, "
          f"max = {max((d['objectives']['judge_score'] for d in mid_gens), default=0):.2f}")
    print(f"Late gens (10-14): avg = {avg_judge(late_gens):.2f}, "
          f"max = {max((d['objectives']['judge_score'] for d in late_gens), default=0):.2f}")

    print()
    print("-" * 80)
    print()

    # Top 5 overall
    all_individuals = [d for individuals in gen_data.values() for d in individuals]
    top_5 = sorted(all_individuals, key=lambda x: x["objectives"]["judge_score"], reverse=True)[:5]

    print("TOP 5 INDIVIDUALS OVERALL:")
    print("-" * 80)
    for i, ind in enumerate(top_5, 1):
        obj = ind["objectives"]
        print(f"{i}. Gen {ind['generation']}, Ind {ind['individual_id']}: "
              f"Judge={obj['judge_score']:.2f} "
              f"(consonance={obj['consonance']:.2f}, "
              f"groove={obj['groove_alignment']:.2f}, "
              f"motif={obj['motif_coherence']:.2f}, "
              f"interplay={obj['interplay']:.2f}, "
              f"density={obj['density_regularity']:.2f})")

    print()
    print("=" * 80)
    print()

    # Check for critique files to analyze jazz-specific scores
    critique_found = False
    for elite_dir in sorted(elites_dir.iterdir()):
        if not elite_dir.is_dir():
            continue
        critique_path = elite_dir / "critique.json"
        if critique_path.exists():
            critique_found = True
            break

    if critique_found:
        print("JAZZ-SPECIFIC CRITERION ANALYSIS:")
        print("-" * 80)

        # Collect all critiques
        gen_critiques = defaultdict(list)
        for elite_dir in sorted(elites_dir.iterdir()):
            if not elite_dir.is_dir():
                continue

            metrics_path = elite_dir / "metrics.json"
            critique_path = elite_dir / "critique.json"

            if metrics_path.exists() and critique_path.exists():
                with open(metrics_path) as f:
                    metrics = json.load(f)
                with open(critique_path) as f:
                    critique = json.load(f)

                gen = metrics["generation"]
                gen_critiques[gen].append({
                    "ind_id": metrics["individual_id"],
                    "overall": critique.get("overall_score", 0),
                    "scores": critique.get("scores", {})
                })

        # Average jazz scores by generation phase
        def avg_jazz_scores(critiques):
            if not critiques:
                return {}

            keys = ["jazz_harmony", "jazz_rhythm", "jazz_melody", "interplay_space", "jazz_authenticity"]
            avg = {}
            for key in keys:
                scores = [c["scores"].get(key, 0) for c in critiques if key in c["scores"]]
                avg[key] = sum(scores) / len(scores) if scores else 0
            return avg

        early_critiques = [c for gen, crits in gen_critiques.items() if gen < 5 for c in crits]
        mid_critiques = [c for gen, crits in gen_critiques.items() if 5 <= gen < 10 for c in crits]
        late_critiques = [c for gen, crits in gen_critiques.items() if gen >= 10 for c in crits]

        early_avg = avg_jazz_scores(early_critiques)
        mid_avg = avg_jazz_scores(mid_critiques)
        late_avg = avg_jazz_scores(late_critiques)

        print(f"{'Criterion':<20} {'Early (0-4)':<15} {'Mid (5-9)':<15} {'Late (10-14)':<15}")
        print("-" * 80)

        for key in ["jazz_harmony", "jazz_rhythm", "jazz_melody", "interplay_space", "jazz_authenticity"]:
            e = early_avg.get(key, 0)
            m = mid_avg.get(key, 0)
            l = late_avg.get(key, 0)
            delta = l - e
            arrow = "↑" if delta > 0.5 else ("↓" if delta < -0.5 else "→")
            print(f"{key:<20} {e:>6.2f}          {m:>6.2f}          {l:>6.2f}  {arrow} ({delta:+.2f})")

        print()
        print("=" * 80)

        # Find best and worst critiques
        all_critiques_with_gen = [(gen, c) for gen, crits in gen_critiques.items() for c in crits]
        if all_critiques_with_gen:
            best_critique = max(all_critiques_with_gen, key=lambda x: x[1]["overall"])
            worst_critique = min(all_critiques_with_gen, key=lambda x: x[1]["overall"])

            print()
            print("BEST CRITIQUE (highest overall score):")
            print(f"Gen {best_critique[0]}, Ind {best_critique[1]['ind_id']}: {best_critique[1]['overall']:.1f}/10")
            print(f"  Scores: {best_critique[1]['scores']}")

            print()
            print("WORST CRITIQUE (lowest overall score):")
            print(f"Gen {worst_critique[0]}, Ind {worst_critique[1]['ind_id']}: {worst_critique[1]['overall']:.1f}/10")
            print(f"  Scores: {worst_critique[1]['scores']}")
            print()

if __name__ == "__main__":
    main()
