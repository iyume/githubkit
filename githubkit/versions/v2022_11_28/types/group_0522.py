"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0357 import EnterpriseWebhooksType
from .group_0358 import SimpleInstallationType
from .group_0360 import RepositoryWebhooksType
from .group_0361 import SimpleUserWebhooksType
from .group_0359 import OrganizationSimpleWebhooksType


class WebhookMemberEditedType(TypedDict):
    """member edited event"""

    action: Literal["edited"]
    changes: WebhookMemberEditedPropChangesType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    member: Union[WebhookMemberEditedPropMemberType, None]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


class WebhookMemberEditedPropMemberType(TypedDict):
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


class WebhookMemberEditedPropChangesType(TypedDict):
    """WebhookMemberEditedPropChanges

    The changes to the collaborator permissions
    """

    old_permission: NotRequired[WebhookMemberEditedPropChangesPropOldPermissionType]
    permission: NotRequired[WebhookMemberEditedPropChangesPropPermissionType]


class WebhookMemberEditedPropChangesPropOldPermissionType(TypedDict):
    """WebhookMemberEditedPropChangesPropOldPermission"""

    from_: str


class WebhookMemberEditedPropChangesPropPermissionType(TypedDict):
    """WebhookMemberEditedPropChangesPropPermission"""

    from_: NotRequired[Union[str, None]]
    to: NotRequired[Union[str, None]]


__all__ = (
    "WebhookMemberEditedType",
    "WebhookMemberEditedPropMemberType",
    "WebhookMemberEditedPropChangesType",
    "WebhookMemberEditedPropChangesPropOldPermissionType",
    "WebhookMemberEditedPropChangesPropPermissionType",
)
