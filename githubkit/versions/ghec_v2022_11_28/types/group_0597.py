"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0412 import WebhooksUserType
from .group_0400 import EnterpriseWebhooksType
from .group_0401 import SimpleInstallationType
from .group_0403 import RepositoryWebhooksType
from .group_0404 import SimpleUserWebhooksType
from .group_0402 import OrganizationSimpleWebhooksType


class WebhookMemberAddedType(TypedDict):
    """member added event"""

    action: Literal["added"]
    changes: NotRequired[WebhookMemberAddedPropChangesType]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    member: Union[WebhooksUserType, None]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


class WebhookMemberAddedPropChangesType(TypedDict):
    """WebhookMemberAddedPropChanges"""

    permission: NotRequired[WebhookMemberAddedPropChangesPropPermissionType]
    role_name: NotRequired[WebhookMemberAddedPropChangesPropRoleNameType]


class WebhookMemberAddedPropChangesPropPermissionType(TypedDict):
    """WebhookMemberAddedPropChangesPropPermission

    This field is included for legacy purposes; use the `role_name` field instead.
    The `maintain`
    role is mapped to `write` and the `triage` role is mapped to `read`. To
    determine the role
    assigned to the collaborator, use the `role_name` field instead, which will
    provide the full
    role name, including custom roles.
    """

    to: Literal["write", "admin", "read"]


class WebhookMemberAddedPropChangesPropRoleNameType(TypedDict):
    """WebhookMemberAddedPropChangesPropRoleName

    The role assigned to the collaborator.
    """

    to: str


__all__ = (
    "WebhookMemberAddedType",
    "WebhookMemberAddedPropChangesType",
    "WebhookMemberAddedPropChangesPropPermissionType",
    "WebhookMemberAddedPropChangesPropRoleNameType",
)