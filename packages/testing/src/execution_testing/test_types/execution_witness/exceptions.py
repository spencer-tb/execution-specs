"""Exceptions related to execution witness validation."""


class ExecutionWitnessValidationError(Exception):
    """Raised when execution witness content fails an expectation."""


class StatelessValidationError(Exception):
    """
    Raised when stateless validation cannot proceed: a required
    artifact is missing, or the active fork has no stateless support.
    """
