"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class RepositoryRuleRulesetInfo(GitHubModel):
    """repository ruleset data for rule

    User-defined metadata to store domain-specific information limited to 8 keys
    with scalar values.
    """

    ruleset_source_type: Missing[Literal["Repository", "Organization"]] = Field(
        default=UNSET,
        description="The type of source for the ruleset that includes this rule.",
    )
    ruleset_source: Missing[str] = Field(
        default=UNSET,
        description="The name of the source of the ruleset that includes this rule.",
    )
    ruleset_id: Missing[int] = Field(
        default=UNSET, description="The ID of the ruleset that includes this rule."
    )


model_rebuild(RepositoryRuleRulesetInfo)

__all__ = ("RepositoryRuleRulesetInfo",)
