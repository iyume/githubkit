"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict

from .group_0173 import SimpleCommitType


class MergeGroupType(TypedDict):
    """Merge Group

    A group of pull requests that the merge queue has grouped together to be merged.
    """

    head_sha: str
    head_ref: str
    base_sha: str
    base_ref: str
    head_commit: SimpleCommitType


__all__ = ("MergeGroupType",)
