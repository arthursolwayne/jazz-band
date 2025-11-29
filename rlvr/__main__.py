"""Entry point for `python -m rlvr`."""

import argparse
import asyncio
from .loop import train

parser = argparse.ArgumentParser(description="RLVR Training")
parser.add_argument("--steps", type=int, default=20, help="Training steps")
parser.add_argument("--rollouts", type=int, default=8, help="Rollouts per step")
parser.add_argument("--dry-run", action="store_true", help="Use mock metrics")
args = parser.parse_args()

summary = asyncio.run(train(
    num_steps=args.steps,
    rollouts_per_step=args.rollouts,
    dry_run=args.dry_run,
))
print(f"Done: {summary}")
