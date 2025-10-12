# Agent Jazz Band - Development Roadmap

## Subplan 1: Core Score & Schema ✓ COMPLETED

Foundation for symbolic music generation with music21 and W&B Weave telemetry.

- [x] Init repo with **uv**; add `music21`, `wandb`, `weave`; write `README.md`
- [x] Define **JamJSON** spec (docstring) + validator **stub**
- [x] Implement **OrchestraSpec** and **ScoreBuilder** (incl. GM drums on channel 10)
- [x] Add **MIDI export** + brief console summary
- [x] Create **smoke test** that logs to Weave using **only `WANDBAPIKEY`** (pattern from `2048.py`)
- [x] Verify a run with `session_000.mid` appears; update `TODO.md` and link next subplan

### Deliverables
- `src/jazz_band/schema.py` - JamJSON specification and validator
- `src/jazz_band/orchestra.py` - Five-instrument ensemble configuration
- `src/jazz_band/score_builder.py` - JamJSON → music21 → MIDI conversion
- `tests/smoke_test.py` - Integration test with Weave logging
- `artifacts/session_000.mid` - Example 4-bar jazz arrangement

---

## Subplan 2: Agents & Judge ✓ COMPLETED

LLM-based agents with chemistry memory and dry-run testing mode.

- [x] Create prompt templates (prompts/composer.md, judge.md)
- [x] Implement ChemistryMemory (MotifBank, StyleVector, InterplayLedger)
- [x] Implement Composer agent interface with dry-run mode
- [x] Implement Judge agent interface with dry-run mode
- [x] Create LLM wrapper mirroring 2048.py pattern (WANDBAPIKEY only)
- [x] Build agents_smoke_test.py flow
- [x] Verify Weave run with session_001.mid and memory.json
- [x] Update README with agent usage examples

### Deliverables
- `prompts/composer.md`, `prompts/judge.md` - Agent system prompts
- `src/jazz_band/memory/chemistry.py` - Pattern tracking (motifs, style, interplay)
- `src/jazz_band/agents/llm.py` - LLM wrapper with dry-run mode
- `src/jazz_band/agents/composer.py` - Composer agent (generates bars)
- `src/jazz_band/agents/judge.py` - Judge agent (evaluates & critiques)
- `tests/agents_smoke_test.py` - Integration test
- `artifacts/session_001.mid` - Extended 8-bar arrangement
- `artifacts/memory.json` - Chemistry memory snapshot

### Key Features
- Dry-run mode works without LLM (deterministic stubs for testing)
- LLM mode uses OpenAI API with Weave logging
- Chemistry memory tracks motifs, style characteristics, and interplay
- Judge provides 4-dimensional scoring (harmony, rhythm, melody, interplay)
- Composer uses memory and context to generate coherent continuations

---

## Subplan 3: Training Infrastructure (RLVR) ✓ COMPLETED

ART-based RL training with rhythm-first metrics, strict Judge calibration, and curriculum learning.

### Goals
- ✅ Replace ad-hoc sessions with structured RL rollouts
- ✅ Define verifiable reward function with rhythm-first focus
- ✅ Train Composer agent with curriculum learning (rhythm → harmony → full)
- ✅ Track metrics: reward progression, 7 verifiable objectives, Judge scores

### Key Tasks
- [x] Create RLVR-specific prompts with contrastive examples
  - `prompts/composer_rlvr.md` - GOOD vs BAD JamJSON examples
  - `prompts/judge_strict.md` - Strict thresholds from Gen 0
- [x] Implement rhythm-first metrics (rlvr/metrics.py)
  - Upbeat syncopation (>60% target)
  - 7th chord usage (>75% target)
  - Trumpet activation (≥50% target)
  - Space density (≥50% target)
  - Plus 3 baseline metrics (consonance, groove, density regularity)
- [x] Implement reward function with curriculum (rlvr/reward.py)
  - Phase A: Rhythm focus (syncopation + groove = 60% weight)
  - Phase B: Add harmony metrics
  - Phase C: Anneal Judge score weight from 0.10 → 0.30
  - Exploration bonuses for first-time achievements
  - Penalty hooks for violations (silent trumpet, no 7ths, etc.)
- [x] Build ART training loop (rlvr/loop.py)
  - Rollout function following 2048.py pattern
  - Early stopping (no Judge improvement for 3 steps)
  - Mid-course correction check (Judge < 6.0 at step 10)
  - Checkpoint management with best-so-far tracking
  - MIDI artifact export per rollout
- [x] Add Weave logging throughout
  - Per-rollout: metrics, reward breakdown, Judge output, MIDI
  - Per-checkpoint: trend charts, curriculum phase, flags
- [x] Create smoke test and verify dry-run
  - 3 steps, 2 rollouts per step
  - All components integrate correctly
  - MIDI artifacts exported successfully

### Deliverables
- `prompts/composer_rlvr.md` - Enhanced prompt with contrastive examples
- `prompts/judge_strict.md` - Strict Judge calibration from day 1
- `rlvr/metrics.py` - 7 verifiable metrics (4 new + 3 baseline)
- `rlvr/reward.py` - Weighted reward with curriculum/annealing
- `rlvr/loop.py` - ART training loop with early stopping
- `rlvr/smoke_test.py` - Verification test (dry-run + optional LLM)
- `artifacts/rlvr_checkpoints/` - MIDI outputs per step

### Results
- ✅ Smoke test passed: 3 steps, 2 rollouts per step
- ✅ Dry-run mode works without WANDBAPIKEY
- ✅ MIDI artifacts exported correctly
- ✅ Curriculum phases advance properly
- ✅ Reward function provides real gradients
- ✅ Early stopping and mid-course correction logic implemented

