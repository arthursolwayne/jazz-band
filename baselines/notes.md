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

---

## Multi-Instrument Feature Analysis (2024-11-30)

Extended reward function to bass, piano, drums, and ensemble interaction.

### Bass Features

| Feature | r | Category | Definition |
|---------|---|----------|------------|
| **non_chromatic_ratio** | +0.846 | Melodic | % intervals != 1 semitone |
| **ioi_swing** | +0.697 | Rhythm | CV of inter-onset intervals |
| **direction_changes** | +0.552 | Melodic | % melodic direction changes |
| **bass_register_ratio** | +0.423 | Pitch | % notes in MIDI 28-55 |

**Key finding**: Machines use 40-100% chromatic half-steps. Standards use 5ths, octaves, varied intervals (non_chromatic ~95%).

### Piano Features

| Feature | r | Category | Definition |
|---------|---|----------|------------|
| **gap_ratio** | -0.850 | Rhythm | % time in silence (invert) |
| **attack_variance** | +0.670 | Rhythm | CV of attack timing |
| **velocity_variance** | +0.618 | Dynamics | StdDev of velocities |
| **voicing_richness** | -0.466 | Voicing | Avg notes per chord (penalty >3) |

**Key finding**: attack_variance = 0.0 for ALL model outputs. Standards avg 0.58. Machines are perfectly robotic.

### Drum Features

| Feature | r | Category | Definition |
|---------|---|----------|------------|
| **kick_sparseness** | +0.964 | Sparseness | exp(-kicks_per_sec) |
| **ghost_note_ratio** | +0.600 | Dynamics | % snares with velocity < 80 |
| **ioi_entropy** | +0.490 | Timing | Entropy of quantized IOIs |
| **velocity_variance** | +0.448 | Dynamics | StdDev of all drum velocities |

**Key finding**: Jazz standards have ZERO kick drums. LLM outputs play rock-style kick patterns. kick_sparseness has r=0.964 — strongest single predictor found.

### Ensemble Features

| Feature | r | Category | Definition |
|---------|---|----------|------------|
| **register_separation** | +0.574 | Register | Avg pitch distance sax↔bass |
| **drum_groove_alignment** | +0.517 | Rhythm | % melody on strong beats |
| **dynamic_coherence** | -0.693 | Dynamics | Correlation of velocity contours (INVERT) |
| **texture_density** | -0.615 | Texture | Avg simultaneous voices (INVERT) |

**Key finding**: dynamic_coherence is INVERTED. Real jazz ensembles are dynamically INDEPENDENT — instruments breathe separately. Model outputs are "too coordinated" (r=0.84 coherence vs 0.41 for standards).

### Correlation Summary

| Instrument | Best Feature | r | Combined R² |
|------------|--------------|---|-------------|
| Bass | non_chromatic_ratio | +0.85 | ~0.72 |
| Piano | gap_ratio | -0.85 | ~0.68 |
| Drums | kick_sparseness | +0.96 | ~0.93 |
| Ensemble | dynamic_coherence | -0.69 | 0.95 |

### Inverted Features (Lower = Better)

These features showed negative correlation — opposite to initial hypothesis:

| Feature | Expected | Actual | Explanation |
|---------|----------|--------|-------------|
| gap_ratio | More silence = sparse | Less silence = active | Good comping is engaged, not passive |
| dynamic_coherence | Move together | Move independently | Jazz = conversation, not unison |
| texture_density | Dense = rich | Sparse = clear | Standards are cleaner, less cluttered |
| voicing_richness | More notes = richer | Fewer notes = focused | 3-note voicings beat 5-note clusters |

### Implementation Files

- `src/jazz_band/reward_bass.py`
- `src/jazz_band/reward_piano.py`
- `src/jazz_band/reward_drums.py`
- `src/jazz_band/reward_ensemble.py`

---

## Piano Feature Statistical Analysis (2024-11-30)

Rigorous analysis following the sax methodology: individual correlations, exhaustive N-feature search with both OLS and equal-weighted z-sum, collinearity analysis, and model validation.

### 1. Individual Feature Correlations (sorted by |r|)

| Feature | r | R^2 | Signal |
|---------|---|-----|--------|
| `gap_ratio` | -0.853 | 0.728 | DOMINANT |
| `attack_variance` | +0.626 | 0.392 | Strong |
| `velocity_variance` | +0.618 | 0.382 | Strong |
| `voice_leading_smoothness` | -0.611 | 0.373 | Strong (inverted!) |
| `register_below_melody` | +0.339 | 0.115 | Moderate |
| `rootless_ratio` | +0.336 | 0.113 | Moderate |
| `note_density` | +0.299 | 0.089 | Weak |
| `voicing_richness` | -0.279 | 0.078 | Weak |
| `interval_variety` | +0.274 | 0.075 | Weak |
| `register_separation` | +0.246 | 0.061 | Weak |
| `rhythmic_pattern_score` | -0.209 | 0.044 | Noise |
| `avg_chord_spread` | +0.088 | 0.008 | Noise |
| `syncopation_score` | -0.059 | 0.004 | Noise |

**Key finding**: `gap_ratio` alone explains 72.8% of variance. Good piano comping is ACTIVE, not sparse.

### 2. Exhaustive N-Feature Search

#### OLS (learned weights)

| N | R^2 | Best Combination |
|---|-----|------------------|
| 1 | 0.728 | gap_ratio |
| 2 | 0.842 | avg_chord_spread, gap_ratio |
| 3 | 0.907 | avg_chord_spread, gap_ratio, register_separation |
| 4 | 0.969 | avg_chord_spread, gap_ratio, register_separation, register_below_melody |
| 5 | 0.979 | gap_ratio, register_separation, register_below_melody, interval_variety, velocity_variance |

#### Z-Sum (equal weights) - for actual reward function

| N | R^2 | Best Combination |
|---|-----|------------------|
| 1 | 0.728 | gap_ratio |
| 2 | 0.770 | gap_ratio, voice_leading_smoothness |
| 3 | 0.822 | voicing_richness, avg_chord_spread, gap_ratio |
| **4** | **0.897** | **avg_chord_spread, gap_ratio, register_separation, velocity_variance** |
| 5 | 0.851 | overfitting begins |

### 3. Selected Features (4-feature z-sum model)

| Feature | r | Direction | What it captures |
|---------|---|-----------|------------------|
| `avg_chord_spread` | +0.088 | higher=better | Open voicings |
| `gap_ratio` | -0.853 | lower=better | Active comping |
| `register_separation` | +0.246 | higher=better | Stay out of melody |
| `velocity_variance` | +0.618 | higher=better | Dynamic expression |

### 4. Collinearity Matrix (selected features)

|             | avg_chord | gap_ratio | register_sep | velocity_var |
|-------------|-----------|-----------|--------------|--------------|
| avg_chord   | --- | +0.28 | -0.27 | -0.31 |
| gap_ratio   | +0.28 | --- | -0.10 | **-0.84** |
| register_sep| -0.27 | -0.10 | --- | -0.27 |
| velocity_var| -0.31 | **-0.84** | -0.27 | --- |

**Warning**: gap_ratio and velocity_variance are highly correlated (r=-0.84). Both capture "liveliness" — but the combination still gives best R^2.

### 5. Predictions vs Actual

| Sample | Actual | Predicted | Error |
|--------|--------|-----------|-------|
| moanin | 9.0 | 8.99 | +0.01 |
| sowhat | 9.0 | 7.60 | +1.40 |
| songformyfather | 9.0 | 9.23 | -0.23 |
| watermelon | 9.0 | 9.75 | -0.75 |
| cantina | 9.0 | 8.22 | +0.78 |
| opus_1 | 5.0 | 6.16 | -1.16 |
| opus_2 | 5.5 | 5.08 | +0.42 |
| opus_3 | 4.5 | 4.70 | -0.20 |
| rlvr_1 | 4.5 | 4.65 | -0.15 |
| rlvr_2 | 4.0 | 3.19 | +0.81 |
| rlvr_3 | 3.0 | 3.93 | -0.93 |

