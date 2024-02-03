"""Workflows for the monorepo package."""

from monorepo_core.utils import sum_of_squares
from monorepo.utils import format_number


def run_workflow(x):
    """Run the monorepo workflow."""
    return format_number(sum_of_squares(x))
