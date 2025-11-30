"""
GEPA Evaluation: Pareto selection for multi-objective optimization.
"""

from typing import Dict, List
from dataclasses import dataclass, field


@dataclass
class Individual:
    """An individual in the population."""
    id: int
    prompt: str
    reward: float = 0.0
    metrics: Dict[str, float] = field(default_factory=dict)
    traces: List[Dict] = field(default_factory=list)  # execution traces for reflection


def dominates(a: Individual, b: Individual) -> bool:
    """True if a dominates b (a >= b on all objectives, a > b on at least one)."""
    dominated = False
    for key in a.metrics:
        if key not in b.metrics:
            continue
        if a.metrics[key] < b.metrics[key]:
            return False
        if a.metrics[key] > b.metrics[key]:
            dominated = True
    return dominated


def compute_pareto_fronts(population: List[Individual]) -> List[List[Individual]]:
    """
    Compute Pareto fronts using non-dominated sorting.

    Returns list of fronts, where front[0] is the Pareto-optimal set.
    """
    remaining = list(population)
    fronts = []

    while remaining:
        front = []
        for ind in remaining:
            is_dominated = False
            for other in remaining:
                if other is not ind and dominates(other, ind):
                    is_dominated = True
                    break
            if not is_dominated:
                front.append(ind)

        fronts.append(front)
        remaining = [ind for ind in remaining if ind not in front]

    return fronts


def select_survivors(population: List[Individual], target_size: int) -> List[Individual]:
    """
    Select survivors using NSGA-II style selection.
    Fill from front 0, then front 1, etc. until target_size reached.
    """
    fronts = compute_pareto_fronts(population)
    survivors = []

    for front in fronts:
        if len(survivors) + len(front) <= target_size:
            survivors.extend(front)
        else:
            # Partial front - just take first N needed
            needed = target_size - len(survivors)
            survivors.extend(front[:needed])
            break

    return survivors


async def mutate_prompt(
    client,
    model_name: str,
    prompt: str,
    traces: List[Dict],
) -> str:
    """
    GEPA reflective mutation: LLM analyzes execution traces and proposes prompt improvement.

    Args:
        client: AsyncOpenAI client
        model_name: Model to use for reflection
        prompt: Current system prompt
        traces: List of execution traces [{reward, unique_durs, has_rests, error}, ...]

    Returns:
        Improved prompt
    """
    if not traces:
        return prompt  # No traces to reflect on yet

    # Use most recent trace with code
    t = traces[-1]
    error_str = f", error={t['error']}" if t.get('error') else ""

    # Extract sax-related code if available
    code = t.get('code', '')
    if code:
        # Try to extract just the sax portion
        lines = code.split('\n')
        sax_lines = []
        in_sax = False
        for line in lines:
            if 'sax' in line.lower() or in_sax:
                sax_lines.append(line)
                if 'sax.notes' in line and 'extend' in line:
                    in_sax = False
                elif 'sax_notes' in line and '=' in line:
                    in_sax = True
        code_snippet = '\n'.join(sax_lines[:30]) if sax_lines else code[:1500]
    else:
        code_snippet = "(no code available)"

    reflection_prompt = f"""You are improving a system prompt for jazz MIDI generation.

CURRENT PROMPT:
{prompt}

LAST OUTPUT:
reward={t['reward']:.2f}, unique_durs={t.get('unique_durs', '?')} (distinct note lengths), has_rests={t.get('has_rests', '?')} (gaps between notes){error_str}

SAX CODE:
```python
{code_snippet}
```

Analyze the code. What's causing the metrics? Propose an improved prompt.

Output ONLY the improved prompt, no explanation."""

    try:
        response = await client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": reflection_prompt}],
            max_completion_tokens=4000,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception:
        return prompt  # Fallback to original on error
