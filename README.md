# JITSY Jazz
## Just-in-Time Symbolic Jazz: Comparing In-Context Learning vs Reinforcement Learning for Compositional Skills

![JITSY Jazz](jit-sy_jazz.png)

**Listen to samples**: [Audio Examples on Google Drive](https://drive.google.com/drive/folders/1jTNRG4S9uhjCpqjoJWInKOqZM51ORmS_?usp=drive_link)

---

## Overview

This project explores how language models acquire *new* compositional skills through two approaches:
1. **GEPA** (Genetic-Evolutionary Prompt Adaptation): Multi-objective prompt evolution with LLM-based mutation
2. **RLVR** (Reinforcement Learning with Verifiable Rewards): Trajectory-based RL with algorithmic metrics

**The Task**: Generate 8-bar Latin jazz compositions in JamJSON format (5 instruments: bass, drums, piano, sax, trumpet)

**Inspired by**:
- [RL for Reasoning with One Training Example](https://arxiv.org/abs/2504.20571) - Verifiable rewards unlock latent reasoning
- [In-Context Learning Dynamics](https://arxiv.org/abs/2507.16003) - ICL implements implicit weight updates
- [GEPA Paper](https://arxiv.org/abs/2507.19457) - Prompt evolution outperforms RL on reasoning tasks

---

## Tech Stack

- **music21**: Symbolic score representation and MIDI generation
- **OpenPipe/ART**: RL training framework (Qwen3-14B-Instruct base model)
- **W&B Weave**: Telemetry, logging, and artifact tracking
- **Custom**: JamJSON schema, multi-objective Pareto optimization (NSGA-II)

---

## Methods

### GEPA: Evolutionary Prompt Optimization

**Approach**: Evolve a population of 6 individuals, each with:
- **Numerical genes** (chord_density, syncopation_target, motif_reuse_weight, etc.)
- **Textual prompts** (do/don't lists mutated by Judge LLM feedback)

**Training Loop** (30 generations):
1. Generate 8-bar composition for each individual
2. Evaluate on 6 objectives: consonance, groove, motif coherence, interplay, density, judge score
3. Compute Pareto front (NSGA-II)
4. Select top 50% by Pareto rank + crowding distance
5. Mutate prompts via Judge LLM critique + Gaussian noise on genes
6. Crossover survivors to create next generation

### RLVR: Reinforcement Learning with Fixed Reward Weights

**Approach**: Fine-tune Qwen3-14B via policy gradient RL using trajectory-based training (OpenPipe/ART)

**Training Loop** (30 steps, 6 rollouts/step):
1. Generate 8-bar composition using current model checkpoint
2. Compute 9 verifiable metrics (upbeat syncopation, 7th chords, groove, etc.)
3. Calculate reward: `R = Σ(w_i × metric_i) + exploration_bonuses - penalties`
4. Train model on trajectories using advantage-weighted policy gradient
5. Save checkpoint if reward improves

**Reward Metrics**:
| Metric | Weight | Description |
|--------|--------|-------------|
| upbeat_syncopation | 0.25 | % hihat hits on upbeats (target >0.6) |
| groove_alignment | 0.15 | Bass-drum downbeat correlation |
| seventh_chords | 0.10 | % bars with 7th chords |
| textural_arc | 0.10 | Progressive instrument activation |
| rhythmic_variety | 0.10 | Duration entropy + motif repetition |
| dynamic_contrast | 0.10 | Between-instrument variance |
| melodic_exploration | 0.10 | Pitch range + stepwise motion |
| harmonic_movement | 0.05 | Chord change rate (1-3 per 8 bars) |
| consonance | 0.05 | % notes in key scale |

---

## Repository Structure

```
jazz-band/
├── src/jazz_band/          # Core agents (Composer, Judge, memory, MIDI export)
├── gepa/                   # Evolutionary prompt optimization
│   ├── loop.py            # Main training loop
│   ├── population.py      # Individual/Population classes
│   ├── evaluate.py        # 6D objective computation
│   ├── pareto.py          # NSGA-II Pareto optimization
│   └── mutate.py          # LLM-based prompt mutation
├── rlvr/                   # Reinforcement learning approach
│   ├── loop.py            # ART training loop
│   ├── reward.py          # Fixed-weight reward calculation
│   └── metrics.py         # 9 verifiable metrics
├── artifacts/
│   ├── elites/            # GEPA Pareto front snapshots
│   └── rlvr_checkpoints/  # RLVR model checkpoints + MIDI exports
└── README.md
```

---

## Running the Code

### GEPA Training
```bash
python -m gepa.loop --generations 30 --population-size 6 --mutation-rate 0.8
```

### RLVR Training
```bash
python -m rlvr.loop --steps 30 --rollouts 6 --lr 1e-5
```

### Play Generated Samples
```bash
# Play a GEPA composition
python scripts/play_midi.py artifacts/elites/gen_012_ind_0003/jam.mid

# Play an RLVR composition
python scripts/play_midi.py artifacts/rlvr_checkpoints/step_020_reward_0p654.mid
```

---

## Citation

```bibtex
@misc{jitsyjazz2025,
  title={JITSY Jazz: Just-in-Time Symbolic Jazz for Compositional Skill Learning},
  author={Wayne, Arthur},
  year={2025},
  url={https://github.com/arthursolwayne/jazz-band}
}
```

---

## About This Project

This is an exploration of compositional skill acquisition in language models, comparing evolutionary prompt optimization (GEPA) with trajectory-based reinforcement learning (RLVR). Both approaches aim to teach models complex structured tasks—in this case, multi-instrument jazz composition with stylistic constraints—without explicit supervised examples.
