# Baseline Notes

## 2024-11-29

### Opus Runs (3x)
| Run | Timestamp | Score |
|-----|-----------|-------|
| 1 | 131245 | 5.0 |
| **2** | **131327** | **5.5** |
| 3 | 131404 | 4.5 |

### RLVR Runs (Qwen3-14B, 3x)
| Run | Score |
|-----|-------|
| 1 | 4.5 |
| 2 | 4.0 |
| 3 | 3.0 |

### Summary
- Opus best: Run 2 (5.5)
- RLVR best: Run 1 (4.5)
- Opus outperforms RLVR on musicality with same prompt

---

## Reward Feature Analysis

### Feature: `peak_not_final`
Does the melody's highest note occur before the last note? (Resolution signal)

| Sample | Score | Peak Position | Peak Not Final |
|--------|-------|---------------|----------------|
| Moanin' | 9.0 | 60% | ✓ |
| So What | 9.0 | 8% | ✓ |
| Song for My Father | 9.0 | 17% | ✓ |
| Watermelon Man | 9.0 | 15% | ✓ |
| Cantina | 9.0 | 11% | ✓ |
| Opus 1 | 5.0 | 0% | ✓ |
| Opus 2 | 5.5 | 0% | ✓ |
| Opus 3 | 4.5 | 100% | ✗ |
| RLVR 1 | 4.5 | 86% | ✓ |
| RLVR 2 | 4.0 | 21% | ✓ |
| RLVR 3 | 3.0 | 100% | ✗ |

**Finding**: `peak_not_final=False` perfectly predicts the worst score in each group (Opus 3, RLVR 3).

### Feature: `descending_end`
Does the melody descend into the final note?

| Sample | Score | Descending End |
|--------|-------|----------------|
| Standards | 9.0 | 2/5 (mixed) |
| Opus 1 | 5.0 | ✓ |
| Opus 2 | 5.5 | ✓ |
| Opus 3 | 4.5 | ✗ |
| RLVR 1 | 4.5 | ✓ |
| RLVR 2 | 4.0 | ✓ |
| RLVR 3 | 3.0 | ✗ |

**Finding**: Weaker signal. Standards are mixed. But worst outputs (Opus 3, RLVR 3) both lack it.

### Feature: `peak_zone` (addendum)
Where does the peak occur? Early (0-33%), Middle (33-66%), Late (66-100%)?

| Zone | Count | Avg Score |
|------|-------|-----------|
| EARLY | 8 | 7.1 |
| MIDDLE | 1 | 9.0 |
| LATE | 3 | 4.0 |

**Finding**: LATE is poison (avg 4.0). But EARLY vs MIDDLE not distinguishable with this sample size. Most standards are EARLY (8-21%). Lower weight than `peak_not_final`.

---

## Story Feature Analysis

Tested 6 hypotheses for "storiness" across all samples.

### Feature: `has_motif` / `repeated_2grams` ⭐ STRONG
Are there repeated interval patterns (call-and-response)?

| Sample | Score | 2-grams | 3-grams | Has Motif |
|--------|-------|---------|---------|-----------|
| Moanin' | 9.0 | 6 | 3 | ✓ |
| So What | 9.0 | 2 | 0 | ✓ |
| Song for My Father | 9.0 | 12 | 13 | ✓ |
| Watermelon Man | 9.0 | 3 | 0 | ✓ |
| Cantina | 9.0 | 26 | 30 | ✓ |
| Opus 1 | 5.0 | 0 | 0 | ✗ |
| Opus 2 | 5.5 | 0 | 0 | ✗ |
| Opus 3 | 4.5 | 0 | 0 | ✗ |
| RLVR 1 | 4.5 | 2 | 1 | ✓ |
| RLVR 2 | 4.0 | 3 | 2 | ✓ |
| RLVR 3 | 3.0 | 0 | 0 | ✗ |

**Finding**: Standards 100% have motifs, outputs 33%. Avg repeated 2-grams: 9.8 vs 0.8 (12x gap). This captures "call and response" — melody states something, then returns to it.

### Feature: `journey_range` ⭐ STRONG
Pitch range of the melody (max - min in semitones).

| Group | Avg Range |
|-------|-----------|
| Standards | 22.2 |
| Outputs | 9.2 |

**Finding**: 2.4x gap. Standards travel somewhere; outputs stay in a narrow band.

### Feature: `rest_ratio` ⭐ MODERATE (inverted)
Percentage of time spent in silence between notes.

| Group | Avg Rest Ratio |
|-------|----------------|
| Standards | 12.9% |
| Outputs | 33.6% |

