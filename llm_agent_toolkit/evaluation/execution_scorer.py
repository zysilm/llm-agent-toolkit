"""Execution scorer — Docker-based deterministic scoring."""
from llm_agent_toolkit.types import Issue


class ExecutionScorer:
    """Scores a patch by running the issue's test suite inside a Docker container."""

    def __init__(self, docker_image: str, timeout: int) -> None:
        self._docker_image = docker_image
        self._timeout = timeout

    def score(self, patch: str, issue: Issue) -> float:
        """Return a deterministic execution score in [0.0, 1.0].

        Stub logic (no actual Docker execution):
        - Invalid or empty patch  -> 0.0
        - Patch causes regression -> 0.0
        - Otherwise               -> 1.0 (assume all tests pass)
        """
        if not patch or patch.strip() == "not-a-valid-patch":
            return 0.0

        if "regression" in patch:
            return 0.0

        return 1.0
