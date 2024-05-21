"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired


class ReposOwnerRepoPagesPostBodyPropSourceType(TypedDict):
    """ReposOwnerRepoPagesPostBodyPropSource

    The source branch and directory used to publish your Pages site.
    """

    branch: str
    path: NotRequired[Literal["/", "/docs"]]


__all__ = ("ReposOwnerRepoPagesPostBodyPropSourceType",)