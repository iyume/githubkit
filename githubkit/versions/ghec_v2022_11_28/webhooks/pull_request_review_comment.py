"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from typing import Dict, Type, Union
from typing_extensions import Annotated, TypeAlias

from pydantic import Field

from githubkit.compat import GitHubModel

from ..models import (
    WebhookPullRequestReviewCommentEdited,
    WebhookPullRequestReviewCommentCreated,
    WebhookPullRequestReviewCommentDeleted,
)

Event: TypeAlias = Annotated[
    Union[
        WebhookPullRequestReviewCommentCreated,
        WebhookPullRequestReviewCommentDeleted,
        WebhookPullRequestReviewCommentEdited,
    ],
    Field(discriminator="action"),
]

PullRequestReviewCommentEvent: TypeAlias = Event

action_types: Dict[str, Type[GitHubModel]] = {
    "created": WebhookPullRequestReviewCommentCreated,
    "deleted": WebhookPullRequestReviewCommentDeleted,
    "edited": WebhookPullRequestReviewCommentEdited,
}

pull_request_review_comment_action_types = action_types

__all__ = (
    "Event",
    "PullRequestReviewCommentEvent",
    "action_types",
    "pull_request_review_comment_action_types",
)