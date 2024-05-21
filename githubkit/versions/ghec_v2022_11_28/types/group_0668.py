"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0400 import EnterpriseWebhooksType
from .group_0401 import SimpleInstallationType
from .group_0403 import RepositoryWebhooksType
from .group_0404 import SimpleUserWebhooksType
from .group_0438 import PullRequestWebhookType
from .group_0402 import OrganizationSimpleWebhooksType


class WebhookPullRequestEditedType(TypedDict):
    """pull_request edited event"""

    action: Literal["edited"]
    changes: WebhookPullRequestEditedPropChangesType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    number: int
    organization: NotRequired[OrganizationSimpleWebhooksType]
    pull_request: PullRequestWebhookType
    repository: RepositoryWebhooksType
    sender: NotRequired[SimpleUserWebhooksType]


class WebhookPullRequestEditedPropChangesType(TypedDict):
    """WebhookPullRequestEditedPropChanges

    The changes to the comment if the action was `edited`.
    """

    base: NotRequired[WebhookPullRequestEditedPropChangesPropBaseType]
    body: NotRequired[WebhookPullRequestEditedPropChangesPropBodyType]
    title: NotRequired[WebhookPullRequestEditedPropChangesPropTitleType]


class WebhookPullRequestEditedPropChangesPropBodyType(TypedDict):
    """WebhookPullRequestEditedPropChangesPropBody"""

    from_: str


class WebhookPullRequestEditedPropChangesPropTitleType(TypedDict):
    """WebhookPullRequestEditedPropChangesPropTitle"""

    from_: str


class WebhookPullRequestEditedPropChangesPropBaseType(TypedDict):
    """WebhookPullRequestEditedPropChangesPropBase"""

    ref: WebhookPullRequestEditedPropChangesPropBasePropRefType
    sha: WebhookPullRequestEditedPropChangesPropBasePropShaType


class WebhookPullRequestEditedPropChangesPropBasePropRefType(TypedDict):
    """WebhookPullRequestEditedPropChangesPropBasePropRef"""

    from_: str


class WebhookPullRequestEditedPropChangesPropBasePropShaType(TypedDict):
    """WebhookPullRequestEditedPropChangesPropBasePropSha"""

    from_: str


__all__ = (
    "WebhookPullRequestEditedType",
    "WebhookPullRequestEditedPropChangesType",
    "WebhookPullRequestEditedPropChangesPropBodyType",
    "WebhookPullRequestEditedPropChangesPropTitleType",
    "WebhookPullRequestEditedPropChangesPropBaseType",
    "WebhookPullRequestEditedPropChangesPropBasePropRefType",
    "WebhookPullRequestEditedPropChangesPropBasePropShaType",
)