"""Exceptions related to execution witness validation."""


class ExecutionWitnessValidationError(Exception):
    """Custom exception for execution witness validation errors."""

    pass


class StatelessValidationError(Exception):
    """
    Raised when stateless validation cannot proceed: a required
    artifact is missing, or the active fork has no stateless support.
    """

    pass
