"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0178 import Verification


class GitTag(GitHubModel):
    """Git Tag

    Metadata for a Git tag
    """

    node_id: str = Field()
    tag: str = Field(description="Name of the tag")
    sha: str = Field()
    url: str = Field(description="URL for the tag")
    message: str = Field(description="Message describing the purpose of the tag")
    tagger: GitTagPropTagger = Field()
    object_: GitTagPropObject = Field(alias="object")
    verification: Missing[Verification] = Field(default=UNSET, title="Verification")


class GitTagPropTagger(GitHubModel):
    """GitTagPropTagger"""

    date: str = Field()
    email: str = Field()
    name: str = Field()


class GitTagPropObject(GitHubModel):
    """GitTagPropObject"""

    sha: str = Field()
    type: str = Field()
    url: str = Field()


model_rebuild(GitTag)
model_rebuild(GitTagPropTagger)
model_rebuild(GitTagPropObject)

__all__ = (
    "GitTag",
    "GitTagPropTagger",
    "GitTagPropObject",
)
