"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0005 import IntegrationType


class WebhookIssueCommentCreatedPropCommentType(TypedDict):
    """issue comment

    The [comment](https://docs.github.com/rest/issues/comments#get-an-issue-comment)
    itself.
    """

    author_association: Literal[
        "COLLABORATOR",
        "CONTRIBUTOR",
        "FIRST_TIMER",
        "FIRST_TIME_CONTRIBUTOR",
        "MANNEQUIN",
        "MEMBER",
        "NONE",
        "OWNER",
    ]
    body: str
    created_at: datetime
    html_url: str
    id: int
    issue_url: str
    node_id: str
    performed_via_github_app: Union[None, IntegrationType]
    reactions: WebhookIssueCommentCreatedPropCommentPropReactionsType
    updated_at: datetime
    url: str
    user: Union[WebhookIssueCommentCreatedPropCommentPropUserType, None]


class WebhookIssueCommentCreatedPropCommentPropReactionsType(TypedDict):
    """Reactions"""

    plus_one: int
    minus_one: int
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class WebhookIssueCommentCreatedPropCommentPropUserType(TypedDict):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]


__all__ = (
    "WebhookIssueCommentCreatedPropCommentType",
    "WebhookIssueCommentCreatedPropCommentPropReactionsType",
    "WebhookIssueCommentCreatedPropCommentPropUserType",
)
