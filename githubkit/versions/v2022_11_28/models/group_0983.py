"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoCheckSuitesPostBody(GitHubModel):
    """ReposOwnerRepoCheckSuitesPostBody"""

    head_sha: str = Field(description="The sha of the head commit.")


model_rebuild(ReposOwnerRepoCheckSuitesPostBody)

__all__ = ("ReposOwnerRepoCheckSuitesPostBody",)
