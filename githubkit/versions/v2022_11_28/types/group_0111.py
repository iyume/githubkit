"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict


class RepositoryRuleRequiredLinearHistoryType(TypedDict):
    """required_linear_history

    Prevent merge commits from being pushed to matching refs.
    """

    type: Literal["required_linear_history"]


__all__ = ("RepositoryRuleRequiredLinearHistoryType",)
