"""Tests for GEPA evolution loop."""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from gepa.loop import evolve
from gepa.pareto import Individual, dominates, compute_pareto_fronts, select_survivors


def test_dry_run_one_generation():
    """Verify evolve() completes 1 generation in dry-run mode."""
    summary = asyncio.run(evolve(generations=1, population_size=4, dry_run=True))
    assert summary["generations"] == 1
    assert "best_reward" in summary
    print("✓ test_dry_run_one_generation")


def test_dry_run_multiple_generations():
    """Verify evolve() completes multiple generations."""
    summary = asyncio.run(evolve(generations=3, population_size=4, dry_run=True))
    assert summary["generations"] == 3
    print("✓ test_dry_run_multiple_generations")


def test_dominates():
    """Test dominance relation."""
    a = Individual(id=0, prompt="", metrics={"x": 1.0, "y": 1.0})
    b = Individual(id=1, prompt="", metrics={"x": 0.5, "y": 0.5})
    c = Individual(id=2, prompt="", metrics={"x": 1.0, "y": 0.5})
    d = Individual(id=3, prompt="", metrics={"x": 0.5, "y": 1.0})

    assert dominates(a, b) == True   # a dominates b (better on both)
    assert dominates(b, a) == False  # b does not dominate a
    assert dominates(a, c) == True   # a dominates c (equal on x, better on y)
    assert dominates(c, a) == False  # c does not dominate a
    assert dominates(a, d) == True   # a dominates d (better on x, equal on y)
    assert dominates(c, d) == False  # c and d are incomparable (Pareto front)
    assert dominates(d, c) == False  # c and d are incomparable
    print("✓ test_dominates")


def test_pareto_fronts():
    """Test Pareto front computation."""
    pop = [
        Individual(id=0, prompt="", metrics={"x": 1.0, "y": 0.0}),
        Individual(id=1, prompt="", metrics={"x": 0.0, "y": 1.0}),
        Individual(id=2, prompt="", metrics={"x": 0.5, "y": 0.5}),
        Individual(id=3, prompt="", metrics={"x": 0.2, "y": 0.2}),
    ]

    fronts = compute_pareto_fronts(pop)

    # First front should contain the non-dominated individuals
    assert len(fronts) >= 1
    front0_ids = {ind.id for ind in fronts[0]}
    # id=0, id=1 are on Pareto front (neither dominates the other)
    # id=2 might also be non-dominated depending on interpretation
    assert 0 in front0_ids or 1 in front0_ids
    print("✓ test_pareto_fronts")


def test_select_survivors():
    """Test survivor selection."""
    pop = [
        Individual(id=0, prompt="", metrics={"x": 1.0}),
        Individual(id=1, prompt="", metrics={"x": 0.8}),
        Individual(id=2, prompt="", metrics={"x": 0.5}),
        Individual(id=3, prompt="", metrics={"x": 0.2}),
    ]

    survivors = select_survivors(pop, target_size=2)
    assert len(survivors) == 2
    # Best should survive
    survivor_ids = {s.id for s in survivors}
    assert 0 in survivor_ids
    print("✓ test_select_survivors")


if __name__ == "__main__":
    test_dry_run_one_generation()
    test_dry_run_multiple_generations()
    test_dominates()
    test_pareto_fronts()
    test_select_survivors()
    print("\nAll tests passed!")
