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

## Running GEPA
```bash
uv run python -m gepa --dry-run --generations 3 --population 4   # Test mode
uv run python -m gepa --generations 2 --population 4              # Real evolution
```

## Running Tests
```bash
uv run python tests/test_rlvr.py
uv run python tests/test_gepa.py
```

## Key Files
- `rlvr/loop.py` - Training loop (ART/GRPO)
- `rlvr/eval.py` - Reward function (dummy: has notes → 1.0)
- `gepa/loop.py` - Evolution loop (Pareto selection)
- `gepa/eval.py` - Pareto fronts, survivor selection
