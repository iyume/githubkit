"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0400 import EnterpriseWebhooksType
from .group_0401 import SimpleInstallationType
from .group_0403 import RepositoryWebhooksType
from .group_0404 import SimpleUserWebhooksType
from .group_0114 import CustomPropertyValueType
from .group_0402 import OrganizationSimpleWebhooksType


class WebhookCustomPropertyValuesUpdatedType(TypedDict):
    """Custom property values updated event"""

    action: Literal["updated"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    repository: RepositoryWebhooksType
    organization: OrganizationSimpleWebhooksType
    sender: NotRequired[SimpleUserWebhooksType]
    new_property_values: List[CustomPropertyValueType]
    old_property_values: List[CustomPropertyValueType]


__all__ = ("WebhookCustomPropertyValuesUpdatedType",)