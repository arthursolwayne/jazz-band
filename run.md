# Training Commands

## GEPA Training
30 generations, no early stopping, population size 6

```bash
uv run python -m gepa.loop \
  --generations 30 \
  --population-size 6 \
  --use-llm \
  --no-early-stopping \
  --seed 42
```

## RLVR Training
30 steps, 6 rollouts per step, learning rate 1e-5

```bash
uv run python -m rlvr.loop \
  --steps 30 \
  --rollouts 6 \
  --lr 1e-5
```

## Run Both in Background

```bash
# GEPA (in background with output logging)
nohup uv run python -m gepa.loop \
  --generations 30 \
  --population-size 6 \
  --use-llm \
  --no-early-stopping \
  --seed 42 \
  > gepa_training.log 2>&1 &

# RLVR (in background with output logging)
nohup uv run python -m rlvr.loop \
  --steps 30 \
  --rollouts 6 \
  --lr 1e-5 \
  > rlvr_training.log 2>&1 &
```

## Monitor Progress

```bash
# Tail GEPA logs
tail -f gepa_training.log

# Tail RLVR logs
tail -f rlvr_training.log

# Check running processes
ps aux | grep "gepa.loop\|rlvr.loop"
```

## Wandb Dashboards

- **GEPA**: https://wandb.ai/arthursolwayne-penn/jazz-band-gepa
- **RLVR**: https://wandb.ai/arthursolwayne-penn/jazz-band-rlvr

## Features

Both training systems now include:
- ✅ Parallel Judge evaluation (5 criterion judges + 1 aggregator)
- ✅ Real-time metrics logging to Wandb
- ✅ Full evaluation tracking (scores, rewards, objectives)
- ✅ 5-instrument ensemble (bass, snare, hihat, piano, sax)
- ✅ Progressive arrangement building (bar 1: hihat only, bars 2-4: full ensemble)
- ✅ 4-bar loop structure for tighter, catchier compositions
- ✅ Textured bass with varied note durations
- ✅ Varied sax note lengths for rhythmic interest
