"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict

from .group_0132 import (
    RepositoryRulesetConditionsRepositoryNameTargetPropRepositoryNameType,
)


class RepositoryRulesetConditionsRepositoryNameTargetType(TypedDict):
    """Repository ruleset conditions for repository names

    Parameters for a repository name condition
    """

    repository_name: (
        RepositoryRulesetConditionsRepositoryNameTargetPropRepositoryNameType
    )


__all__ = ("RepositoryRulesetConditionsRepositoryNameTargetType",)
