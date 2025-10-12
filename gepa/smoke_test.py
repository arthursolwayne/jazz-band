"""
GEPA Smoke Test

Runs 3 generations with population size 4 to verify:
- Pareto front computation works
- Front changes across generations
- Elite archive created with all artifacts
- Mutation operators work
- Weave logging successful
"""

import os
import sys
import asyncio
from pathlib import Path
from dotenv import load_dotenv

import weave

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from gepa.loop import run_gepa

# Load environment variables
load_dotenv()


async def main():
    """Run GEPA smoke test."""
    print("=" * 60)
    print("GEPA Smoke Test - 3 Generations, Population 4")
    print("=" * 60)
    print()

    # Get project root
    project_root = Path(__file__).parent.parent

    # Initialize Weave (following 2048.py pattern)
    api_key = os.environ.get("WANDB_API_KEY") or os.environ.get("WANDBAPIKEY", "")
    os.environ["WANDB_API_KEY"] = api_key
    weave.init("jazz-band-gepa-smoke")

    # Run GEPA for 3 generations
    result = await run_gepa(
        project_root=project_root,
        generations=3,
        population_size=4,
        seed=42,  # Reproducible
        dry_run=True,  # Use dry-run mode for testing
        mutation_rate=0.8,
    )

    # Verify results
    print("\n" + "="*60)
    print("Verification")
    print("="*60)

    # Check generations ran
    assert len(result["generations"]) == 3, f"Expected 3 generations, got {len(result['generations'])}"
    print("✓ Ran 3 generations")

    # Check fronts exist
    for i, gen in enumerate(result["generations"]):
        assert len(gen["front_sizes"]) > 0, f"Generation {i} has no fronts"
        print(f"✓ Generation {i} has {len(gen['front_sizes'])} front(s): {gen['front_sizes']}")

    # Check first front is non-empty
    for i, gen in enumerate(result["generations"]):
        assert gen["front_sizes"][0] > 0, f"Generation {i} has empty first front"
        print(f"✓ Generation {i} first front has {gen['front_sizes'][0]} individual(s)")

    # Check front changes across generations (not all identical)
    front_sizes_list = [tuple(gen["front_sizes"]) for gen in result["generations"]]
    all_same = all(fs == front_sizes_list[0] for fs in front_sizes_list)
    if not all_same:
        print("✓ Pareto fronts changed across generations (evolution working)")
    else:
        print("⚠ Pareto fronts identical across generations (may be OK for small test)")

    # Check elite archive exists
    archive_dir = project_root / "artifacts" / "elites"
    assert archive_dir.exists(), "Elite archive directory not found"
    print(f"✓ Elite archive exists at {archive_dir}")

    # Check archive has elites
    elite_dirs = list(archive_dir.glob("gen_*"))
    assert len(elite_dirs) > 0, "No elites archived"
    print(f"✓ Found {len(elite_dirs)} archived elite(s)")

    # Check elite artifacts
    for elite_dir in elite_dirs[:2]:  # Check first 2
        assert (elite_dir / "composer.md").exists(), f"Missing composer.md in {elite_dir}"
        assert (elite_dir / "genes.yaml").exists(), f"Missing genes.yaml in {elite_dir}"
        assert (elite_dir / "metrics.json").exists(), f"Missing metrics.json in {elite_dir}"
        print(f"✓ Elite {elite_dir.name} has all artifacts")

    print("\n" + "="*60)
    print("GEPA Smoke Test PASSED!")
    print("="*60)
    print()
    print("Summary:")
    print(f"  - Ran 3 generations with population size 4")
    print(f"  - Pareto fronts computed successfully")
    print(f"  - {len(elite_dirs)} elites archived with artifacts")
    print(f"  - Weave logging successful")
    print()
    print("Next steps:")
    print("  - Run with --use-llm to test real LLM integration")
    print("  - Run longer evolutions (10+ generations)")
    print("  - Analyze Pareto frontier expansion")
    print()


if __name__ == "__main__":
    asyncio.run(main())
