"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0045 import MarketplaceListingPlanType


class UserMarketplacePurchaseType(TypedDict):
    """User Marketplace Purchase

    User Marketplace Purchase
    """

    billing_cycle: str
    next_billing_date: Union[datetime, None]
    unit_count: Union[int, None]
    on_free_trial: bool
    free_trial_ends_on: Union[datetime, None]
    updated_at: Union[datetime, None]
    account: MarketplaceAccountType
    plan: MarketplaceListingPlanType


class MarketplaceAccountType(TypedDict):
    """Marketplace Account"""

    url: str
    id: int
    type: str
    node_id: NotRequired[str]
    login: str
    email: NotRequired[Union[str, None]]
    organization_billing_email: NotRequired[Union[str, None]]


__all__ = (
    "UserMarketplacePurchaseType",
    "MarketplaceAccountType",
)
