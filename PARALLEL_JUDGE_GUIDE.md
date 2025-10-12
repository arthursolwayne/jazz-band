# Parallel Judge Architecture Guide

## Overview

The Jazz Judge system has been refactored from a **monolithic single-LLM architecture** to a **parallel multi-judge architecture** while maintaining backward compatibility.

### Architecture Comparison

**Before (Monolithic):**
```
1 LLM call → Judge → 5 criterion scores + overall score + rationale + suggestions
```

**After (Parallel):**
```
5 parallel LLM calls → [Harmony, Rhythm, Melody, Interplay, Authenticity] judges
                    ↓
1 aggregator LLM call → Combines results → Same output format
```

## Files Created

### Criterion Judge Prompts
- **`prompts/judges/harmony.md`** - Jazz Harmony evaluation (7th chords, voice leading, extensions)
- **`prompts/judges/rhythm.md`** - Latin Jazz Rhythm evaluation (upbeat syncopation, groove)
- **`prompts/judges/melody.md`** - Jazz Melody & Phrasing evaluation (bebop vocabulary, rests)
- **`prompts/judges/interplay.md`** - Interplay & Space evaluation (progressive build, arrangement)
- **`prompts/judges/authenticity.md`** - Jazz Authenticity evaluation (vibe, memorability, idioms)

### Aggregator Prompt
- **`prompts/judges/aggregator.md`** - Combines criterion results, applies threshold caps, generates final critique

### Code Updates
- **`src/jazz_band/agents/judge.py`**
  - Added `critique_parallel()` function (new parallel mode)
  - Kept `critique()` function (original monolithic mode as fallback)
  - Added helper functions: `_call_criterion_judge()`, `_call_aggregator()`, `_build_aggregator_user_prompt()`

- **`src/jazz_band/agents/__init__.py`**
  - Exported `critique_parallel` alongside `critique`

## Usage

### Option 1: Monolithic Mode (Original)

```python
from jazz_band.agents import critique

critique_result = await critique(
    model=model,
    jam_json=jam_json,
    summary="8-bar Latin jazz intro"
)
```

### Option 2: Parallel Mode (New)

```python
from jazz_band.agents import critique_parallel

critique_result = await critique_parallel(
    model=model,
    jam_json=jam_json,
    summary="8-bar Latin jazz intro"
)
```

**Both functions return the same structure:**
```python
{
    "overall_score": 4.6,
    "scores": {
        "jazz_harmony": 3,
        "latin_jazz_rhythm": 4,
        "jazz_melody": 5,
        "interplay_space": 4,
        "jazz_authenticity": 5
    },
    "rationale": "2-4 sentence summary...",
    "suggestions": ["Specific suggestion 1", "Specific suggestion 2", ...],
    "prompt_mutation": "Hint for improving the composer prompt..."
}
```

## Benefits of Parallel Architecture

1. **Focused Evaluation**: Each criterion judge specializes in one aspect of jazz
2. **Scalability**: Criterion judges run in parallel (5x faster with async)
3. **Easier Prompt Engineering**: Modify individual criterion prompts independently
4. **Debugging**: See scores breakdown before aggregation
5. **Extensibility**: Easy to add new criteria (e.g., "jazz_dynamics", "jazz_articulation")

## Implementation Details

### Criterion Judge Output Format

Each criterion judge returns:
```json
{
  "score": 5,
  "rationale": "2-3 sentences explaining the score with specific observations",
  "suggestion": "1-2 specific, actionable improvements"
}
```

### Aggregator Responsibilities

1. **Apply Threshold Caps**: Check for deficiencies mentioned in rationales, cap scores if needed
   - Triads only → jazz_harmony ≤ 3
   - No upbeat syncopation → latin_jazz_rhythm ≤ 3
   - Aimless scalar runs → jazz_melody ≤ 4
   - No progressive build/space → interplay_space ≤ 4

2. **Calculate Overall Score**: Average of 5 capped scores, rounded to 1 decimal

3. **Synthesize Rationale**: Combine insights from all judges into 2-4 sentences

4. **Prioritize Suggestions**: Pull suggestions from lowest-scoring criteria first (3-5 total)

### Dry-Run Mode

Both `critique()` and `critique_parallel()` support dry-run mode:

```python
# Dry-run returns deterministic stub data (no LLM calls)
result = await critique_parallel(model=None, jam_json=jam_json)
```

## Migration Guide

### For RLVR Training Loop (rlvr/loop.py)

To switch to parallel mode:

```python
# BEFORE (monolithic):
from jazz_band.agents import critique
critique_result = await critique(model, jam_json, summary)

# AFTER (parallel):
from jazz_band.agents import critique_parallel
critique_result = await critique_parallel(model, jam_json, summary)
```

### Adding a Mode Flag

You can add a flag to switch between modes:

```python
from jazz_band.agents import critique, critique_parallel

async def evaluate_arrangement(model, jam_json, summary, use_parallel=True):
    if use_parallel:
        return await critique_parallel(model, jam_json, summary)
    else:
        return await critique(model, jam_json, summary)
```

## Strict Scoring Standards

All criterion judges maintain the **strict jazz standards** from the original prompt:

- **NO LENIENCY from generation 0**
- Early attempts expected to score 4-5/10
- Threshold caps applied rigorously
- Full score range (0-10) used honestly
- Specific, actionable feedback

## Testing

Run the structure validation test:

```bash
python3 test_judge_structure.py
```

This verifies:
- All prompt files exist
- judge.py has correct functions
- Module exports are correct
- Documentation is present

## Performance

**Monolithic mode:**
- 1 LLM call (1500 max tokens)
- ~2-4 seconds per critique

**Parallel mode:**
- 6 LLM calls (5 × 800 tokens + 1 × 1500 tokens)
- ~2-4 seconds per critique (thanks to async parallelization)
- Similar latency, more detailed evaluation

## Future Enhancements

Potential improvements to the parallel architecture:

1. **Add More Criteria**: Dynamics, articulation, form structure
2. **Weighted Aggregation**: Different criteria could have different weights
3. **Criterion-Specific Penalties**: More granular reward shaping in RLVR
4. **Multi-Stage Aggregation**: Hierarchical combination (rhythm+harmony → groove, etc.)
5. **Ensemble Voting**: Multiple judges per criterion, majority vote

## Troubleshooting

### JSON Parsing Errors

If a criterion judge returns invalid JSON:
```
ValueError: harmony judge returned invalid JSON
```

**Solution**: Check `prompts/judges/harmony.md` - ensure it emphasizes "Output pure JSON only, no markdown"

### Missing Scores

If aggregator fails with:
```
ValueError: Critique missing score: jazz_harmony
```

**Solution**: Verify criterion judges are returning all required fields (`score`, `rationale`, `suggestion`)

### Threshold Caps Not Applied

If scores seem too high despite deficiencies:

**Solution**: Check aggregator prompt - ensure it reviews rationales and applies caps correctly

## Questions?

For issues or improvements, see:
- `src/jazz_band/agents/judge.py` - Core implementation
- `prompts/judges/*.md` - Individual judge prompts
- `test_judge_structure.py` - Validation tests
