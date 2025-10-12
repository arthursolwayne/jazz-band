"""
GEPA - Genetic-Pareto Reflective Prompt Evolution

Multi-objective evolutionary optimization for Composer prompts.
Evolves prompts across generations using Pareto selection and Judge-guided mutation.

Main modules:
- population: Manages prompt variants with gene knobs
- evaluate: Computes 6D objective vector (consonance, groove, motif, interplay, density, Judge)
- pareto: Non-dominated sorting, crowding distance, elite archiving
- mutate: Reflective (Judge-guided) + programmatic (numeric) mutation operators
- loop: Main GEPA runner with Weave logging
"""

from .population import Individual, Population
from .evaluate import evaluate_individual, ObjectiveVector
from .pareto import compute_pareto_front, archive_elites
from .mutate import mutate_individual
from .loop import run_gepa

__all__ = [
    "Individual",
    "Population",
    "evaluate_individual",
    "ObjectiveVector",
    "compute_pareto_front",
    "archive_elites",
    "mutate_individual",
    "run_gepa",
]