### Usage
```bash
# Dry-run test (no LLM, no API key needed)
uv run python -m rlvr.smoke_test

# Full training (20 steps, 8 rollouts per step)
uv run python -m rlvr.loop --steps 20 --rollouts 8

# Short LLM training (requires WANDBAPIKEY)
uv run python -m rlvr.loop --steps 5 --rollouts 4
```

### Next Steps
- Run longer RLVR training (50+ steps with --use-llm)
- Compare RLVR vs GEPA outputs (Subplan 5: Evaluation)
- Analyze which training method produces better jazz

---

## Subplan 4: Training Infrastructure (GEPA) ✓ COMPLETED

Genetic-Pareto reflective prompt evolution for multi-objective optimization.

### Goals
- Evolve Composer prompts over generations using multi-objective optimization
- Use Pareto optimization for 6 verifiable objectives (consonance, groove, motif, interplay, density, Judge score)
- Archive elite prompts with full artifacts (MIDI, metrics, memory)

### Key Tasks
- [x] Implement GEPA prompt evolution logic
  - Initial prompt population with gene knobs (numeric + textual)
  - Fitness evaluation (6D objective vector)
  - Pareto selection with non-dominated sorting and crowding distance
  - Reflective (Judge-guided) + programmatic mutation operators
- [x] Create population management system
  - Prompt variants stored in gepa/population/XXXX/
  - Gene knobs (chord_density, motif_reuse_weight, etc.)
  - Archive of elites with all artifacts
- [x] Implement 6 verifiable objective functions
  - Consonance: % notes in key scale
  - Groove alignment: bass-drum correlation
  - Motif coherence: n-gram repetition/variation
  - Interplay: call-response event count
  - Density regularity: note count variance
  - Judge score: 0-10 from Judge agent
- [x] Create GEPA loop runner with Weave logging
  - CLI with --dry-run and --use-llm modes
  - Uses only WANDBAPIKEY (following 2048.py pattern)
  - Logs per-individual and per-generation metrics
- [x] Verify with 3-generation smoke test
  - Pareto fronts computed successfully
  - Elite archive created with MIDI + metrics + memory
  - Reproducible with --seed

### Deliverables
- `gepa/` - Complete GEPA implementation
- `gepa/population.py` - Population and individual management
- `gepa/evaluate.py` - 6D objective vector computation
- `gepa/pareto.py` - Non-dominated sorting, crowding distance, elite archiving
- `gepa/mutate.py` - Reflective (Judge) + programmatic mutations
- `gepa/loop.py` - Main GEPA runner with Weave logging
- `gepa/genes_schema.yaml` - Gene knob definitions and ranges
- `gepa/smoke_test.py` - 3-generation verification test
- `artifacts/elites/` - Archive of elite individuals with full artifacts

### Results
- ✅ Smoke test passed: 3 generations, population size 4
- ✅ Pareto fronts computed successfully
- ✅ 9 elites archived with composer.md, genes.yaml, metrics.json, jam.mid, memory.json
- ✅ Weave logging functional
- ✅ Reproducible evolution with --seed

### Next Steps
- Subplan 3 (RLVR) for scalar-reward comparison
- Longer GEPA runs (50+ generations) with --use-llm
- Comparative analysis: GEPA vs RLVR performance

---

## Subplan 5: Evaluation & Analysis

Build tools for assessing musical quality and agent behavior.

### Goals
- Automated metrics beyond Judge feedback
- Human evaluation framework
- Visualization of improvement over time

### Key Tasks
- [ ] Implement automated music analysis
  - Pitch diversity (entropy)
  - Rhythmic complexity
  - Harmonic stability (consonance/dissonance ratios)
  - Instrument interaction (call-response detection)
- [ ] Create human evaluation interface
  - Blind A/B tests (early vs. late sessions)
  - Likert scale questionnaires
  - Preference rankings
- [ ] Build visualization dashboard
  - Reward curves over sessions
  - Musical feature trends
  - Weave integration for interactive exploration
- [ ] Write analysis notebooks
  - Statistical comparisons
  - Qualitative insights
  - Example MIDI highlights

---

## Subplan 6: Polish & Extensions

Refinements and optional features for robustness and creativity.

### Potential Extensions
- [ ] Multi-genre support (swing, bebop, latin, fusion)
- [ ] Longer compositions (8, 16, 32 bars)
- [ ] Chord progression awareness (not just key)
- [ ] Dynamic tempo/style changes mid-session
- [ ] Audio rendering (MIDI → audio with soundfonts)
- [ ] Interactive demo (web UI for generating jams on demand)
- [ ] Model distillation (faster inference for real-time use)
- [ ] Publication-ready experiments and paper draft

---

## Notes

- **Ground Rules**: Keep `TODO.md` updated as work progresses. Check off tasks, add new ones as needed.
- **Environment**: Always use `uv` for dependency management and script execution.
- **Secrets**: Only use `WANDBAPIKEY` from environment (never hardcode).
- **References**:
  - GEPA paper: https://arxiv.org/abs/2507.19457
  - RLVR paper: https://arxiv.org/abs/2504.20571
  - ART library: https://github.com/openpipe/art
  - music21 docs: https://web.mit.edu/music21/doc/

---

**Current Status**: ✅ Subplan 1 (Core), Subplan 2 (Agents), Subplan 3 (RLVR), and Subplan 4 (GEPA) complete. Two training modes ready: GEPA (multi-objective genetic evolution) and RLVR (scalar-reward RL with curriculum). Ready for Subplan 5 (Evaluation & Comparison).
