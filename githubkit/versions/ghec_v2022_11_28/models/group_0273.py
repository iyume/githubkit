"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class GitRef(GitHubModel):
    """Git Reference

    Git references within a repository
    """

    ref: str = Field()
    node_id: str = Field()
    url: str = Field()
    object_: GitRefPropObject = Field(alias="object")


class GitRefPropObject(GitHubModel):
    """GitRefPropObject"""

    type: str = Field()
    sha: str = Field(min_length=40, max_length=40, description="SHA for the reference")
    url: str = Field()


model_rebuild(GitRef)
model_rebuild(GitRefPropObject)

__all__ = (
    "GitRef",
    "GitRefPropObject",
)