### 6. Final Model Performance

- **R^2 = 0.897** (89.7% variance explained)
- **MAE = 0.62** points
- **Separation**: Standards avg ~8.6, Opus avg ~5.3, RLVR avg ~3.9

### 7. Reference Statistics (for z-score normalization)

```python
PIANO_REFERENCE_STATS = {
    'avg_chord_spread': {'mean': 9.246, 'std': 5.725, 'direction': 1},
    'gap_ratio': {'mean': 0.444, 'std': 0.217, 'direction': -1},
    'register_separation': {'mean': 7.050, 'std': 6.846, 'direction': 1},
    'velocity_variance': {'mean': 0.055, 'std': 0.095, 'direction': 1},
}
```

### 8. Key Insights

1. **gap_ratio is king**: Single feature explains 72.8%. LLM outputs have too much silence — good comping stays engaged.

2. **voice_leading_smoothness contradicts theory**: r=-0.611 (smoother = worse). Standards have MORE voice motion because they're actively moving through harmonies. LLM outputs stay static.

3. **syncopation_score shows NO signal**: r=-0.059. LLM outputs often have high syncopation scores because they land randomly, not because they groove.

4. **Equal weights work**: Z-sum (R^2=0.897) nearly matches OLS (R^2=0.969) with 4 features. No need for learned weights.

5. **avg_chord_spread has low individual r (+0.088) but adds value in combination**: It captures voicing quality orthogonal to timing features.

---

## Drum Feature Regression Analysis (2024-11-30)

### Sample Set (n=11)
- Standards (score=9.0): moanin, sowhat, songformyfather, watermelon, cantina
- Opus outputs (scores 4.5-5.5): 3 samples
- RLVR outputs (scores 3.0-4.5): 3 samples

### Individual Feature Correlations (sorted by |r|)

| Feature | r | R^2 |
|---------|-----|------|
| `kick_off_beat_ratio` | +0.959 | 0.920 |
| `kick_sparseness` | +0.882 | 0.777 |
| `snare_backbeat_ratio` | +0.622 | 0.386 |
| `ghost_note_ratio` | +0.606 | 0.367 |
| `velocity_variance` | +0.558 | 0.312 |
| `duration_variety` | +0.486 | 0.237 |
| `ioi_entropy` | +0.370 | 0.137 |
| `dynamics_range` | +0.359 | 0.129 |
| `snare_pattern_entropy` | -0.171 | 0.029 |
| `ioi_cv` | +0.160 | 0.026 |
| `unique_drum_pitches` | +0.155 | 0.024 |
| `ride_presence` | +0.000 | 0.000 |

**Key finding**: `kick_off_beat_ratio` is the strongest single predictor (r=0.959, R^2=0.920). Jazz standards have ZERO kick drums (ratio=1.0), while model outputs play rock-style on-beat kicks (ratio~0.5). This alone explains 92% of the variance!

### Exhaustive N-Feature Search

**Without collinearity filter:**
| # Features | R^2 | Best Combo |
|------------|-------|------------|
| 1 | 0.920 | `kick_off_beat_ratio` |
| 2 | 0.862 | `kick_off_beat_ratio + kick_sparseness` |
| 3 | 0.861 | `kick_off_beat_ratio + snare_backbeat_ratio + velocity_variance` |
| 4 | 0.886 | `kick_off_beat_ratio + snare_backbeat_ratio + velocity_variance + duration_variety` |
| 5 | 0.902 | `kick_off_beat_ratio + snare_backbeat_ratio + ghost_note_ratio + unique_drum_pitches + velocity_variance` |

**With collinearity filter (|r| < 0.7):**
| # Features | R^2 | Best Combo |
|------------|-------|------------|
| 1 | 0.920 | `kick_off_beat_ratio` |
| 2 | 0.764 | `kick_off_beat_ratio + snare_backbeat_ratio` |
| 3 | 0.861 | `kick_off_beat_ratio + snare_backbeat_ratio + velocity_variance` |
| **4** | **0.886** | **`kick_off_beat_ratio + snare_backbeat_ratio + velocity_variance + duration_variety`** |
| 5 | 0.869 | `kick_sparseness + snare_backbeat_ratio + velocity_variance + snare_pattern_entropy + unique_drum_pitches` |

### Equal-Weighted Z-Sum Model

**Best 4-feature combo (R^2 = 0.886, MAE = 0.62):**

```python
features = ['kick_off_beat_ratio', 'snare_backbeat_ratio', 'velocity_variance', 'duration_variety']
```

**Reference statistics (n=11):**

| Feature | Mean | Std | r |
|---------|------|-----|-----|
| `kick_off_beat_ratio` | 0.716 | 0.262 | +0.959 |
| `snare_backbeat_ratio` | 0.097 | 0.166 | +0.622 |
| `velocity_variance` | 13.78 | 10.14 | +0.558 |
| `duration_variety` | 2.18 | 0.83 | +0.486 |

### Predictions vs Actual

| Sample | Human Score | Predicted | Error |
|--------|-------------|-----------|-------|
| moanin | 9.0 | 8.86 | +0.14 |
| sowhat | 9.0 | 9.53 | -0.53 |
| songformyfather | 9.0 | 8.13 | +0.87 |
| watermelon | 9.0 | 8.51 | +0.49 |
| cantina | 9.0 | 8.80 | +0.20 |
| opus_1 | 5.0 | 5.02 | -0.02 |
| opus_2 | 5.5 | 5.54 | -0.04 |
| opus_3 | 4.5 | 5.48 | -0.98 |
| rlvr_1 | 4.5 | 2.79 | +1.71 |
| rlvr_2 | 4.0 | 5.08 | -1.08 |
| rlvr_3 | 3.0 | 3.77 | -0.77 |

### Collinearity Matrix (Selected Features)

| Feature | kick_off | snare_back | velocity | duration |
|---------|----------|------------|----------|----------|
| kick_off_beat_ratio | 1.000 | 0.636 | 0.544 | 0.498 |
| snare_backbeat_ratio | 0.636 | 1.000 | -0.024 | 0.020 |
| velocity_variance | 0.544 | -0.024 | 1.000 | 0.217 |
| duration_variety | 0.498 | 0.020 | 0.217 | 1.000 |

**All pairwise correlations < 0.7** — features capture orthogonal aspects of quality.

### Final Recommendation

**Use 4 features (R^2 = 0.886, MAE = 0.62):**

1. **kick_off_beat_ratio** (r=+0.959, Category: Sparseness)
   - Proportion of kicks off-beat. No kicks = 1.0
   - Standards: 1.0 (zero kicks), Outputs: ~0.5 (on-beat kicks)
   - **This is the strongest predictor across ALL instrument features**

2. **snare_backbeat_ratio** (r=+0.622, Category: Jazz Pattern)
   - Proportion of snares on backbeats (beats 2 & 4)
   - Standards: ~21% (varied placement), Outputs: 0% (no snare variation)

3. **velocity_variance** (r=+0.558, Category: Dynamics)
   - Standard deviation of drum velocities
   - Standards: 19.4 std, RLVR: often 0 (every hit same loudness)

4. **duration_variety** (r=+0.486, Category: Pattern)
   - Count of distinct note durations
   - Standards: 2.6 (mix short/long), Outputs: 1.8 (uniform)

**Key Insights:**

1. **kick_off_beat_ratio alone explains 92%** — Jazz standards have ZERO kicks
2. **kick_sparseness is collinear** (r=0.96) with kick_off_beat — pick one
3. **ghost_note_ratio and snare_backbeat_ratio are collinear** (r=0.83) — pick one
4. **ride_presence has zero variance** — all samples have no ride (excluded)

