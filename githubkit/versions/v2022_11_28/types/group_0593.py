"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0390 import WebhooksUserType
from .group_0378 import EnterpriseWebhooksType
from .group_0379 import SimpleInstallationType
from .group_0381 import RepositoryWebhooksType
from .group_0382 import SimpleUserWebhooksType
from .group_0380 import OrganizationSimpleWebhooksType


class WebhookOrganizationMemberInvitedType(TypedDict):
    """organization member_invited event"""

    action: Literal["member_invited"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    invitation: WebhookOrganizationMemberInvitedPropInvitationType
    organization: OrganizationSimpleWebhooksType
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserWebhooksType
    user: NotRequired[Union[WebhooksUserType, None]]


class WebhookOrganizationMemberInvitedPropInvitationType(TypedDict):
    """WebhookOrganizationMemberInvitedPropInvitation

    The invitation for the user or email if the action is `member_invited`.
    """

    created_at: datetime
    email: Union[str, None]
    failed_at: Union[datetime, None]
    failed_reason: Union[str, None]
    id: float
    invitation_teams_url: str
    inviter: Union[WebhookOrganizationMemberInvitedPropInvitationPropInviterType, None]
    login: Union[str, None]
    node_id: str
    role: str
    team_count: float
    invitation_source: NotRequired[str]


class WebhookOrganizationMemberInvitedPropInvitationPropInviterType(TypedDict):
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
    "WebhookOrganizationMemberInvitedType",
    "WebhookOrganizationMemberInvitedPropInvitationType",
    "WebhookOrganizationMemberInvitedPropInvitationPropInviterType",
)
