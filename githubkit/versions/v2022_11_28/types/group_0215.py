"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired


class ContentFileType(TypedDict):
    """Content File

    Content File
    """

    type: Literal["file"]
    encoding: str
    size: int
    name: str
    path: str
    content: str
    sha: str
    url: str
    git_url: Union[str, None]
    html_url: Union[str, None]
    download_url: Union[str, None]
    links: ContentFilePropLinksType
    target: NotRequired[str]
    submodule_git_url: NotRequired[str]


class ContentFilePropLinksType(TypedDict):
    """ContentFilePropLinks"""

    git: Union[str, None]
    html: Union[str, None]
    self_: str


__all__ = (
    "ContentFileType",
    "ContentFilePropLinksType",
)