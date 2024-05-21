"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class InteractionLimit(GitHubModel):
    """Interaction Restrictions

    Limit interactions to a specific type of user for a specified duration
    """

    limit: Literal["existing_users", "contributors_only", "collaborators_only"] = Field(
        description="The type of GitHub user that can comment, open issues, or create pull requests while the interaction limit is in effect."
    )
    expiry: Missing[
        Literal["one_day", "three_days", "one_week", "one_month", "six_months"]
    ] = Field(
        default=UNSET,
        description="The duration of the interaction restriction. Default: `one_day`.",
    )


model_rebuild(InteractionLimit)

__all__ = ("InteractionLimit",)