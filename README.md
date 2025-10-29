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

**Fixed Weights** (no curriculum):
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

## Key Findings

### 1. RLVR Outperforms GEPA on Judge Quality
- RLVR: 4.8/10 best, 4.57/10 average final
- GEPA: 4.0/10 best, 3.7/10 average final
- Both used 180 total evaluations (equal sample efficiency)

### 2. Critical Discovery: Metric Saturation Epidemic
**56% of RLVR's reward function is saturated** (variance < 0.05):
- `upbeat_syncopation`: **Zero variance** across all 30 steps (stuck at 0.5)
- `groove_alignment`, `seventh_chords`, `textural_arc`, `harmonic_movement`: All frozen
- Only 3 metrics show learning: `dynamic_contrast`, `melodic_exploration`, `rhythmic_variety`

**Impact**: The reward function provides almost no learning signal. Training effectively optimizes <35% of the reward.

### 3. Reward-Judge Misalignment
- **Correlation: 0.25** (essentially independent)
- Best judge score (4.8) came from sample with reward 0.654 (below average)
- Best reward (1.014) came from step 0 due to exploration bonuses, not quality

**Root Cause**: Algorithmic metrics measure *technical correctness* (stay in key, use 7th chords) but miss *musical quality* (catchiness, groove feel, harmonic interest).

### 4. Both Methods Plateau Around 4.5/10
- Neither approach broke past ~4.8/10 judge scores
- Model learned constraints (7th chords, upbeat emphasis) but not deeper musicality
- Suggests need for human-in-the-loop or learned reward models

### 5. Training Dynamics Differ
- **GEPA**: Fluctuates (3.6-4.0) due to evolutionary exploration
- **RLVR**: Remarkably stable (4.37-4.60 per-step average)
- RLVR's stability suggests consistent but mediocre quality

---

## Next Steps: Judge-in-the-Loop for Both Methods

Based on the analysis, **both GEPA and RLVR should use judge score as the primary reward signal**:

### Proposed Reward Design (for both methods):
```python
reward = 0.50 × judge_score + 0.50 × algorithmic_metrics
```

Where `algorithmic_metrics` only includes actively-learning metrics:
- Remove saturated metrics (upbeat_syncopation, groove_alignment, seventh_chords, etc.)
- Keep only: dynamic_contrast (0.15), melodic_exploration (0.15), rhythmic_variety (0.15), consonance (0.05)

### Expected Improvements:
1. **Alignment**: Reward-judge correlation will be 1.0 by construction
2. **Learning signal**: Judge provides holistic gradient (not saturated)
3. **Higher ceiling**: Should break past 4.8/10 plateau
4. **Consistency**: Both methods optimize for same objective

### Implementation Plan:
- **GEPA**: Add judge_score weight (0.50) to Pareto objectives, reduce other weights
- **RLVR**: Update `FIXED_WEIGHTS` to judge-primary design
- Re-run both for 30 iterations with new reward design

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
├── analysis/              # Training run analysis reports
│   ├── rlvr_analysis_report.html
│   ├── rlvr_deep_dive_findings.html
│   └── metric_rewards_simple.html
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

### Play Best Samples
```bash
# GEPA best (4.0/10)
python scripts/play_midi.py artifacts/elites/gen_012_ind_0003/jam.mid

# RLVR best (4.8/10, reward 0.654 - shows misalignment)
python scripts/play_midi.py artifacts/rlvr_checkpoints/step_020_reward_0p654.mid
```

### Analyze Training Run
```bash
python analyze_rlvr_run.py  # Generates comprehensive HTML reports
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

## Current Status

✅ **Completed**:
- GEPA training (30 generations, best: 4.0/10)
- RLVR training (30 steps, best: 4.8/10)
- Comprehensive analysis revealing metric saturation and reward-judge misalignment

🚧 **In Progress**:
- Implementing judge-in-the-loop reward design for both methods
- Re-training with new reward weights (judge_score primary signal)

📊 **Analysis Reports**: See `rlvr_analysis_report.html` for full findings
