"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing_extensions import TypedDict, NotRequired


class ReposOwnerRepoNotificationsPutResponse202Type(TypedDict):
    """ReposOwnerRepoNotificationsPutResponse202"""

    message: NotRequired[str]
    url: NotRequired[str]


__all__ = ("ReposOwnerRepoNotificationsPutResponse202Type",)
