# JITSY Jazz

Jazz lives between structure and freedom. Musical conventions are programmatically checkable—chord voicings, syncopation, bass lines—but artistry lies in knowing when to follow the rules and when to break them.

We compare two paradigms for teaching LLMs creative skills under verifiable constraints: **prompt evolution** (GEPA) refines instructions through self-reflection without weight updates, while **reinforcement learning** (RLVR) embeds knowledge through gradient descent. Both generate 4-bar jazz ensembles on the same model (Qwen3-14B-Instruct), evaluated with identical deterministic metrics. All 30,000 generated MIDIs and reward traces included for reproducibility.

## Structure

```
rlvr/                 # Reinforcement Learning with Verifiable Rewards
  loop.py             # train: rollout → reward → gradient descent

gepa/                 # Genetic-Evolutionary Prompt Adaptation
  loop.py             # evolve: rollout → Pareto select → mutate prompt
  pareto.py           # Pareto selection logic

src/jazz_band/
  symbol_engine.py    # shared: prompt, execute_midi_code, compute_reward

prompts/
  composer.md         # system prompt for LLM
  judge.md            # (TODO) for GEPA reflective mutation

reference_riffs/      # 5 sample MIDIs
archive/              # old analysis, artifacts, wandb logs
```

## The Comparison

Both generate pretty_midi Python code via LLM, execute it, compute reward.

| | RLVR | GEPA |
|-|------|------|
| **Optimizes** | Model weights | Prompt text |
| **Method** | Gradient descent (GRPO) | LLM reflection + Pareto selection |
| **Prompt** | Fixed | Evolves |
| **Weights** | Learned | Fixed |

## Ensemble

Jazz quartet: piano, bass, drums (kick/snare/hihat), tenor sax.

4 bars at 160 BPM = 6.0 seconds.

## Setup

```bash
uv sync   # Install dependencies
```

## Run

```bash
# RLVR
uv run python -m rlvr --dry-run --steps 3 --rollouts 4   # Test mode
uv run python -m rlvr --steps 1 --rollouts 2              # Real training

# GEPA
uv run python -m gepa --dry-run --generations 3 --population 4   # Test mode
uv run python -m gepa --generations 2 --population 4              # Real evolution
```

## Reference Riffs

| File | Song | Artist | Key | BPM |
|------|------|--------|-----|-----|
| `cantina_jazzband.mid` | Cantina Band | John Williams | Dm | 270 |
| `moanin_jazzband.mid` | Moanin' | Art Blakey | Fm | 150 |
| `watermelon_jazzband.mid` | Watermelon Man | Herbie Hancock | F | 200 |
| `sowhat_jazzband.mid` | So What | Miles Davis | D dorian | 236 |
| `songformyfather_jazzband.mid` | Song for My Father | Horace Silver | Fm | 120 |
