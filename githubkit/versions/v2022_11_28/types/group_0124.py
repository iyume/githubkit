"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0125 import RepositoryRuleBranchNamePatternPropParametersType


class RepositoryRuleBranchNamePatternType(TypedDict):
    """branch_name_pattern

    Parameters to be used for the branch_name_pattern rule
    """

    type: Literal["branch_name_pattern"]
    parameters: NotRequired[RepositoryRuleBranchNamePatternPropParametersType]


__all__ = ("RepositoryRuleBranchNamePatternType",)
