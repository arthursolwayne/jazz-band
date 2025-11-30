"""Entry point for `python -m rlvr`."""

import argparse
import asyncio
from .loop import train

parser = argparse.ArgumentParser(description="RLVR Training")
parser.add_argument("--steps", type=int, default=20, help="Training steps")
parser.add_argument("--rollouts", type=int, default=24, help="Rollouts per step")
parser.add_argument("--dry-run", action="store_true", help="Use mock rewards")
parser.add_argument("--project", default="jazz-band-rlvr", help="W&B project")
parser.add_argument("--model-name", default="composer-001", help="Model name")
parser.add_argument("--base-model", default="OpenPipe/Qwen3-14B-Instruct", help="Base model")
parser.add_argument("--resume", type=str, default=None, help="Run ID to resume")
args = parser.parse_args()

summary = asyncio.run(train(
    num_steps=args.steps,
    rollouts_per_step=args.rollouts,
    dry_run=args.dry_run,
    project=args.project,
    model_name=args.model_name,
    base_model=args.base_model,
    resume=args.resume,
))
print(f"Done: {summary}")
