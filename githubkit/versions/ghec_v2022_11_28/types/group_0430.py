"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0112 import OrgCustomPropertyType
from .group_0390 import EnterpriseWebhooksType
from .group_0391 import SimpleInstallationType
from .group_0394 import SimpleUserWebhooksType
from .group_0392 import OrganizationSimpleWebhooksType


class WebhookCustomPropertyCreatedType(TypedDict):
    """custom property created event"""

    action: Literal["created"]
    definition: OrgCustomPropertyType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: OrganizationSimpleWebhooksType
    sender: NotRequired[SimpleUserWebhooksType]


__all__ = ("WebhookCustomPropertyCreatedType",)
