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

## Subplan 3: Training Infrastructure (RLVR)

Integrate ART (Automated Reinforcement Training) for RLVR-based improvement.

### Goals
- Replace ad-hoc sessions with structured RL rollouts
- Define verifiable reward function based on Judge scores
- Train Composer agent to improve over 50 sessions
- Track metrics: reward progression, musical quality trends

### Key Tasks
- [ ] Define reward function from Judge outputs
  - Map qualitative feedback to scalar rewards
  - Weight different criteria (harmony, rhythm, melody, balance)
- [ ] Integrate ART library
  - Define rollout function (Composer generates → Judge evaluates → reward)
  - Set up training loop with ART TrainableModel
  - Use W&B Serverless Backend for GPU autoscaling
- [ ] Create evaluation scripts
  - Compare session 1 vs. session 50
  - Plot reward curves
  - Generate before/after MIDI comparisons
- [ ] Document RLVR configuration and hyperparameters

### Open Questions
- What's the optimal reward shaping?
- How many rollouts per training step?
- What learning rate works best?

---

## Subplan 4: Training Infrastructure (GEPA)

Add alternative training mode using Genetic-Pareto reflective prompt evolution.

### Goals
- Evolve Composer prompts over generations
- Use Pareto optimization for multi-objective criteria (harmony, rhythm, melody, balance)
- Compare GEPA vs. RLVR performance

### Key Tasks
- [ ] Implement GEPA prompt evolution logic
  - Initial prompt population
  - Fitness evaluation (Judge scores as objectives)
  - Selection, crossover, mutation for prompts
  - Pareto front tracking
- [ ] Create interchangeable training mode switch
  - CLI flag: `--training-mode rlvr` or `--training-mode gepa`
  - Shared interfaces for both modes
- [ ] Run comparative experiments
  - RLVR baseline (50 sessions)
  - GEPA variant (50 generations)
  - Analyze which produces better music
- [ ] Document GEPA configuration and hyperparameters

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

**Current Status**: ✅ Subplan 1 complete. Ready to begin Subplan 2 (Agents & Judge).