**Z-Sum Formula:**
```python
reward = z(kick_off_beat_ratio) + z(snare_backbeat_ratio) + z(velocity_variance) + z(duration_variety)
```

**Raw Feature Data:**

| Sample | kick_off | snare_back | velocity | duration | Score |
|--------|----------|------------|----------|----------|-------|
| moanin | 1.00 | 0.43 | 14.86 | 2 | 9.0 |
| sowhat | 1.00 | 0.23 | 23.61 | 3 | 9.0 |
| songformyfather | 1.00 | 0.42 | 6.28 | 2 | 9.0 |
| watermelon | 1.00 | 0.00 | 36.57 | 2 | 9.0 |
| cantina | 1.00 | 0.00 | 15.87 | 4 | 9.0 |
| opus_1 | 0.50 | 0.00 | 11.45 | 2 | 5.0 |
| opus_2 | 0.50 | 0.00 | 18.04 | 2 | 5.5 |
| opus_3 | 0.50 | 0.00 | 17.21 | 2 | 4.5 |
| rlvr_1 | 0.38 | 0.00 | 0.00 | 1 | 4.5 |
| rlvr_2 | 0.50 | 0.00 | 0.00 | 3 | 4.0 |
| rlvr_3 | 0.50 | 0.00 | 7.64 | 1 | 3.0 |

---

## Ensemble Feature Regression Analysis (2024-11-30)

### Individual Feature Correlations (sorted by |r|)

| Feature | r | R^2 |
|---------|-----|------|
| `dynamic_coherence` | -0.737 | 0.544 |
| `texture_density` | -0.702 | 0.493 |
| `onset_density_balance` | -0.702 | 0.492 |
| `phrase_alignment` | -0.701 | 0.491 |
| `harmonic_consonance` | +0.601 | 0.362 |
| `call_response` | -0.519 | 0.269 |
| `register_separation` | +0.517 | 0.267 |
| `drum_groove_alignment` | +0.422 | 0.178 |
| `velocity_variance_ratio` | -0.270 | 0.073 |
| `collision_rate` | -0.229 | 0.052 |
| `chord_alignment` | -0.052 | 0.003 |
| `rhythm_independence` | +0.042 | 0.002 |

**Key finding**: `dynamic_coherence` is the single strongest predictor (r=-0.737). Standards have LOWER coherence — instruments are dynamically independent, not moving in lockstep.

### Exhaustive N-Feature Search

| # Features | R^2 | Best Combo |
|------------|-------|------------|
| 1 | 0.544 | `dynamic_coherence` |
| 2 | 0.864 | `dynamic_coherence + texture_density` |
| **3** | **0.927** | **`dynamic_coherence + call_response + texture_density`** |
| **4** | **0.955** | **`collision_rate + phrase_alignment + texture_density + harmonic_consonance`** |
| 5 | 0.983 | `rhythm_independence + phrase_alignment + velocity_variance_ratio + texture_density + harmonic_consonance` |

### Equal-Weighted Z-Sum Model

**Best 4-feature combo (R^2 = 0.934, MAE = 0.44):**

```python
features = ['collision_rate', 'phrase_alignment', 'texture_density', 'harmonic_consonance']
directions = {
    'collision_rate': -1,      # Lower = better
    'phrase_alignment': -1,    # Lower = better
    'texture_density': -1,     # Lower = better
    'harmonic_consonance': +1, # Higher = better
}
```

**Reference statistics (n=11):**

| Feature | Mean | Std |
|---------|------|-----|
| `collision_rate` | 0.389 | 0.268 |
| `phrase_alignment` | 0.466 | 0.320 |
| `texture_density` | 0.531 | 0.369 |
| `harmonic_consonance` | 0.763 | 0.111 |

### Predictions vs Actual

| Sample | Human Score | Predicted | Error |
|--------|-------------|-----------|-------|
| moanin | 9.0 | 9.12 | -0.12 |
| sowhat | 9.0 | 8.48 | +0.52 |
| songformyfather | 9.0 | 10.24 | -1.24 |
| watermelon | 9.0 | 8.77 | +0.23 |
| cantina | 9.0 | 7.81 | +1.19 |
| opus_1 | 5.0 | 5.01 | -0.01 |
| opus_2 | 5.5 | 5.04 | +0.46 |
| opus_3 | 4.5 | 4.59 | -0.09 |
| rlvr_1 | 4.5 | 4.47 | +0.03 |
| rlvr_2 | 4.0 | 4.56 | -0.56 |
| rlvr_3 | 3.0 | 3.42 | -0.42 |

### Collinearity Matrix (Selected Features)

| Feature | collision | phrase | texture | harmonic |
|---------|-----------|--------|---------|----------|
| collision | 1.000 | 0.042 | 0.123 | 0.345 |
| phrase | 0.042 | 1.000 | 0.258 | -0.418 |
| texture | 0.123 | 0.258 | 1.000 | -0.173 |
| harmonic | 0.345 | -0.418 | -0.173 | 1.000 |

**Low collinearity** — features capture orthogonal aspects of quality.

### Final Recommendation

**Use 4 features (R^2 = 0.934):**

1. **collision_rate** (lower=better, Category: collision)
   - % sax notes colliding with piano at same pitch class
   - Standards: ~0.35, Outputs: ~0.45

2. **phrase_alignment** (lower=better, Category: structure)
   - How rigidly phrases align with bar lines
   - Standards: ~0.25, Outputs: ~0.75

3. **texture_density** (lower=better, Category: texture)
   - Average simultaneous voices
   - Standards: ~0.23, Outputs: ~0.72

4. **harmonic_consonance** (higher=better, Category: harmony)
   - % consonant intervals between melody and accompaniment
   - Standards: ~0.84, Outputs: ~0.70

**Why these 4:**
- Highest combined R^2 (0.955 OLS, 0.934 z-sum)
- Low collinearity (max |r| = 0.42 between features)
- Category coverage: collision, structure, texture, harmony
- Three inversions confirmed: less collision, less rigid, sparser = better

---

## Final Combined Model Backtest (2024-11-30)

### Sample Set (n=11)

**Standards (score=9.0):**
- reference_riffs/moanin_jazzband.mid
- reference_riffs/sowhat_jazzband.mid
- reference_riffs/songformyfather_jazzband.mid
- reference_riffs/watermelon_jazzband.mid
- reference_riffs/cantina_jazzband.mid

**Opus outputs:**
- baselines/opus/20251129_131245 (5.0)
- baselines/opus/20251129_131327 (5.5)
- baselines/opus/20251129_131404 (4.5)

**RLVR outputs (composer-001_20251129_202149):**
- step_000/rollout_000 (4.5)
- step_000/rollout_001 (4.0)
- step_000/rollout_002 (3.0)

### Individual R² Results

| Instrument | Expected | Actual | Features |
|------------|----------|--------|----------|
| Sax | 0.85 | 0.870 | 6 features (melodic_entropy, dur_cv, etc.) |
| Bass | 0.76 | 0.728 | 2 features (ioi_swing, non_chromatic_ratio) |
| Piano | 0.90 | 0.848 | 4 features (gap_ratio, velocity_variance, etc.) |
| Drums | 0.89 | 0.886 | 4 features (kick_off_beat_ratio, etc.) |
| Ensemble | 0.93 | 0.936 | 4 features (collision_rate, phrase_alignment, etc.) |

### Combined Model

**Equal-weight z-sum of all 5 instruments: R² = 0.964**

