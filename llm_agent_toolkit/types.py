"""Shared types used across modules."""
from dataclasses import dataclass, field


@dataclass
class Issue:
    issue_id: str
    repo: str
    description: str
    base_commit: str = ""
    fail_to_pass: list[str] = field(default_factory=list)
    pass_to_pass: list[str] = field(default_factory=list)


class BudgetExhaustedError(Exception):
    pass


@dataclass
class ActionEvent:
    action_name: str
    arguments: dict
    result: str
