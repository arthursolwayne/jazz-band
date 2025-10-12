"""
Population Management for GEPA

Manages prompt variants (individuals) with gene knobs.
Each individual is a Composer prompt + numeric/textual parameters.
"""

import os
import random
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field, asdict
import shutil


@dataclass
class GeneKnobs:
    """
    Numeric and textual gene parameters for a prompt variant.
    """
    # Numeric genes (floats)
    chord_density: float = 0.5
    ghost_note_prob: float = 0.1
    motif_reuse_weight: float = 0.6
    syncopation_target: float = 0.4
    interplay_density: float = 0.5

    # Textual genes (lists of strings)
    do_list: List[str] = field(default_factory=list)
    dont_list: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "GeneKnobs":
        """Load from dictionary."""
        return cls(**data)

    @classmethod
    def from_defaults(cls, schema_path: Path) -> "GeneKnobs":
        """Create with default values from schema."""
        with open(schema_path, 'r') as f:
            schema = yaml.safe_load(f)

        numeric_defaults = {
            name: params['default']
            for name, params in schema['numeric'].items()
        }
        textual_defaults = {
            name: params['default']
            for name, params in schema['textual'].items()
        }

        return cls(
            chord_density=numeric_defaults['chord_density'],
            ghost_note_prob=numeric_defaults['ghost_note_prob'],
            motif_reuse_weight=numeric_defaults['motif_reuse_weight'],
            syncopation_target=numeric_defaults['syncopation_target'],
            interplay_density=numeric_defaults['interplay_density'],
            do_list=textual_defaults['do_list'].copy(),
            dont_list=textual_defaults['dont_list'].copy(),
        )


@dataclass
class Individual:
    """
    A single prompt variant with gene knobs and fitness metrics.
    """
    id: int
    prompt_text: str
    genes: GeneKnobs
    objectives: Optional[List[float]] = None  # 6D objective vector
    rank: Optional[int] = None  # Pareto rank (0 = front)
    crowding_distance: float = 0.0

    def save(self, base_dir: Path) -> None:
        """
        Save individual to directory: composer.md + genes.yaml

        Args:
            base_dir: Directory like gepa/population/0003/
        """
        base_dir.mkdir(parents=True, exist_ok=True)

        # Save prompt
        prompt_path = base_dir / "composer.md"
        with open(prompt_path, 'w') as f:
            f.write(self.prompt_text)

        # Save genes
        genes_path = base_dir / "genes.yaml"
        with open(genes_path, 'w') as f:
            yaml.dump(self.genes.to_dict(), f, default_flow_style=False)

    @classmethod
    def load(cls, individual_id: int, base_dir: Path) -> "Individual":
        """
        Load individual from directory.

        Args:
            individual_id: Individual ID
            base_dir: Directory like gepa/population/0003/

        Returns:
            Individual instance
        """
        prompt_path = base_dir / "composer.md"
        genes_path = base_dir / "genes.yaml"

        with open(prompt_path, 'r') as f:
            prompt_text = f.read()

        with open(genes_path, 'r') as f:
            genes_dict = yaml.safe_load(f)

        genes = GeneKnobs.from_dict(genes_dict)

        return cls(id=individual_id, prompt_text=prompt_text, genes=genes)


class Population:
    """
    Manages a population of prompt variants.
    """

    def __init__(
        self,
        population_dir: Path,
        schema_path: Path,
        size: int = 8
    ):
        """
        Initialize population manager.

        Args:
            population_dir: Directory for population (e.g., gepa/population/)
            schema_path: Path to genes_schema.yaml
            size: Population size
        """
        self.population_dir = population_dir
        self.schema_path = schema_path
        self.size = size
        self.individuals: List[Individual] = []

        # Create population directory
        self.population_dir.mkdir(parents=True, exist_ok=True)

    def initialize_from_base(self, base_prompt_path: Path) -> None:
        """
        Create initial population with random variations of base prompt.

        Args:
            base_prompt_path: Path to base composer.md (from prompts/)
        """
        # Load base prompt
        with open(base_prompt_path, 'r') as f:
            base_prompt = f.read()

        # Load schema for defaults and ranges
        with open(self.schema_path, 'r') as f:
            schema = yaml.safe_load(f)

        # Create individuals with small random variations
        for i in range(self.size):
            # Start with default genes
            genes = GeneKnobs.from_defaults(self.schema_path)

            # Add small random jitter to numeric genes
            for gene_name, gene_params in schema['numeric'].items():
                current_val = getattr(genes, gene_name)
                sigma = gene_params['mutation_sigma']
                new_val = current_val + random.gauss(0, sigma)
                # Clip to valid range
                new_val = max(gene_params['min'], min(gene_params['max'], new_val))
                setattr(genes, gene_name, new_val)

            # Maybe add one random do/dont item for variety
            if random.random() < 0.3 and schema['textual']['do_list']['examples']:
                example = random.choice(schema['textual']['do_list']['examples'])
                genes.do_list.append(example)

            # Optionally modify prompt text slightly (for diversity)
            # For now, use same base prompt (genes provide variation)
            prompt_text = base_prompt

            individual = Individual(id=i, prompt_text=prompt_text, genes=genes)
            individual.save(self.population_dir / f"{i:04d}")
            self.individuals.append(individual)

    def load_all(self) -> None:
        """Load all individuals from population directory."""
        self.individuals = []
        subdirs = sorted([d for d in self.population_dir.iterdir() if d.is_dir()])

        for i, subdir in enumerate(subdirs):
            individual = Individual.load(individual_id=i, base_dir=subdir)
            self.individuals.append(individual)

    def save_all(self) -> None:
        """Save all individuals to population directory."""
        for ind in self.individuals:
            ind.save(self.population_dir / f"{ind.id:04d}")

    def replace_with(self, new_individuals: List[Individual]) -> None:
        """
        Replace current population with new one.

        Args:
            new_individuals: New population (must have size <= self.size)
        """
        # Clear old population directory
        if self.population_dir.exists():
            shutil.rmtree(self.population_dir)
        self.population_dir.mkdir(parents=True, exist_ok=True)

        # Reassign IDs
        for i, ind in enumerate(new_individuals):
            ind.id = i

        self.individuals = new_individuals
        self.save_all()

    def get_elite(self, k: int) -> List[Individual]:
        """
        Get top k individuals by Pareto rank and crowding distance.

        Args:
            k: Number of elites to return

        Returns:
            List of elite individuals
        """
        # Sort by rank (ascending), then crowding distance (descending)
        sorted_pop = sorted(
            self.individuals,
            key=lambda ind: (ind.rank if ind.rank is not None else float('inf'), -ind.crowding_distance)
        )
        return sorted_pop[:k]


def create_initial_population(
    project_root: Path,
    population_size: int = 8,
    seed: Optional[int] = None
) -> Population:
    """
    Create and initialize a new population.

    Args:
        project_root: Project root directory
        population_size: Number of individuals
        seed: Random seed for reproducibility

    Returns:
        Initialized Population
    """
    if seed is not None:
        random.seed(seed)

    population_dir = project_root / "gepa" / "population"
    schema_path = project_root / "gepa" / "genes_schema.yaml"
    base_prompt_path = project_root / "prompts" / "composer.md"

    pop = Population(population_dir, schema_path, size=population_size)
    pop.initialize_from_base(base_prompt_path)

    return pop
