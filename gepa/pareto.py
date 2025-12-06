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

    # Find best and worst traces
    sorted_traces = sorted(traces, key=lambda t: t.get('reward', 0))
    worst = sorted_traces[0]
    best = sorted_traces[-1]

    def extract_code_snippet(t):
        """Extract relevant code from trace."""
        code = t.get('code', '')
        if not code:
            return "(no code available)"
        # Truncate to reasonable length
        return code[:1200] + "..." if len(code) > 1200 else code

    def format_trace(t, label):
        """Format a trace for display with per-instrument breakdown."""
        error_str = f"\nError: {t['error']}" if t.get('error') else ""

        # Per-instrument scores (0-1 scale, higher is better)
        sax = t.get('sax', 0)
        bass = t.get('bass', 0)
        piano = t.get('piano', 0)
        drums = t.get('drums', 0)

        # Interpret scores
        def interpret(score, name):
            if score >= 0.9:
                return f"{name}: {score:.2f} ★ (excellent)"
            elif score >= 0.7:
                return f"{name}: {score:.2f} ✓ (good)"
            elif score >= 0.5:
                return f"{name}: {score:.2f} ~ (mediocre)"
            else:
                return f"{name}: {score:.2f} ✗ (weak)"

        return f"""{label}:
Overall: {t.get('reward', 0):.2f}
{interpret(sax, 'Sax')}
{interpret(bass, 'Bass')}
{interpret(piano, 'Piano')}
{interpret(drums, 'Drums')}
unique_durations={t.get('unique_durs', '?')}, has_rests={t.get('has_rests', '?')}{error_str}

```python
{extract_code_snippet(t)}
```"""

    best_section = format_trace(best, "BEST OUTPUT")
    worst_section = format_trace(worst, "WORST OUTPUT")

    reflection_prompt = f"""You are Wayne Shorter. You've been playing saxophone for sixty years. You've played with Miles, with Art Blakey, with Weather Report. You've heard everything.

You're sitting in the back of The Cellar at 2am. A young composer shows you two pieces — one that made you lean forward, one that made you look away. Both came from the same instructions.

THEIR PROMPT:
{prompt}

{best_section}

{worst_section}

The difference matters. What's working in the best one? What's failing in the worst? How would you change their instructions so every output sounds like the best one?

Write the improved prompt. Nothing else. Just the prompt that would make you stay for the next set.

IMPORTANT: Don't copy the raw metrics (reward scores, numbers) into your prompt. Translate what they mean into musical guidance the composer can act on."""

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
