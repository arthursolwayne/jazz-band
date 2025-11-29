# JITSY Jazz

Comparing RLVR vs GEPA for teaching LLMs to compose jazz.

## Structure

```
rlvr/                 # Reinforcement Learning with Verifiable Rewards
  loop.py             # train: rollout → metrics → reward → gradient descent
  eval.py             # weighted sum of metrics → scalar reward

gepa/                 # Genetic-Evolutionary Prompt Adaptation
  loop.py             # evolve: rollout → metrics → Pareto select → mutate prompt
  eval.py             # Pareto selection + prompt mutation

src/jazz_band/
  metrics.py          # 9 verifiable metrics (shared by both)
  orchestra.py        # MIDI program/channel/pitch constants

prompts/              # system prompts (TODO: wire up)
reference_riffs/      # 5 sample MIDIs
archive/              # old analysis, artifacts, wandb logs
```

## The Comparison

Both use the **same 9 metrics** for evaluation. The difference is optimization:

| | RLVR | GEPA |
|-|------|------|
| **Optimizes** | Model weights | Prompt text |
| **Method** | Gradient descent | LLM reflection + Pareto selection |
| **Prompt** | Fixed | Evolves |
| **Weights** | Learned | Fixed |

## Metrics

| Metric | Weight | Target |
|--------|--------|--------|
| upbeat_syncopation | 0.25 | >0.6 |
| groove_alignment | 0.15 | bass-drum correlation |
| seventh_chord_usage | 0.10 | >0.75 |
| textural_arc | 0.10 | progressive build |
| rhythmic_variety | 0.10 | duration entropy |
| dynamic_contrast | 0.10 | velocity variance |
| melodic_exploration | 0.10 | pitch range + steps |
| harmonic_movement | 0.05 | 1-3 changes/4 bars |
| consonance | 0.05 | % in key |

## Run

```bash
# RLVR
python -m rlvr.loop --steps 30 --dry-run

# GEPA
python -m gepa.loop --generations 30 --dry-run
```

## Reference Riffs

| File | Song | Artist | Key | BPM |
|------|------|--------|-----|-----|
| `cantina_jazzband.mid` | Cantina Band | John Williams | Dm | 270 |
| `moanin_jazzband.mid` | Moanin' | Art Blakey | Fm | 150 |
| `watermelon_jazzband.mid` | Watermelon Man | Herbie Hancock | F | 200 |
| `sowhat_jazzband.mid` | So What | Miles Davis | D dorian | 236 |
| `songformyfather_jazzband.mid` | Song for My Father | Horace Silver | Fm | 120 |

All adapted to 5-part setup: bass, snare, hihat, piano, sax. 4 bars each.

## Status

Scaffolding complete. All functions stubbed with `NotImplementedError` for pretty_midi implementation.
