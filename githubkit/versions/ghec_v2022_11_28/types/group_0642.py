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
from .group_0434 import WebhooksProjectColumnType
from .group_0402 import OrganizationSimpleWebhooksType


class WebhookProjectColumnEditedType(TypedDict):
    """project_column edited event"""

    action: Literal["edited"]
    changes: WebhookProjectColumnEditedPropChangesType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    project_column: WebhooksProjectColumnType
    repository: NotRequired[RepositoryWebhooksType]
    sender: NotRequired[SimpleUserWebhooksType]


class WebhookProjectColumnEditedPropChangesType(TypedDict):
    """WebhookProjectColumnEditedPropChanges"""

    name: NotRequired[WebhookProjectColumnEditedPropChangesPropNameType]


class WebhookProjectColumnEditedPropChangesPropNameType(TypedDict):
    """WebhookProjectColumnEditedPropChangesPropName"""

    from_: str


__all__ = (
    "WebhookProjectColumnEditedType",
    "WebhookProjectColumnEditedPropChangesType",
    "WebhookProjectColumnEditedPropChangesPropNameType",
)