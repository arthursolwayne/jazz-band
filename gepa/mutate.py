"""
Mutation Operators for GEPA

Implements reflective (Judge-guided) and programmatic (numeric jitter) mutations.
"""

import random
import yaml
import copy
from pathlib import Path
from typing import Dict, List, Optional
from .population import Individual, GeneKnobs


def mutate_numeric_genes(
    genes: GeneKnobs,
    schema_path: Path,
    mutation_rate: float = 0.8,
) -> GeneKnobs:
    """
    Apply Gaussian noise to numeric gene knobs.

    Args:
        genes: Current gene knobs
        schema_path: Path to genes_schema.yaml
        mutation_rate: Probability of mutating each gene

    Returns:
        Mutated gene knobs
    """
    # Load schema for ranges and sigmas
    with open(schema_path, 'r') as f:
        schema = yaml.safe_load(f)

    # Create copy
    mutated = copy.deepcopy(genes)

    # Mutate each numeric gene
    for gene_name, gene_params in schema['numeric'].items():
        if random.random() < mutation_rate:
            current_val = getattr(mutated, gene_name)
            sigma = gene_params['mutation_sigma']

            # Add Gaussian noise
            new_val = current_val + random.gauss(0, sigma)

            # Clip to valid range
            new_val = max(gene_params['min'], min(gene_params['max'], new_val))

            setattr(mutated, gene_name, new_val)

    return mutated


def mutate_textual_genes(
    genes: GeneKnobs,
    schema_path: Path,
    mutation_rate: float = 0.3,
) -> GeneKnobs:
    """
    Add/remove items from do_list and dont_list.

    Args:
        genes: Current gene knobs
        schema_path: Path to genes_schema.yaml
        mutation_rate: Probability of mutating textual genes

    Returns:
        Mutated gene knobs
    """
    if random.random() > mutation_rate:
        return genes

    # Load schema for examples
    with open(schema_path, 'r') as f:
        schema = yaml.safe_load(f)

    # Create copy
    mutated = copy.deepcopy(genes)

    # Mutate do_list
    if random.random() < 0.5 and schema['textual']['do_list']['examples']:
        # Add a new do item
        available_items = [
            item for item in schema['textual']['do_list']['examples']
            if item not in mutated.do_list
        ]
        if available_items:
            mutated.do_list.append(random.choice(available_items))
    elif len(mutated.do_list) > 0:
        # Remove a do item
        mutated.do_list.pop(random.randrange(len(mutated.do_list)))

    # Mutate dont_list
    if random.random() < 0.5 and schema['textual']['dont_list']['examples']:
        # Add a new dont item
        available_items = [
            item for item in schema['textual']['dont_list']['examples']
            if item not in mutated.dont_list
        ]
        if available_items:
            mutated.dont_list.append(random.choice(available_items))
    elif len(mutated.dont_list) > 0:
        # Remove a dont item
        mutated.dont_list.pop(random.randrange(len(mutated.dont_list)))

    return mutated


def mutate_reflective(
    prompt_text: str,
    genes: GeneKnobs,
    critique: Optional[Dict] = None,
) -> str:
    """
    Mutate prompt text using Judge feedback (reflective mutation).

    Uses suggestions and prompt_mutation from critique to guide text edits.

    Args:
        prompt_text: Current prompt text
        genes: Current gene knobs (for context)
        critique: Judge critique with suggestions and prompt_mutation

    Returns:
        Mutated prompt text
    """
    if critique is None or "suggestions" not in critique:
        # No critique available, return unchanged
        return prompt_text

    # Extract Judge guidance
    suggestions = critique.get("suggestions", [])
    prompt_mutation_hint = critique.get("prompt_mutation", "")

    # Build constraint additions from suggestions
    new_constraints = []
    for suggestion in suggestions[:2]:  # Use top 2 suggestions
        # Convert suggestion to constraint format
        constraint = f"- {suggestion}"
        new_constraints.append(constraint)

    if not new_constraints:
        return prompt_text

    # Inject constraints into prompt (append to "Musical Constraints" section)
    # Find the "Musical Constraints" section
    lines = prompt_text.split('\n')
    constraint_section_idx = None

    for i, line in enumerate(lines):
        if "Musical Constraints" in line or "## Musical" in line:
            constraint_section_idx = i
            break

    if constraint_section_idx is not None:
        # Find end of section (next ## or end of file)
        insert_idx = constraint_section_idx + 1
        for i in range(constraint_section_idx + 1, len(lines)):
            if lines[i].startswith("##"):
                insert_idx = i
                break
            insert_idx = i + 1

        # Insert new constraints before next section
        constraint_header = "\n### GEPA-Evolved Constraints:\n"
        new_lines = lines[:insert_idx] + [constraint_header] + new_constraints + lines[insert_idx:]
        return '\n'.join(new_lines)

    # Fallback: append to end
    return prompt_text + "\n\n### GEPA-Evolved Constraints:\n" + '\n'.join(new_constraints)


def mutate_individual(
    individual: Individual,
    schema_path: Path,
    critique: Optional[Dict] = None,
    use_reflective: bool = True,
    mutation_rate: float = 0.8,
) -> Individual:
    """
    Mutate an individual using programmatic + optionally reflective mutations.

    Args:
        individual: Individual to mutate
        schema_path: Path to genes_schema.yaml
        critique: Optional Judge critique for reflective mutation
        use_reflective: Whether to apply reflective mutation to prompt
        mutation_rate: Mutation rate for numeric/textual genes

    Returns:
        New mutated individual (original unchanged)
    """
    # Create copy
    mutated = Individual(
        id=individual.id,
        prompt_text=individual.prompt_text,
        genes=copy.deepcopy(individual.genes),
        objectives=None,  # Clear objectives (must be re-evaluated)
        rank=None,
        crowding_distance=0.0,
    )

    # Mutate numeric genes
    mutated.genes = mutate_numeric_genes(mutated.genes, schema_path, mutation_rate)

    # Mutate textual genes
    mutated.genes = mutate_textual_genes(mutated.genes, schema_path, mutation_rate * 0.5)

    # Reflective mutation (prompt text)
    if use_reflective and critique and random.random() < 0.5:
        mutated.prompt_text = mutate_reflective(mutated.prompt_text, mutated.genes, critique)

    return mutated


def validate_mutated_prompt(prompt_text: str) -> bool:
    """
    Validate that mutated prompt can still produce valid output.

    Basic check: ensure key sections are present.

    Args:
        prompt_text: Prompt text to validate

    Returns:
        True if valid
    """
    required_sections = [
        "JamJSON",
        "tempo",
        "key",
        "bars",
    ]

    for section in required_sections:
        if section not in prompt_text:
            return False

    return True