| Sample | Human Score | Combined Reward |
|--------|-------------|-----------------|
| moanin | 9.0 | **+10.34** |
| sowhat | 9.0 | **+8.02** |
| songformyfather | 9.0 | **+10.85** |
| watermelon | 9.0 | **+10.87** |
| cantina | 9.0 | **+7.88** |
| opus_1 | 5.0 | -3.40 |
| opus_2 | 5.5 | -1.38 |
| opus_3 | 4.5 | -3.75 |
| rlvr_1 | 4.5 | -5.24 |
| rlvr_2 | 4.0 | -3.81 |
| rlvr_3 | 3.0 | **-6.12** |

**Separation:** Standards avg = +9.6, Outputs avg = -3.9 (13.5 point gap)

### Raw Values (for reference)

| Sample | Score | Sax | Bass | Piano | Drums | Ensemble |
|--------|-------|-----|------|-------|-------|----------|
| moanin | 9.0 | +3.77 | +2.17 | 0.77 | +2.97 | 0.66 |
| sowhat | 9.0 | +1.58 | +1.31 | 0.70 | +3.81 | 0.62 |
| songformyfather | 9.0 | +5.62 | +1.68 | 0.78 | +2.05 | 0.72 |
| watermelon | 9.0 | +3.86 | +3.04 | 0.80 | +2.53 | 0.64 |
| cantina | 9.0 | +3.59 | +0.09 | 0.73 | +2.89 | 0.58 |
| opus_1 | 5.0 | -1.97 | -0.22 | 0.32 | -1.86 | 0.33 |
| opus_2 | 5.5 | -0.30 | -0.49 | 0.29 | -1.21 | 0.33 |
| opus_3 | 4.5 | -1.40 | -1.64 | 0.28 | -1.29 | 0.30 |
| rlvr_1 | 4.5 | -1.25 | -0.25 | 0.56 | -4.67 | 0.37 |
| rlvr_2 | 4.0 | -1.79 | -0.78 | 0.25 | -1.79 | 0.30 |
| rlvr_3 | 3.0 | -1.98 | -1.22 | 0.26 | -3.43 | 0.25 |

### Gates (per-instrument)

| Instrument | Gate | Penalty | Triggers When |
|------------|------|---------|---------------|
| Sax | `unique_durations < 2` | 50% | Monotone rhythm |
| Sax | `not has_rests` | 50% | No phrasing |
| Bass | `not has_direction_variety` | 50% | Monotonic (all up/down) |
| Ensemble | `not duration_on_target` | 20% | Not 4 bars (tempo-aware) |

### Tempo-Aware Duration Gate

The ensemble duration gate is now tempo-aware:
- Reads tempo from MIDI metadata (`get_tempo_changes()`)
- Calculates bar count: `duration / (4 * 60/tempo)`
- Passes if within ±0.5 bars of target (4 bars)

Prompt updated to require `initial_tempo=160` in PrettyMIDI constructor.

### Key Findings

1. **Combined R² = 0.964** vs sax-only R² = 0.870 (+11% improvement)
2. **Drums strongest separator**: RLVR samples have vel_var=0 (robotic), drums=-4.67
3. **Piano most predictive single instrument**: R²=0.848
4. **Ensemble captures interaction**: Standards more dynamically independent (lower coherence)
5. **Bass direction gate**: Prevents monotonic ascending/descending basslines

---

## TODO: Integration (pending)

### Reward Output Format

Current state:
- Sax: sigmoid → [0.3, 1.0] ✓
- Piano: sigmoid → [0.3, 1.0] ✓
- Ensemble: sigmoid → [0, 1] ✓
- Bass: **raw z-sum** (needs fix)
- Drums: **raw z-sum** (needs fix)

**Decision: Option B**
1. All instruments return raw z-sum (no per-instrument sigmoid)
2. Sum all 5 raw z-sums
3. Apply ONE sigmoid at the end → [0.3, 1.0]
4. Apply gates as multipliers

**Need to verify:** R² still holds after final sigmoid transform.

### Files to update for integration:
- `src/jazz_band/reward_bass.py` - remove sigmoid, return raw z-sum
- `src/jazz_band/reward_piano.py` - remove sigmoid, return raw z-sum
- `src/jazz_band/reward_drums.py` - already returns raw z-sum ✓
- `src/jazz_band/reward_ensemble.py` - remove sigmoid, return raw z-sum
- `src/jazz_band/symbol_engine.py` - remove sigmoid from sax, add combined reward function
- Create `compute_combined_reward()` that sums all 5 + applies final sigmoid + gates

---

## GEPA Dynamics Comparison (2024-12-01)

### Runs Compared

| Run | Config | Generations |
|-----|--------|-------------|
| `gepa_20251130_171422` | OLD: no acceptance gating, no z-clamp, old baselines | 30 |
| `gepa_20251130_220038` | NEW: acceptance gating + z-clamp (±3) + recalibrated baselines | 30 |

### Trajectory Stats (gen 0-29)

| Metric | OLD RUN | NEW RUN |
|--------|---------|---------|
| Early reward (gen 0-4) | +0.13 | +0.48 |
| Late reward (gen 25-29) | +0.15 | +0.42 |
| Δ reward | +0.01 | **-0.06** |
| Early valid % | 62% | 96% |
| Late valid % | 58% | 90% |

**Key finding**: New run maintains higher validity and reward, but reward drifted DOWN slightly. Acceptance gating prevents collapse but doesn't push upward.

### Listening Test Results

Played 3 samples from each run: best by score, best by balance, random.

| Run | Sample | Reward | Balance | Verdict |
|-----|--------|--------|---------|---------|
| OLD | gen_28/ind_010 (best score) | 0.84 | drums=+14.24 | Exploit. Drums spiked. |
| OLD | gen_19/ind_015 (best balance) | 0.24 | spread=0.26 | **Good! Bass+sax complemented well.** |
| OLD | gen_05/ind_030 (random) | 0.40 | bass=-0.19 | Bass too high (wrong register). |
| NEW | gen_00/ind_011 (best score) | 0.95 | sax=+11.71 | **Terrible. No jazz. Musically empty.** |
| NEW | gen_03/ind_024 (best balance) | 0.50 | spread=0.21 | **Best one. Very balanced. Unique story. Better than any Opus run. Cohesive.** |
| NEW | gen_23/ind_013 (random) | 0.49 | sax=+0.97 | Bad. Super random. |

### Key Insight

**Balance (low spread across instrument z-sums) is a better quality proxy than raw reward.**

The reward function produces musically coherent output when no single instrument dominates. High scores from spiking one instrument (sax=+11.71) sound terrible. Balanced scores (~0.5 with spread<0.3) sound like real jazz.

### Best Output Found

**gen_03/ind_024 from NEW run** (`gepa_20251130_220038`)
- Reward: 0.504
- Spread: 0.21 (lowest)
- sax=-0.05, bass=-0.02, piano=-0.07, drums=+0.14
- User verdict: "Best one. Very balanced. Unique, there's a bit of a story. Better than any Opus run. Cohesive."

### Implication

Consider adding a **balance penalty** to the reward function — penalize high spread between instrument z-sums. Or use balance as a selection criterion in GEPA (Pareto front: reward vs balance).

### Extended Listening Test (balance metric variations)

Tested multiple balance metrics on NEW run. All metrics converged on the same winner (gen_03/ind_024):
- spread_4 (range of 4 instruments)
- spread_5 (range including ensemble)
- std_4 (stddev of 4 instruments)
- std_5 (stddev including ensemble)
- pareto (reward>0.45, then lowest spread)

Listened to top 5 most balanced from NEW run:

| Rank | Sample | Spread | Verdict |
|------|--------|--------|---------|
| 1 | gen_03/ind_024 | 0.21 | **Winner. Cohesive, story, better than Opus.** |
| 2 | gen_29/ind_020 | 0.42 | Repetitive, but unique high pitch |
| 3 | gen_23/ind_030 | 0.47 | Terribly out of tune (consonance=0.43) |
| 4 | gen_20/ind_006 | 0.47 | Similar to #3, not great |

