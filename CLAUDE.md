# Claude Code Instructions

## Package Management
Use `uv` for all package management:
```bash
uv sync          # Install/sync dependencies
uv add <pkg>     # Add a package
uv run <cmd>     # Run command in venv
```

## Running RLVR
```bash
uv run python -m rlvr --dry-run --steps 3 --rollouts 4   # Test mode
uv run python -m rlvr --steps 1 --rollouts 2              # Real training
```

## Running Tests
```bash
uv run python tests/test_rlvr.py
```

## Key Files
- `rlvr/loop.py` - Training loop (ART/GRPO)
- `rlvr/eval.py` - Reward function
- `gepa/loop.py` - Evolution loop (TODO)
- `src/jazz_band/metrics.py` - Metrics (TODO)
