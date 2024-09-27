"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired


class DiffEntryType(TypedDict):
    """Diff Entry

    Diff Entry
    """

    sha: str
    filename: str
    status: Literal[
        "added", "removed", "modified", "renamed", "copied", "changed", "unchanged"
    ]
    additions: int
    deletions: int
    changes: int
    blob_url: Union[str, None]
    raw_url: Union[str, None]
    contents_url: str
    patch: NotRequired[str]
    previous_filename: NotRequired[str]


__all__ = ("DiffEntryType",)