Tried filtering by consonance>0.6:

| Sample | Spread | Consonance | Verdict |
|--------|--------|------------|---------|
| gen_22/ind_020 | 0.51 | 0.61 | Not jazz, out of tune, but resolved |
| gen_07/ind_023 | 0.52 | 0.71 | Potential in sax, everything else bland |

### OLD Run Balanced Comparison

| Rank | Sample | Spread | Verdict |
|------|--------|--------|---------|
| 1 | gen_19/ind_015 | 0.27 | Good bass, complemented sax well |
| 2 | gen_24/ind_018 | 0.38 | Piano made ears bleed |
| 3 | gen_08/ind_022 | 0.40 | Decent sax, less impressive after hearing winner |

### Key Finding: Spread Threshold

**spread < 0.3 is the quality threshold.**

| Spread Range | Quality |
|--------------|---------|
| < 0.3 | Good (cohesive, musical) |
| 0.3 - 0.4 | Okay (some good elements) |
| > 0.4 | Bad (dissonant, bland, or exploity) |

NEW run's best balanced (spread=0.21) beats OLD run's best balanced (spread=0.27). Recalibrated baselines + z-clamp produce better quality even without reward climbing over generations.

### Fine-Grained Feature Analysis

Detailed breakdown of key samples:

#### NEW Winner (gen_03/ind_024) - "Cohesive, story, better than Opus"

| Instrument | z-sum | Key Features |
|------------|-------|--------------|
| SAX | -0.05 | blue_ratio=+1.23 (good), peak_not_late=+0.43, but melodic_entropy=-0.99, dur_cv=-0.30 |
| BASS | -0.02 | non_chromatic_ratio=+0.23 (varied intervals), ioi_swing=-0.25 |
| PIANO | -0.07 | avg_chord_spread=+1.41 (open voicings), but gap_ratio=-0.39, velocity_variance=-0.23 |
| DRUMS | +0.14 | duration_variety=+1.33 (good), kick_off_beat=+0.24, but velocity_variance=-1.07 |
| ENSEMBLE | +0.09 | phrase_alignment=+0.82, collision_rate=-0.11, harmonic_consonance=-0.18 |

**Why it works**: No extreme z-scores. Blue notes present. Open piano voicings. Drum duration variety. Nothing broken.

#### OLD #1 (gen_19/ind_015) - "Good bass, complemented sax"

| Instrument | z-sum | Key Features |
|------------|-------|--------------|
| SAX | -1.24 | peak_not_late=-1.63 (bad ending), blue_ratio=-0.92, variety_gate=0.25 (penalized) |
| BASS | -1.07 | non_chromatic_ratio=-0.26, ioi_swing=-0.81 |
| PIANO | -1.27 | variety_gate=1.0 (good), but gap_ratio=-0.72 |
| DRUMS | -1.33 | snare_backbeat=+1.42 (good!), but kick_off_beat=-0.83, duration_variety=-1.42 |
| ENSEMBLE | -1.99 | collision_rate=+1.45 (no collisions!), but phrase_alignment=-1.67, harmonic_consonance=-1.40 |

**Why bass sounded good**: collision_rate=0.0 (bass never stepped on other instruments). But low overall scores from old baselines.

#### NEW Exploit (gen_00/ind_011) - "Terrible, no jazz"

| Instrument | z-sum | Key Features |
|------------|-------|--------------|
| SAX | **+11.71** | melodic_entropy=+3.00 (CLAMPED), dur_cv=+3.00 (CLAMPED), rhythm_2grams=+3.00 (CLAMPED) |
| BASS | +2.61 | non_chromatic_ratio=+1.98 |
| PIANO | +0.78 | register_separation=+2.74 |
| DRUMS | +0.62 | velocity_variance=+0.65 |
| ENSEMBLE | +2.53 | phrase_alignment=+1.98, harmonic_consonance=+1.17 |

**Why it sounded terrible**: Sax maxed 3 features at the ±3 clamp ceiling. High scores ≠ good music. The features measure statistical properties, not musicality. Extreme values on multiple features simultaneously = gaming.

### Feature-Quality Correlations from Listening

