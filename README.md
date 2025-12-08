# JITSY Jazz

Jazz occupies the space between structure and freedom. A pianist knows the ii-V-I progression, but artistry lies in how she voices the chords, when she anticipates the resolution, or whether she substitutes a tritone or plays it straight. The conventions are real—checkable, even—but blindly following them produces mechanical music. Creativity emerges from knowing when structure serves expression and when to break free.

This tension makes jazz an ideal domain for studying how language models acquire creative skills under enabling constraints. Unlike open-ended text generation, musical conventions can be verified programmatically: we can check whether chords are voiced correctly, whether rhythms syncopate, whether the bass walks. Yet verification alone does not capture quality. The same chord progression played mechanically sounds lifeless; played with intention, it swings.

Two paradigms have emerged for adapting language models for task-specific learning. Prompt evolution (Agrawal et al. 2025) refines natural-language instructions through self-reflection and selection. This approach has demonstrated strong results on structured tasks, such as arithmetic, sometimes matching gradient-based methods while using far fewer training samples. Reinforcement learning (Sutton and Barto 1998; Wang et al. 2025) updates weights through reward signals, embedding task knowledge into internal representations. Despite theoretical interest in comparing these approaches, no prior work has evaluated them head-to-head on the same creative task with the same metrics.

We implement both in-context evolution and reinforcement learning on the same model (Qwen3-14B-Instruct) to generate 4-bar jazz ensemble compositions in executable Python code using the `pretty_midi` library (Raffel and Ellis 2014). Our primary contributions are threefold:

**(1) Comparative training dynamics:** Our work is the first direct comparison of prompt evolution vs. RL for creative generation. Prior work evaluates methods in isolation; we offer a comparative look into the tradeoffs in training dynamics, evaluated head-to-head on the same task with identical model, metrics, and random seeds.

**(2) Verifiable reward infrastructure:** We avoid learned reward models entirely, using only symbolic MIDI analysis. Every metric is deterministic and re-runnable from the open-sourced code repository which includes 30,000 generated MIDI files with corresponding data.

**(3) Methodological blueprint:** Our framework generalizes to any domain where conventions are programmatically checkable but true competence requires knowing when to violate them: code synthesis with unit tests, protein design with folding constraints, game level generation with playability checks.

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
