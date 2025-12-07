"""
GEPA Evaluation: Pareto selection for multi-objective optimization.
"""

import random
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
    population: List[Individual] = None,
    num_parents: int = 2,
) -> str:
    """
    GEPA reflective mutation: LLM analyzes execution traces and proposes prompt improvement.

    With crossover: shows traces from multiple parents to enable idea propagation.

    Args:
        client: AsyncOpenAI client
        model_name: Model to use for reflection
        prompt: Current system prompt
        traces: List of execution traces [{reward, unique_durs, has_rests, error}, ...]
        population: Optional list of other individuals for crossover
        num_parents: Number of other parents to show for crossover (default 2)

    Returns:
        Improved prompt
    """
    if not traces:
        return prompt  # No traces to reflect on yet

    # Find best and worst traces from self
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

    # Crossover: get best outputs from other parents in population
    other_parents = []
    if population and len(population) > 1:
        # Sample other individuals (exclude self by prompt match, require traces)
        others = [ind for ind in population if ind.prompt != prompt and ind.traces]
        if others:
            samples = random.sample(others, min(num_parents, len(others)))
            for i, other in enumerate(samples):
                other_sorted = sorted(other.traces, key=lambda t: t.get('reward', 0))
                other_best = other_sorted[-1]
                # Truncate prompt for readability
                other_prompt_preview = other.prompt[:300] + "..." if len(other.prompt) > 300 else other.prompt
                other_parents.append({
                    'label': chr(66 + i),  # B, C, D, ...
                    'prompt': other_prompt_preview,
                    'trace': other_best,
                })

    # Build reflection prompt with crossover if we have other parents
    if other_parents:
        other_sections = "\n\n".join([
            f"COMPOSER {op['label']} (different approach):\n{op['prompt']}\n\n{format_trace(op['trace'], 'Their best')}"
            for op in other_parents
        ])

        reflection_prompt = f"""You are Wayne Shorter. You've been playing saxophone for sixty years. You've played with Miles, with Art Blakey, with Weather Report. You've heard everything.

You're sitting in the back of The Cellar at 2am. Three young composers show you their best work. Each took a different approach. You're going to help them synthesize the best ideas.

COMPOSER A (current approach):
{prompt}

{best_section}

{worst_section}

{other_sections}

What's working across these different approaches? What patterns emerge in the successful outputs? Synthesize the best ideas from all of them into new instructions.

Write the improved prompt. Nothing else. Just the prompt that combines what works."""

    else:
        # Fallback: single-parent mutation (original GEPA-Lite behavior)
        reflection_prompt = f"""You are Wayne Shorter. You've been playing saxophone for sixty years. You've played with Miles, with Art Blakey, with Weather Report. You've heard everything.

You're sitting in the back of The Cellar at 2am. A young composer shows you two pieces — one that made you lean forward, one that made you look away. Both came from the same instructions.

THEIR PROMPT:
{prompt}

{best_section}

{worst_section}

The difference matters. What's working in the best one? What's failing in the worst? How would you change their instructions so every output sounds like the best one?

Write the improved prompt. Nothing else. Just the prompt that would make you stay for the next set."""

    try:
        response = await client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": reflection_prompt}],
            max_completion_tokens=4000,
            temperature=0.75,
        )
        return response.choices[0].message.content
    except Exception:
        return prompt  # Fallback to original on error
