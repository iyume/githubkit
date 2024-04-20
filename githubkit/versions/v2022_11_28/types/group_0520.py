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


class WebhookMarketplacePurchasePurchasedType(TypedDict):
    """marketplace_purchase purchased event"""

    action: Literal["purchased"]
    effective_date: str
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    marketplace_purchase: WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    previous_marketplace_purchase: NotRequired[
        WebhookMarketplacePurchasePurchasedPropPreviousMarketplacePurchaseType
    ]
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserWebhooksType


class WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseType(TypedDict):
    """Marketplace Purchase"""

    account: WebhookMarketplacePurchasePurchasedPropMarketplacePurchasePropAccountType
    billing_cycle: str
    free_trial_ends_on: Union[str, None]
    next_billing_date: Union[str, None]
    on_free_trial: bool
    plan: WebhookMarketplacePurchasePurchasedPropMarketplacePurchasePropPlanType
    unit_count: int


class WebhookMarketplacePurchasePurchasedPropMarketplacePurchasePropAccountType(
    TypedDict
):
    """WebhookMarketplacePurchasePurchasedPropMarketplacePurchasePropAccount"""

    id: int
    login: str
    node_id: str
    organization_billing_email: Union[str, None]
    type: str


class WebhookMarketplacePurchasePurchasedPropMarketplacePurchasePropPlanType(TypedDict):
    """WebhookMarketplacePurchasePurchasedPropMarketplacePurchasePropPlan"""

    bullets: List[Union[str, None]]
    description: str
    has_free_trial: bool
    id: int
    monthly_price_in_cents: int
    name: str
    price_model: Literal["FREE", "FLAT_RATE", "PER_UNIT"]
    unit_name: Union[str, None]
    yearly_price_in_cents: int


class WebhookMarketplacePurchasePurchasedPropPreviousMarketplacePurchaseType(TypedDict):
    """Marketplace Purchase"""

    account: WebhookMarketplacePurchasePurchasedPropPreviousMarketplacePurchasePropAccountType
    billing_cycle: str
    free_trial_ends_on: None
    next_billing_date: NotRequired[Union[str, None]]
    on_free_trial: bool
    plan: WebhookMarketplacePurchasePurchasedPropPreviousMarketplacePurchasePropPlanType
    unit_count: int


class WebhookMarketplacePurchasePurchasedPropPreviousMarketplacePurchasePropAccountType(
    TypedDict
):
    """WebhookMarketplacePurchasePurchasedPropPreviousMarketplacePurchasePropAccount"""

    id: int
    login: str
    node_id: str
    organization_billing_email: Union[str, None]
    type: str


class WebhookMarketplacePurchasePurchasedPropPreviousMarketplacePurchasePropPlanType(
    TypedDict
):
    """WebhookMarketplacePurchasePurchasedPropPreviousMarketplacePurchasePropPlan"""

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
    "WebhookMarketplacePurchasePurchasedType",
    "WebhookMarketplacePurchasePurchasedPropMarketplacePurchaseType",
    "WebhookMarketplacePurchasePurchasedPropMarketplacePurchasePropAccountType",
    "WebhookMarketplacePurchasePurchasedPropMarketplacePurchasePropPlanType",
    "WebhookMarketplacePurchasePurchasedPropPreviousMarketplacePurchaseType",
    "WebhookMarketplacePurchasePurchasedPropPreviousMarketplacePurchasePropAccountType",
    "WebhookMarketplacePurchasePurchasedPropPreviousMarketplacePurchasePropPlanType",
)
