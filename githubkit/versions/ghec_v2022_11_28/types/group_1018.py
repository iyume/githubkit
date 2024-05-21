"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict, NotRequired

from .group_0007 import WebhookConfigType


class ReposOwnerRepoHooksHookIdPatchBodyType(TypedDict):
    """ReposOwnerRepoHooksHookIdPatchBody"""

    config: NotRequired[WebhookConfigType]
    events: NotRequired[List[str]]
    add_events: NotRequired[List[str]]
    remove_events: NotRequired[List[str]]
    active: NotRequired[bool]


__all__ = ("ReposOwnerRepoHooksHookIdPatchBodyType",)