**Finding**: Outputs have MORE rest, not less. This is the sparseness problem — few notes with big gaps. Standards are denser.

### Features with NO SIGNAL
- **energy_arc**: 40% vs 33% (noise)
- **opening_strength**: Similar across both groups
- **closing_weight**: Noisy, outliers (Song for My Father = 11x avg)

### Summary: High-Signal Features for Reward

| Feature | Standards | Outputs | Signal |
|---------|-----------|---------|--------|
| `peak_not_final` | 100% | 67% | Predicts worst scores |
| `has_motif` | 100% | 33% | Perfect separation |
| `repeated_2grams` | 9.8 | 0.8 | 12x gap |
| `journey_range` | 22.2 | 9.2 | 2.4x gap |
| `rest_ratio` | 12.9% | 33.6% | Inverted (lower = better) |

### Tonal Features — NO SIGNAL

Tested: key consistency, tonic gravity, resolution to tonic, V-I motion, tritones, chromatic approach resolution, strong beat chord tones, enclosures, leap-step resolution, ensemble consonance.

**Finding**: No separation. Both groups are equally diatonic and consonant (96-97% key fit, 80% consonance). Outputs actually score HIGHER on "textbook" metrics like strong-beat chord tones. Jazz standards break classical rules on purpose. Tonal correctness isn't the differentiator.

### Memorability / Jazziness Features ⭐ STRONG

| Feature | Standards | Outputs | Gap |
|---------|-----------|---------|-----|
| `has_rhythm_hook` | 100% | 33% | Repeated rhythm patterns |
| `rhythm_2grams` | 5.0 | 1.0 | 5x difference |
| `syncopation_ratio` | 71% | 46% | Standards swing more |
| `max_interval` | 13 | 5 | Bigger signature leaps |
| `interval_ratio` | 3.7 | 1.6 | ONE distinctive jump |
| `dur_cv` | 0.95 | 0.20 | 4.7x — mix long/short notes |

**Finding**: Memorability comes from:
1. **Rhythm hook** — repeated rhythm patterns (not just pitches)
2. **Duration variance** — mixing long and short notes (RLVR = 0.00, all same length)
3. **Interval signature** — one big memorable leap that defines the riff
4. **Syncopation** — pushing against the beat

### Deep Jazz Features ⭐ STRONG

| Feature | Standards | Outputs | Ratio |
|---------|-----------|---------|-------|
| `duration_contrast_rate` | 31% | 14% | 2.3x |
| `swing_pct` | 55% | 25% | 2.2x |
| `vel_std` | 9.3 | 4.5 | 2.1x |
| `vel_range` | 28 | 14 | 2.0x |
| `blue_ratio` | 26% | 15% | 1.7x |
| `collision_rate` | 26% | 39% | 0.7x (lower=better) |

**Key findings:**
1. **Duration contrast** — Standards mix long/short dramatically. RLVR = 0% (all same length)
2. **Swing pairs** — 55% vs 25% long-short pairs. RLVR plays straight
3. **Velocity variation** — RLVR has 0.0 std (every note same loudness = mechanical)
4. **Blue note resolution** — Standards resolve b3/b7 (8-40%). Outputs: 0% (accidental, not intentional)
5. **Collision rate** — Opus 3 (worst) has 100% collision with piano. Don't step on each other

**RLVR outputs are lifeless:** 0% duration contrast, 0 velocity variation, 0% swing, 0% blue resolution.

---

## Final Regression Analysis

### Individual Feature Correlations (sorted by |r|)

| Feature | r | R² |
|---------|---|-----|
| `melodic_entropy` | +0.756 | 0.572 |
| `total_register_span` | +0.722 | 0.521 |
| `pitch_range` | +0.677 | 0.458 |
| `rhythm_2grams` | +0.663 | 0.439 |
| `dur_cv` | +0.653 | 0.426 |
| `peak_not_late` | +0.650 | 0.423 |
| `duration_contrast` | +0.606 | 0.368 |
| `rest_ratio` | -0.604 | 0.365 |

### Exhaustive Search Results

| # Features | R² | Best Combo |
|------------|-----|------------|
| 1 | 0.572 | `melodic_entropy` |
| 2 | 0.823 | `rhythm_2grams + total_register_span` |
| **3** | **0.879** | **`pitch_range + rhythm_2grams + duration_contrast`** |
| 4 | 0.900 | `rhythm_2grams + avg_interval + dur_cv + melodic_entropy` |
| 5 | 0.935 | `rhythm_2grams + avg_interval + interval_ratio + duration_contrast + melodic_entropy` |

### Recommended Reward Function

**3 features, R² = 0.879, MAE = 0.64:**

