"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0415 import EnterpriseWebhooksType
from .group_0416 import SimpleInstallationType
from .group_0418 import RepositoryWebhooksType
from .group_0419 import SimpleUserWebhooksType
from .group_0417 import OrganizationSimpleWebhooksType
from .group_0442 import WebhooksMarketplacePurchaseType
from .group_0443 import WebhooksPreviousMarketplacePurchaseType


class WebhookMarketplacePurchaseCancelledType(TypedDict):
    """marketplace_purchase cancelled event"""

    action: Literal["cancelled"]
    effective_date: str
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    marketplace_purchase: WebhooksMarketplacePurchaseType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    previous_marketplace_purchase: NotRequired[WebhooksPreviousMarketplacePurchaseType]
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserWebhooksType


__all__ = ("WebhookMarketplacePurchaseCancelledType",)
