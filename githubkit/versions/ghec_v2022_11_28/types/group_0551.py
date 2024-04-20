"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0390 import EnterpriseWebhooksType
from .group_0391 import SimpleInstallationType
from .group_0393 import RepositoryWebhooksType
from .group_0394 import SimpleUserWebhooksType
from .group_0392 import OrganizationSimpleWebhooksType


class WebhookMarketplacePurchasePendingChangeType(TypedDict):
    """marketplace_purchase pending_change event"""

    action: Literal["pending_change"]
    effective_date: str
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    marketplace_purchase: (
        WebhookMarketplacePurchasePendingChangePropMarketplacePurchaseType
    )
    organization: NotRequired[OrganizationSimpleWebhooksType]
    previous_marketplace_purchase: NotRequired[
        WebhookMarketplacePurchasePendingChangePropPreviousMarketplacePurchaseType
    ]
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserWebhooksType


class WebhookMarketplacePurchasePendingChangePropMarketplacePurchaseType(TypedDict):
    """Marketplace Purchase"""

    account: (
        WebhookMarketplacePurchasePendingChangePropMarketplacePurchasePropAccountType
    )
    billing_cycle: str
    free_trial_ends_on: Union[str, None]
    next_billing_date: Union[str, None]
    on_free_trial: bool
    plan: WebhookMarketplacePurchasePendingChangePropMarketplacePurchasePropPlanType
    unit_count: int


class WebhookMarketplacePurchasePendingChangePropMarketplacePurchasePropAccountType(
    TypedDict
):
    """WebhookMarketplacePurchasePendingChangePropMarketplacePurchasePropAccount"""

    id: int
    login: str
    node_id: str
    organization_billing_email: Union[str, None]
    type: str


class WebhookMarketplacePurchasePendingChangePropMarketplacePurchasePropPlanType(
    TypedDict
):
    """WebhookMarketplacePurchasePendingChangePropMarketplacePurchasePropPlan"""

    bullets: List[Union[str, None]]
    description: str
    has_free_trial: bool
    id: int
    monthly_price_in_cents: int
    name: str
    price_model: Literal["FREE", "FLAT_RATE", "PER_UNIT"]
    unit_name: Union[str, None]
    yearly_price_in_cents: int


class WebhookMarketplacePurchasePendingChangePropPreviousMarketplacePurchaseType(
    TypedDict
):
    """Marketplace Purchase"""

    account: WebhookMarketplacePurchasePendingChangePropPreviousMarketplacePurchasePropAccountType
    billing_cycle: str
    free_trial_ends_on: Union[str, None]
    next_billing_date: NotRequired[Union[str, None]]
    on_free_trial: bool
    plan: WebhookMarketplacePurchasePendingChangePropPreviousMarketplacePurchasePropPlanType
    unit_count: int


class WebhookMarketplacePurchasePendingChangePropPreviousMarketplacePurchasePropAccountType(
    TypedDict
):
    """WebhookMarketplacePurchasePendingChangePropPreviousMarketplacePurchasePropAccoun
    t
    """

    id: int
    login: str
    node_id: str
    organization_billing_email: Union[str, None]
    type: str


class WebhookMarketplacePurchasePendingChangePropPreviousMarketplacePurchasePropPlanType(
    TypedDict
):
    """WebhookMarketplacePurchasePendingChangePropPreviousMarketplacePurchasePropPlan"""

    bullets: List[str]
    description: str
    has_free_trial: bool
    id: int
    monthly_price_in_cents: int
    name: str
    price_model: Literal["FREE", "FLAT_RATE", "PER_UNIT"]
    unit_name: Union[str, None]
    yearly_price_in_cents: int


__all__ = (
    "WebhookMarketplacePurchasePendingChangeType",
    "WebhookMarketplacePurchasePendingChangePropMarketplacePurchaseType",
    "WebhookMarketplacePurchasePendingChangePropMarketplacePurchasePropAccountType",
    "WebhookMarketplacePurchasePendingChangePropMarketplacePurchasePropPlanType",
    "WebhookMarketplacePurchasePendingChangePropPreviousMarketplacePurchaseType",
    "WebhookMarketplacePurchasePendingChangePropPreviousMarketplacePurchasePropAccountType",
    "WebhookMarketplacePurchasePendingChangePropPreviousMarketplacePurchasePropPlanType",
)
