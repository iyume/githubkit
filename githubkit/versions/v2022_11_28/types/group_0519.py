"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0357 import EnterpriseWebhooksType
from .group_0358 import SimpleInstallationType
from .group_0360 import RepositoryWebhooksType
from .group_0361 import SimpleUserWebhooksType
from .group_0359 import OrganizationSimpleWebhooksType


class WebhookMarketplacePurchasePendingChangeCancelledType(TypedDict):
    """marketplace_purchase pending_change_cancelled event"""

    action: Literal["pending_change_cancelled"]
    effective_date: str
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    marketplace_purchase: (
        WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchaseType
    )
    organization: NotRequired[OrganizationSimpleWebhooksType]
    previous_marketplace_purchase: NotRequired[
        WebhookMarketplacePurchasePendingChangeCancelledPropPreviousMarketplacePurchaseType
    ]
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserWebhooksType


class WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchaseType(
    TypedDict
):
    """Marketplace Purchase"""

    account: WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchasePropAccountType
    billing_cycle: str
    free_trial_ends_on: None
    next_billing_date: Union[str, None]
    on_free_trial: bool
    plan: WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchasePropPlanType
    unit_count: int


class WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchasePropAccountType(
    TypedDict
):
    """WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchasePropAccou
    nt
    """

    id: int
    login: str
    node_id: str
    organization_billing_email: Union[str, None]
    type: str


class WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchasePropPlanType(
    TypedDict
):
    """WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchasePropPlan"""

    bullets: List[str]
    description: str
    has_free_trial: bool
    id: int
    monthly_price_in_cents: int
    name: str
    price_model: Literal["FREE", "FLAT_RATE", "PER_UNIT"]
    unit_name: Union[str, None]
    yearly_price_in_cents: int


class WebhookMarketplacePurchasePendingChangeCancelledPropPreviousMarketplacePurchaseType(
    TypedDict
):
    """Marketplace Purchase"""

    account: WebhookMarketplacePurchasePendingChangeCancelledPropPreviousMarketplacePurchasePropAccountType
    billing_cycle: str
    free_trial_ends_on: None
    next_billing_date: NotRequired[Union[str, None]]
    on_free_trial: bool
    plan: WebhookMarketplacePurchasePendingChangeCancelledPropPreviousMarketplacePurchasePropPlanType
    unit_count: int


class WebhookMarketplacePurchasePendingChangeCancelledPropPreviousMarketplacePurchasePropAccountType(
    TypedDict
):
    """WebhookMarketplacePurchasePendingChangeCancelledPropPreviousMarketplacePurchaseP
    ropAccount
    """

    id: int
    login: str
    node_id: str
    organization_billing_email: Union[str, None]
    type: str


class WebhookMarketplacePurchasePendingChangeCancelledPropPreviousMarketplacePurchasePropPlanType(
    TypedDict
):
    """WebhookMarketplacePurchasePendingChangeCancelledPropPreviousMarketplacePurchaseP
    ropPlan
    """

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
    "WebhookMarketplacePurchasePendingChangeCancelledType",
    "WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchaseType",
    "WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchasePropAccountType",
    "WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchasePropPlanType",
    "WebhookMarketplacePurchasePendingChangeCancelledPropPreviousMarketplacePurchaseType",
    "WebhookMarketplacePurchasePendingChangeCancelledPropPreviousMarketplacePurchasePropAccountType",
    "WebhookMarketplacePurchasePendingChangeCancelledPropPreviousMarketplacePurchasePropPlanType",
)
