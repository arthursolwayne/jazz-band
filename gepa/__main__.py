"""Entry point for `python -m gepa`."""

import argparse
import asyncio
from .loop import evolve

parser = argparse.ArgumentParser(description="GEPA Evolution")
parser.add_argument("--generations", type=int, default=10, help="Number of generations")
parser.add_argument("--population", type=int, default=8, help="Population size")
parser.add_argument("--dry-run", action="store_true", help="Use mock rewards")
parser.add_argument("--project", default="jazz-band-gepa", help="W&B project")
parser.add_argument("--base-model", default="OpenPipe/Qwen3-14B-Instruct", help="Base model")
args = parser.parse_args()

summary = asyncio.run(evolve(
    generations=args.generations,
    population_size=args.population,
    dry_run=args.dry_run,
    project=args.project,
    base_model=args.base_model,
))
