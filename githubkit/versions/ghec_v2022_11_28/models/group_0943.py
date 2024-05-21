"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoActionsVariablesPostBody(GitHubModel):
    """ReposOwnerRepoActionsVariablesPostBody"""

    name: str = Field(description="The name of the variable.")
    value: str = Field(description="The value of the variable.")


model_rebuild(ReposOwnerRepoActionsVariablesPostBody)

__all__ = ("ReposOwnerRepoActionsVariablesPostBody",)