```python
reward = f(pitch_range, rhythm_2grams, duration_contrast)
```

- `pitch_range`: Melodic travel (semitones)
- `rhythm_2grams`: Repeated rhythm patterns (motif/hook)
- `duration_contrast`: Mix of long/short notes (% with >2x ratio)

### Predictions vs Actual

| Sample | Actual | Predicted | Error |
|--------|--------|-----------|-------|
| moanin | 9.0 | 8.03 | +0.97 |
| sowhat | 9.0 | 9.10 | -0.10 |
| songformyfather | 9.0 | 10.21 | -1.21 |
| watermelon | 9.0 | 7.17 | +1.83 |
| cantina | 9.0 | 8.91 | +0.09 |
| opus_1 | 5.0 | 5.47 | -0.47 |
| opus_2 | 5.5 | 5.80 | -0.30 |
| opus_3 | 4.5 | 4.79 | -0.29 |
| rlvr_1 | 4.5 | 3.90 | +0.60 |
| rlvr_2 | 4.0 | 4.90 | -0.90 |
| rlvr_3 | 3.0 | 3.23 | -0.23 |

---

## Final 6-Feature Reward Model

### Features (one per category)

| # | Feature | Category | r_score |
|---|---------|----------|---------|
| 1 | `melodic_entropy` | Complexity | +0.756 |
| 2 | `dur_cv` | Note Length | +0.653 |
| 3 | `sax_arpeggio_runs` | Chord | +0.397 |
| 4 | `peak_not_late` | Structure | +0.650 |
| 5 | `blue_ratio` | Jazz Identity | +0.495 |
| 6 | `rhythm_2grams` | Rhythm | +0.650 |

### Model Performance

**R² = 0.852** (85.2% variance explained)

Comparison:
- 5-feature model: R² = 0.837
- **6-feature model: R² = 0.852** ← final model
- 5 + syncopation_ratio: R² = 0.754 (hurts — accidental syncopation ≠ groove)

### What Each Feature Captures

1. **melodic_entropy** — Is the melody unpredictable/interesting?
2. **dur_cv** — Does it mix long and short notes?
3. **sax_arpeggio_runs** — Does it deliberately outline harmony?
4. **peak_not_late** — Does it resolve (not end on climax)?
5. **blue_ratio** — Does it use jazz DNA (b3, b5, b7)?
6. **rhythm_2grams** — Does it have repeated rhythm patterns (groove/hook)?

### Reward Formula

```python
reward = z(melodic_entropy) + z(dur_cv) + z(sax_arpeggio_runs) + z(peak_not_late) + z(blue_ratio) + z(rhythm_2grams)
```

### Validation: Reward vs Human Scores

| Sample | Human | Reward |
|--------|-------|--------|
| moanin | 9.0 | +3.77 |
| cantina | 9.0 | +3.59 |
| sowhat | 9.0 | +1.58 |
| opus_2 | 5.5 | -0.30 |
| opus_3 | 4.5 | -1.40 |
| rlvr_2 | 4.0 | -2.11 |
| rlvr_1 | 4.5 | -5.55 |
| rlvr_3 | 3.0 | -7.08 |

Standards → positive. Outputs → negative. Worst → most negative.

---

## Weight Strategy

### Why Equal Weights (z-sum)?

- **OLS with n=11 overfits.** 6 parameters, 11 samples. Learned weights are noisy.
- **Z-sum (2 params: slope + intercept) is more stable.** R² = 0.837 vs OLS R² = 0.822.
- **Features are orthogonal.** When features don't conflict, weights matter less.
- **All features point the same direction.** Good melodies are high on all. Bad melodies are low on all.

### Don't Learn Weights During Training

Continuous weight learning risks:
1. Small batches → noisy estimates → thrashing
2. Negative weights by chance → gradient reversal
3. Distribution shift → weights become stale

### Recommended Approach

1. **Train with equal z-sum.** Stable gradient signal.
2. **After training, evaluate.** Get human scores on outputs.
3. **If systematic bias exists** (model exploits one feature), manually adjust.
4. **Retrain.** One iteration, human in the loop.

### If Adaptive Weights Are Needed

```python
# Every 1000 steps, after 50+ scored rollouts:
new_weights = fit_ols(rollouts)
new_weights = np.clip(new_weights, 0.2, 3.0)  # bound relative to equal
weights = 0.9 * weights + 0.1 * new_weights   # slow EMA
```

### Bottom Line

The 16% unexplained variance isn't in the weights — it's in **missing features** (rhythm, coherence). Fix that by adding better features, not by tuning weights on existing ones.
