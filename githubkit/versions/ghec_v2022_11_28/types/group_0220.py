"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict, NotRequired

from .group_0221 import (
    ProtectedBranchPropRequiredPullRequestReviewsPropDismissalRestrictionsType,
    ProtectedBranchPropRequiredPullRequestReviewsPropBypassPullRequestAllowancesType,
)


class ProtectedBranchPropRequiredPullRequestReviewsType(TypedDict):
    """ProtectedBranchPropRequiredPullRequestReviews"""

    url: str
    dismiss_stale_reviews: NotRequired[bool]
    require_code_owner_reviews: NotRequired[bool]
    required_approving_review_count: NotRequired[int]
    require_last_push_approval: NotRequired[bool]
    dismissal_restrictions: NotRequired[
        ProtectedBranchPropRequiredPullRequestReviewsPropDismissalRestrictionsType
    ]
    bypass_pull_request_allowances: NotRequired[
        ProtectedBranchPropRequiredPullRequestReviewsPropBypassPullRequestAllowancesType
    ]


__all__ = ("ProtectedBranchPropRequiredPullRequestReviewsType",)