| Feature | High z-score | Musical Quality |
|---------|--------------|-----------------|
| blue_ratio | +1.23 | Good (jazz identity) |
| collision_rate | +1.45 (low raw) | Good (instruments don't clash) |
| duration_variety | +1.33 | Good (rhythmic interest) |
| melodic_entropy | +3.00 (clamped) | Bad when maxed (random, not melodic) |
| dur_cv | +3.00 (clamped) | Bad when maxed (erratic, not groovy) |
| rhythm_2grams | +3.00 (clamped) | Bad when maxed (mechanical repetition) |

### Conclusion

The reward function works when:
1. **No instrument dominates** (spread < 0.3)
2. **No features are clamped** (all z-scores within ±2)
3. **Key features are positive**: blue_ratio, collision_rate (inverted), duration_variety

The reward function fails when:
1. **Single instrument spikes** (sax=+11.71)
2. **Multiple features hit clamp ceiling** (3 features at +3.00)
3. **Statistical extremes don't translate to musical quality**

---

## RLVR vs GEPA Comparison (2024-12-01)

### Runs Compared

| Run | Type | Config |
|-----|------|--------|
| `composer-001_20251130_220112` | RLVR | z-clamp ±3, recalibrated baselines, 30 steps |
| `gepa_20251130_220038` | GEPA | z-clamp ±3, acceptance gating, recalibrated baselines, 30 gens |

Both runs use the **same reward schema** (capped z-scores ±3, model-derived baselines).

### RLVR Dynamics

| Step | Reward | Sax | Bass | Piano | Drums | Ens |
|------|--------|-----|------|-------|-------|-----|
| 0 | 0.501 | +0.13 | -0.07 | -0.09 | -0.06 | +0.37 |
| 10 | 0.483 | +0.20 | +0.16 | -0.18 | -0.47 | -0.08 |
| 20 | 0.568 | -0.02 | +0.34 | +0.20 | **+1.52** | -0.13 |
| 29 | 0.667 | +0.18 | +0.49 | +1.56 | **+2.41** | -0.15 |

**Key finding:** RLVR learned to exploit drums. Drums z-score climbed from -0.06 → +2.41 over 30 steps. Reward increased (+0.16) but quality did not.

### Listening Test Results

| Sample | Reward | Spread | Verdict |
|--------|--------|--------|---------|
| RLVR best score (step_00/rollout_013) | 0.968 | 10.03 | Terrible. No jazz, piano makes ears bleed, random, too high pitched, no depth |
| RLVR best balance (step_12/rollout_002) | 0.409 | 0.25 | Not good. Bass too high, sax random, no coherence |
| RLVR #3 balanced (step_23/rollout_020) | 0.681 | 0.27 | 4/10. Best RLVR but low bar |
| RLVR #6 balanced (step_28/rollout_011) | 0.699 | 0.44 | Promising. "Start of something good" |
| **GEPA winner (gen_03/ind_024)** | 0.504 | 0.21 | **Best overall. Cohesive, story, better than Opus** |

### Feature Analysis: Why Samples Sound Good or Bad

#### RLVR Best Score (terrible, reward=0.968)
```
SAX (z=+9.77):  dur_cv=+3.00⚠️  rhythm_2grams=+3.00⚠️  melodic_entropy=+2.28⚠️
BASS (z=+2.87): ioi_swing=+2.56⚠️
ENSEMBLE:       phrase_alignment=+2.76⚠️
```
**4 features at ceiling.** High reward from stacking exploits, not quality.

#### RLVR Best Balance (not good, reward=0.409)
```
SAX:      melodic_entropy=-1.80 (boring), blue_ratio=+2.03⚠️
ENSEMBLE: harmonic_consonance=-2.00⚠️ (out of tune)
Gates:    variety_gate=0.5 on sax and piano (penalized)
```
**Low balance didn't help** — still has extremes and poor consonance.

#### RLVR #3 Balanced (4/10, reward=0.681)
```
SAX:   dur_cv=+3.00⚠️  rhythm_2grams=+3.00⚠️
PIANO: velocity_variance=+3.00⚠️
ENSEMBLE: collision_rate=-1.44, phrase_alignment=-1.13
```
**3 features at ceiling.** Instruments stepping on each other.

#### RLVR #6 Balanced (promising, reward=0.699)
```
SAX:   arpeggio_runs=+1.12, melodic_entropy=+0.27
PIANO: avg_chord_spread=+1.70, gap_ratio=+0.86
DRUMS: velocity_variance=+0.89
Only 1 feature near ceiling: phrase_alignment=+2.76⚠️
```
**Mostly healthy range.** Good arpeggio runs, open voicings.

#### GEPA Winner (best, reward=0.504)
```
SAX:      blue_ratio=+1.23, peak_not_late=+0.43
PIANO:    avg_chord_spread=+1.41
DRUMS:    duration_variety=+1.33
ENSEMBLE: phrase_alignment=+0.82, collision_rate=-0.11
**ZERO features at ceiling. All z-scores in [-1, +1.5] range.**
```
**Natural balance.** The z-clamp didn't constrain it — the output was organically balanced.

### Key Insight: Clamp Doesn't Prevent Exploitation

Both runs use z-clamp ±3. But:
- **RLVR** found ways to exploit WITHIN the clamp by stacking multiple features at +3.00
- **GEPA** (with acceptance gating) produced outputs that naturally stayed in healthy ranges

The clamp prevents single-feature runaway but doesn't prevent multi-feature stacking. RLVR's gradient signal pushes toward boundaries; GEPA's mutation + selection doesn't.

### Quality Correlates

| Metric | Quality Correlation |
|--------|---------------------|
| Spread < 0.3 | Strong positive |
| Zero features at ceiling | Strong positive |
| High reward | **Weak or negative** |
| All z-scores in [-1, +1.5] | Strong positive |

### Conclusion

**GEPA outperforms RLVR on musical quality** despite RLVR having higher rewards. Evolution with acceptance gating finds balanced solutions; gradient descent finds boundary exploits.

The best output (GEPA gen_03/ind_024) has:
- Lowest spread (0.21)
- Zero ceiling hits
- Lower reward (0.504) than RLVR best (0.968)
- **Best subjective quality by far**

---

## Deep Dive: Why Did the Winner Win? (2024-12-01)

### The Winner is a Statistical Outlier

Analysis of 838 valid GEPA outputs from `gepa_20251130_220038`:

| Metric | Winner | Population Mean | Population Std | Percentile |
|--------|--------|-----------------|----------------|------------|
| Reward | 0.504 | 0.488 | 0.130 | 55.6% |
| Spread | **0.21** | 2.92 | 1.65 | **0.0%** (LOWEST) |

The winner's reward is **average** (55th percentile), but its spread is the **lowest in the entire population**.

### Spread Distribution

- Only **1 output** (0.1%) has spread < 0.3
- Only **4 outputs** (0.5%) have spread < 0.5
- Population mean spread: **2.92**
- Winner spread: **0.21** — literally the minimum

### The Winner is SIMPLE, Not Complex

Feature percentile analysis reveals the winner is unusual for being **boring**:

**6 features at 0th percentile (lowest in population):**
- `sax_dur_cv = 0.000` — No duration variety (all notes same length)
- `sax_arpeggio_runs = 0` — No arpeggios
- `bass_ioi_swing = 0.000` — No swing
- `drums_velocity_variance = 0.000` — Constant velocity
- `drums_snare_backbeat = 0.000` — No backbeat variation
- `piano_velocity_variance = 0.000` — Constant velocity

**Only 1 feature stands out HIGH:**
- `piano_avg_chord_spread = 11.33` (93rd percentile) — Wide, open voicings

**Interpretation:** The winner sounds good because it's **restrained**. No flashy arpeggios, no velocity dynamics, no swing. Just simple, clear lines with open piano voicings creating space.

### No Prompt Evolution — Pure Sampling Luck

Critical finding from mutation analysis:

| Metric | Value |
|--------|-------|
| Total outputs | 838 |
| Original prompt (0 diff lines) | 836 (99.8%) |
| Mutated prompt (any diff) | 2 (0.2%) |
| Winner's diff lines | **0** |

**Acceptance gating rejected almost ALL mutations.** The "evolution" is actually just rejection sampling from the same base prompt.

| | Original (n=756) | Mutated (n=82) |
|---|---|---|
| Mean reward | 0.490 | 0.473 |
| Mean spread | 2.88 | 3.29 |
| Min spread | **0.21** | 0.54 |

Mutated outputs are **worse** on average. The winner came from the original prompt with zero mutations.

### Code Analysis: What Made This Sample Different?

The winner uses the **exact same prompt** as 755 other outputs. The difference is in what the model generated:

**Winner's sax line:**
```python
# Simple 2-note motif repeated 3x then resolved
D-Bb, D-Bb, D-Bb-F-C  (8 notes total)
```

**Comparison sample's sax line:**
```python
# More complex, longer phrases
(varies, typically 12-20 notes with more intervals)
```

**Winner's piano:**
- 3 sparse chords, different voicings each bar
- Short stabs (0.375s), not sustained pads

**Winner's drums:**
- velocity=100 uniform (no dynamics)
- Simple kick-snare-hihat pattern

### The Real Conclusion

The winner is NOT the result of:
- ❌ Prompt evolution (0 diff lines)
- ❌ High reward optimization (55th percentile reward)
- ❌ Complex musical features (6 features at 0th percentile)

The winner IS the result of:
- ✅ **Sampling luck** — 1 in 756 samples with original prompt
- ✅ **Simplicity** — model happened to generate restrained, clear code
- ✅ **Balance** — all instruments near zero z-score by chance
- ✅ **Open voicings** — piano chord spread at 93rd percentile

### Implications for Training

1. **GEPA acceptance gating is too strict** — 99.8% rejection rate means no evolution
2. **Balance correlates with quality** — but it's a proxy for "nothing went crazy"
3. **Simplicity beats complexity** — the reward function rewards variance, but musicality comes from restraint
4. **More samples > more generations** — with current setup, just sample more from base prompt

### Recommendation

Instead of GEPA evolution, consider:
1. **Best-of-N sampling** — generate N samples from base prompt, select by spread < 0.3
2. **Simplicity penalty** — reduce reward for high variance features
3. **Fix acceptance gating** — current 99.8% rejection rate means no learning

---

## 30-Track Listening Test (2024-12-01)

### Test Design

Blind listening test with 30 tracks:
- 9 tracks previously heard (highlights + variants)
- 10 random GEPA samples
- 11 random RLVR samples
- Randomized order

### Results Summary

| Metric | Value |
|--------|-------|
| Overall mean score | **3.85/10** |
| Score range | 1.0 - 6.5 |
| Reward↔Score correlation | **0.191** (nearly random) |

### By Source

| Source | Tracks | Mean Score |
|--------|--------|------------|
| GEPA | 14 | 3.71 |
| RLVR | 15 | 3.80 |
| GEPA + bass fix | 1 | **6.50** |

### Top 5 by Human Score

| Score | Track | Reward | Notes |
|-------|-------|--------|-------|
| **6.5** | old_winner_bass_octave_down | 0.504 | **WINNER.** Bass pitched to D2 range |
| 6.0 | GEPA_gen_001_ind_019 | 0.443 | "Provocative, fast, bursty, unique" |
| 6.0 | GEPA_best_balance | 0.504 | Previously called "best one, cohesive" |
| 5.5 | RLVR_best_metrics | 0.776 | "Sounds good, complex chords, but not jazz" |
| 5.0 | RLVR_step_003_rollout_022 | 0.225 | "Sax had depth" |

### Bottom 5 by Human Score

| Score | Track | Reward | Notes |
|-------|-------|--------|-------|
| 2.5 | GEPA_gen_023_ind_004 | 0.365 | "Super basic" |
| 2.5 | RLVR_step_005_rollout_023 | 0.222 | "Out there, terrible, but something" |
| 2.0 | GEPA_gen_017_ind_016 | 0.493 | "Not jazz, super basic" |
| 1.5 | GEPA_mutated_best | 0.660 | "Really basic, does not sound good" |
| 1.0 | RLVR_step_004_rollout_005 | 0.199 | "Sounded random" |

### Key Finding: Reward Does NOT Predict Quality

| Track | Reward | Human Score |
|-------|--------|-------------|
| GEPA_best_metrics | **0.955** | 4.0 |
| GEPA_mutated_best | **0.660** | 1.5 |
| RLVR_best_metrics | **0.776** | 5.5 |
| GEPA_best_balance | 0.504 | 6.0 |
| GEPA + bass fix | 0.504 | **6.5** |

**Correlation = 0.191** — reward is essentially uncorrelated with human preference.

### Full Ratings with Notes

| # | Track | Reward | Score | Notes |
|---|-------|--------|-------|-------|
| 1 | GEPA_gen_023_ind_004 | 0.365 | 2.5 | "Super basic. Extra 0.5 for sax having a little difference at the end" |
| 2 | RLVR_step_016_rollout_014 | 0.303 | 3.0 | "Some complexity, but not jazz" |
| 3 | RLVR_step_016_rollout_019 | 0.312 | 4.0 | "Not jazz, complexity was there. Wish variation in sax note lengths" |
| 4 | GEPA_gen_036_ind_016 | 0.276 | 4.0 | "Bass and drums great. Sax and piano muddied it, out of tune, repetitive" |
| 5 | RLVR_step_009_rollout_012 | 0.235 | 3.5 | "Sax melody good. Bass strong, liked low registers. Piano random like kid smashing keys. Drums basic" |
| 6 | RLVR_step_004_rollout_005 | 0.199 | 1.0 | "Sounded random" |
| 7 | GEPA_gen_001_ind_019 | 0.443 | 6.0 | "Really provocative. Fast pace, drums and sax bursts catch attention. Very unique. Could be more cohesive. Wish more piano depth. Bass line good" |
| 8 | GEPA_gen_017_ind_016 | 0.493 | 2.0 | "Sounds okay. Just not jazz, super basic" |
| 9 | RLVR_step_015_rollout_015 | 0.213 | 3.0 | "Really liked the bass line. Everything else was shit" |
| 10 | GEPA_gen_030_ind_020 | 0.592 | 3.5 | "Same motif structure as best GEPA but didn't execute well. Resolved on up note. Other parts underwhelming" |
| 11 | GEPA_best_metrics | 0.955 | 4.0 | "Liked super low sax notes and burstiness, but didn't sound like music" |
| 12 | RLVR_step_003_rollout_022 | 0.225 | 5.0 | "Sax had depth. Wish variation in note lengths. Other tracks not good" |
| 13 | RLVR_best_metrics | 0.776 | 5.5 | "Sounds good. Sounds like music. Complexity in chords. But not jazz and no variation in note lengths" |
| 14 | GEPA_mutated_best | 0.660 | 1.5 | "Really basic, does not sound good" |
| 15 | RLVR_best_balance | 0.262 | 3.5 | "Similar to best GEPA motif structure. Missed on execution. Other parts underwhelming except drum start" |
| 16 | GEPA_gen_039_ind_029 | 0.532 | 4.5 | "Didn't sound like music, but appreciate sax complexity. Sax could have carried it to 6" |
| 17 | RLVR_step_005_rollout_012 | 0.252 | 4.0 | "Really basic. Sounds good" |
| 18 | RLVR_balanced_positive | 0.443 | 5.0 | "Sounds like the 5.5 one but slightly worse" |
| 19 | GEPA_best_balance | 0.504 | 6.0 | Previously "best one, cohesive" |
| 20 | GEPA_gen_003_ind_006 | 0.623 | 4.0 | "Kinda sounds like just playing scales, but okay" |
| 21 | GEPA_gen_027_ind_020 | 0.491 | 3.0 | "Liked sax complexity, but didn't sound good and out of tune" |
| 22 | GEPA_gen_015_ind_030 | 0.632 | 4.0 | "Sounded like music, not jazz, didn't sound great" |
| 23 | old_winner_bass_octave_down | 0.504 | **6.5** | "Better than Track 19 because bass pitched down. **Preference for bass pitched down — should support sax lead**" |
| 24 | GEPA_gen_012_ind_026 | 0.322 | 3.5 | "Really basic, sounds okay" |
| 25 | RLVR_step_002_rollout_005 | 0.182 | 4.0 | "Sounds like half-baked best GEPA run" |
| 26 | RLVR_step_007_rollout_028 | 0.212 | 4.5 | "Appreciated sax complexity. Riff at end sounded good. Everything else trash, especially ascending piano/bass (hard to tell, bass not pitched down)" |
| 27 | RLVR_step_012_rollout_027 | 0.241 | 4.0 | "Short staccato galore. No depth in note lengths" |
| 28 | RLVR_step_005_rollout_023 | 0.222 | 2.5 | "Liked how out there it was. Sax in top register. Sounded terrible but was something" |
| 29 | RLVR_jazziest | 0.424 | 4.5 | "Liked the burstiness. Wish variation in note length" |
| 30 | GEPA_gen_044_ind_001 | 0.497 | 3.5 | "Sax melody sounded good, just wasn't jazz" |

### Recurring Feedback Themes

| Theme | Count | Examples |
|-------|-------|----------|
| "Not jazz" | 12 | Tracks 2, 3, 8, 13, 22, 30 |
| "No variation in note length" | 9 | Tracks 3, 5, 12, 16, 26, 27, 29 |
| "Basic/simple" (negative) | 7 | Tracks 1, 8, 14, 17, 24 |
| "Sax complexity appreciated" | 6 | Tracks 5, 16, 21, 26 |
| "Bass should be pitched down" | 3 | Tracks 23, 26 |
| "Out of tune" | 3 | Tracks 4, 21 |

### Bass Register Finding

**Track 23 (winner) bass range: D2-F#2 (MIDI 38-42)**
**Track 19 (original) bass range: D3-F#3 (MIDI 50-54)**

Pitching bass down 1 octave to D2 range improved score from 6.0 → 6.5 (+8%).

User quote: "Preference for bass pitched down. Should be supporting the sax lead, not soloing. Exception: bass solos/riffs."

---

## Human Preference Model (2024-12-01)

### What Makes a Good Track

Based on 30-track listening test feedback:

1. **Variation in note length** — adds complexity and depth (mentioned 9 times)
2. **Variation in motif types** — sub-motifs, not one repeated pattern
3. **Burstiness** — dynamic contrast, not monotonous
4. **Sustained chords** — but must sound like jazz (not yet achieved)
5. **Jazz quality** — the ineffable thing metrics don't capture

### What the Current Reward Function is Missing

| Missing Feature | Current State | Proposed Fix |
|-----------------|---------------|--------------|
| Note length variation | `dur_cv` exists but weak weight | Increase weight 2-3x |
| Motif variety | Only `rhythm_2grams` | Add melodic motif detection |
| Burst/sustain contrast | Not measured | Add `staccato_vs_legato_ratio` |
| Jazz detector | Not measured | Harder problem — needs ML classifier |
| Bass register | No penalty | Add penalty if bass > MIDI 55 (G3) |

### Proposed Reward Function Changes

#### 1. Bass Register Penalty (Low-hanging fruit)

```python
# In reward_bass.py
def bass_register_penalty(notes):
    """Penalize bass notes above G3 (MIDI 55)."""
    high_notes = sum(1 for n in notes if n.pitch > 55)
    ratio = high_notes / len(notes) if notes else 0
    return 1.0 - (0.5 * ratio)  # Up to 50% penalty
```

**Expected impact:** +0.5 points (based on Track 19 → 23 improvement)

#### 2. Increase dur_cv Weight

```python
# In reward_sax.py - REFERENCE_STATS
'dur_cv': {'mean': 0.20, 'std': 0.25, 'direction': 1, 'weight': 2.0},  # was 1.0
```

**Rationale:** Mentioned in 9/30 reviews. Currently underweighted.

#### 3. Add Staccato/Legato Contrast Feature

```python
def staccato_legato_ratio(notes):
    """Ratio of short notes (<0.2s) to long notes (>0.5s)."""
    short = sum(1 for n in notes if n.duration < 0.2)
    long = sum(1 for n in notes if n.duration > 0.5)
    if short + long == 0:
        return 0
    return min(short, long) / max(short, long)  # 1.0 = balanced mix
```

**Target:** Standards have ~0.8-1.0 ratio. Current outputs have ~0.0-0.2.

#### 4. Descending End Feature (Sax)

From earlier analysis: melody ending going DOWN sounds "in tune" even with same consonance score.

```python
def descending_end(notes):
    """Does melody end on a descending interval?"""
    if len(notes) < 2:
        return 0
    last_interval = notes[-1].pitch - notes[-2].pitch
    return 1 if last_interval < 0 else 0
```

### Priority Order

1. **Bass register penalty** — trivial to implement, proven +0.5 impact
2. **Increase dur_cv weight** — config change only
3. **Descending end** — simple feature, strong signal from earlier analysis
4. **Staccato/legato ratio** — new feature, moderate implementation
5. **Jazz classifier** — hard problem, defer

### Summary

**Current reward correlation with human preference: 0.191**

The reward function is broken. It optimizes for statistical properties that don't correlate with musicality. The winner (6.5/10) came from a simple post-hoc fix (bass down 1 octave), not from training.

**Immediate fixes:**
1. Bass register penalty
2. dur_cv weight increase
3. descending_end feature

**These should bring correlation to ~0.4-0.5.** Full "sounds like jazz" detection remains unsolved.

---

## Quantitative Feature Analysis (2024-12-01)

### Per-Instrument Human Scores

Imputed per-instrument scores (1-10) for all 30 tracks based on qualitative feedback. Saved to `baselines/human_instrument_scores.json`.

### Per-Instrument Correlation: Reward Z-Score vs Human Score

| Instrument | Correlation | Signal |
|------------|-------------|--------|
| Sax | +0.222 | Weak |
| Bass | **-0.019** | **ZERO** |
| Piano | +0.238 | Weak |
| Drums | +0.055 | Near-zero |
| Ensemble | +0.099 | Very weak |

**Bass reward function has ZERO correlation with human perception of bass quality.**

### Feature-Level Correlation with Overall Human Score

**TOP FEATURES (|corr| > 0.2 — KEEP):**

| Rank | Feature | Corr | Direction |
|------|---------|------|-----------|
| 1 | `piano_avg_chord_spread` | +0.388 | higher=better |
| 2 | `drums_duration_variety` | +0.280 | higher=better |
| 3 | `sax_rhythm_2grams` | +0.250 | higher=better |
| 4 | `ensemble_collision_rate` | -0.250 | **INVERT** |
| 5 | `piano_gap_ratio` | +0.243 | higher=better |
| 6 | `ensemble_texture_density` | +0.229 | higher=better |

**NOISE FEATURES (|corr| < 0.1 — REMOVE OR REWEIGHT):**

| Feature | Corr | Original r (n=11) | Problem |
|---------|------|-------------------|---------|
| `sax_melodic_entropy` | -0.072 | +0.756 | **INVERTED** in real data |
| `bass_ioi_swing` | +0.026 | +0.697 | No signal |
| `bass_non_chromatic_ratio` | +0.059 | +0.846 | No signal |
| `drums_kick_off_beat_ratio` | -0.079 | +0.959 | **Was 'best predictor'** |
| `drums_velocity_variance` | +0.073 | +0.558 | No signal |
| `sax_peak_not_late` | +0.036 | +0.650 | No signal |
| `ensemble_phrase_alignment` | +0.030 | -0.701 | No signal |
| `sax_sax_arpeggio_runs` | +0.017 | +0.397 | No signal |

**Key finding:** Original analysis (n=11) was overfitted. With n=30 human-rated samples, many "strong" features show zero correlation.

### Top 6 vs Bottom 6 Feature Comparison

| Feature | TOP 6 | BOT 6 | Δ | Signal |
|---------|-------|-------|---|--------|
| `sax_rhythm_2grams` | +0.88 | -0.38 | **+1.26** | *** |
| `piano_avg_chord_spread` | +0.78 | -0.05 | **+0.82** | ** |
| `ensemble_harmonic_consonance` | +0.14 | -0.65 | **+0.79** | ** |
| `piano_gap_ratio` | -0.07 | -0.85 | **+0.78** | ** |
| `ensemble_texture_density` | +0.44 | -0.30 | **+0.73** | ** |
| `ensemble_collision_rate` | -0.37 | +0.21 | **-0.58** | ** |
| `drums_duration_variety` | +0.14 | -0.41 | **+0.55** | ** |
| `sax_dur_cv` | -0.22 | -0.49 | +0.28 | weak |
| `sax_blue_ratio` | +0.27 | +0.10 | +0.17 | weak |

### Revised Feature Recommendations

**TIER 1 — Keep with current weight:**
- `sax_rhythm_2grams` (+1.26 separation)
- `piano_avg_chord_spread` (+0.82)
- `ensemble_harmonic_consonance` (+0.79)
- `piano_gap_ratio` (+0.78)
- `ensemble_texture_density` (+0.73)
- `ensemble_collision_rate` (-0.58, INVERT)
- `drums_duration_variety` (+0.55)

**TIER 2 — Keep but may need reweighting:**
- `sax_dur_cv` (+0.28)
- `sax_blue_ratio` (+0.17)

**TIER 3 — Remove or drastically reduce weight:**
- `sax_melodic_entropy` (inverted in practice)
- `bass_ioi_swing` (no signal)
- `bass_non_chromatic_ratio` (no signal)
- `drums_kick_off_beat_ratio` (no signal)
- `drums_velocity_variance` (no signal)
- `sax_peak_not_late` (no signal)
- `ensemble_phrase_alignment` (no signal)
- `sax_sax_arpeggio_runs` (no signal)

### Spread Finding Revisited

**Spread vs Overall Human Score: +0.031** (essentially zero)

Earlier hypothesis that "spread < 0.3 = quality" does not hold across all 30 samples. Balance may be necessary but not sufficient.

### Implications for Reward Design

1. **Prune noise features:** Remove or zero-weight TIER 3 features. They add noise to the gradient.

2. **Bass reward is broken:** Two features (`ioi_swing`, `non_chromatic_ratio`) have no signal. Need new bass features or bass register penalty.

3. **Drums reward is broken:** `kick_off_beat_ratio` was the "best predictor" (r=0.96) in n=11 analysis but shows -0.079 in n=30. Likely overfit to standards having zero kicks.

4. **Ensemble features work best:** 4/6 top features are ensemble or piano. Per-instrument features have weaker signal.

5. **Gating on TIER 1 features:** Consider hard gates on:
   - `piano_avg_chord_spread > 0` (open voicings)
   - `sax_rhythm_2grams > 0` (has rhythm hook)
   - `ensemble_collision_rate < 0.5` (don't collide)
   - `ensemble_harmonic_consonance > 0.6` (in tune)
