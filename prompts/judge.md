# Jazz Band Judge Agent

TODO: Rewrite for metrics-based evaluation.

The judge evaluates compositions based on pre-computed metrics and a text summary,
NOT raw MIDI data. This enables LLM-based critique without parsing binary formats.

## Input Format

The judge receives:
1. Pre-computed metrics (all 0.0-1.0):
   - upbeat_syncopation
   - seventh_chord_usage
   - groove_alignment
   - textural_arc
   - rhythmic_variety
   - dynamic_contrast
   - melodic_exploration
   - harmonic_movement
   - consonance

2. Composition summary:
   - Duration in seconds
   - Note counts per instrument
   - Pitch range per melodic instrument
   - Tempo and key

## Output Format

```json
{
  "overall_score": 0-10,
  "rationale": "2-4 sentences explaining score",
  "suggestions": ["actionable improvement 1", ...],
  "prompt_mutation": "hint for GEPA mutation"
}
```

## Role in GEPA

The judge's `prompt_mutation` field guides reflective evolution:
- Identifies what's missing or weak
- Suggests specific prompt changes
- Enables LLM-based mutation of composer prompts
