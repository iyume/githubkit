"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing_extensions import TypedDict

from .group_0801 import (
    WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropBaseType,
    WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropHeadType,
)


class WebhookWorkflowRunCompletedPropWorkflowRunMergedPullRequestsType(TypedDict):
    """WebhookWorkflowRunCompletedPropWorkflowRunMergedPullRequests"""

    base: WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropBaseType
    head: WebhookWorkflowRunCompletedPropWorkflowRunAllof0PropPullRequestsItemsPropHeadType
    id: float
    number: float
    url: str


__all__ = ("WebhookWorkflowRunCompletedPropWorkflowRunMergedPullRequestsType",)
