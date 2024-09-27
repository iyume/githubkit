"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_1020 import ReposOwnerRepoPagesPutBodyPropSourceAnyof1Type


class ReposOwnerRepoPagesPutBodyAnyof1Type(TypedDict):
    """ReposOwnerRepoPagesPutBodyAnyof1"""

    cname: NotRequired[Union[str, None]]
    https_enforced: NotRequired[bool]
    build_type: NotRequired[Literal["legacy", "workflow"]]
    source: Union[
        Literal["gh-pages", "master", "master /docs"],
        ReposOwnerRepoPagesPutBodyPropSourceAnyof1Type,
    ]


__all__ = ("ReposOwnerRepoPagesPutBodyAnyof1Type",)
