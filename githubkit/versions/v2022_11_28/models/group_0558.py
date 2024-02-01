"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild

from .group_0355 import EnterpriseWebhooks
from .group_0356 import SimpleInstallation
from .group_0358 import RepositoryWebhooks
from .group_0359 import SimpleUserWebhooks
from .group_0357 import OrganizationSimpleWebhooks


class WebhookMarketplacePurchaseChanged(GitHubModel):
    """marketplace_purchase changed event"""

    action: Literal["changed"] = Field()
    effective_date: str = Field()
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts)."\n',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    marketplace_purchase: WebhookMarketplacePurchaseChangedPropMarketplacePurchase = (
        Field()
    )
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    previous_marketplace_purchase: Missing[
        WebhookMarketplacePurchaseChangedPropPreviousMarketplacePurchase
    ] = Field(default=UNSET, title="Marketplace Purchase")
    repository: Missing[RepositoryWebhooks] = Field(
        default=UNSET,
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


class WebhookMarketplacePurchaseChangedPropMarketplacePurchase(GitHubModel):
    """WebhookMarketplacePurchaseChangedPropMarketplacePurchase"""

    account: WebhookMarketplacePurchaseChangedPropMarketplacePurchaseMergedAccount = (
        Field()
    )
    billing_cycle: str = Field()
    free_trial_ends_on: Union[Union[str, None], None] = Field()
    next_billing_date: Union[Union[str, None], None] = Field()
    on_free_trial: bool = Field()
    plan: WebhookMarketplacePurchaseChangedPropMarketplacePurchaseMergedPlan = Field()
    unit_count: int = Field()


class WebhookMarketplacePurchaseChangedPropMarketplacePurchaseMergedAccount(
    GitHubModel
):
    """WebhookMarketplacePurchaseChangedPropMarketplacePurchaseMergedAccount"""

    id: int = Field()
    login: str = Field()
    node_id: str = Field()
    organization_billing_email: Union[Union[str, None], None] = Field()
    type: str = Field()


class WebhookMarketplacePurchaseChangedPropMarketplacePurchaseMergedPlan(GitHubModel):
    """WebhookMarketplacePurchaseChangedPropMarketplacePurchaseMergedPlan"""

    bullets: List[str] = Field()
    description: str = Field()
    has_free_trial: bool = Field()
    id: int = Field()
    monthly_price_in_cents: int = Field()
    name: str = Field()
    price_model: Literal["FREE", "FLAT_RATE", "PER_UNIT"] = Field()
    unit_name: Union[Union[str, None], None] = Field()
    yearly_price_in_cents: int = Field()


class WebhookMarketplacePurchaseChangedPropPreviousMarketplacePurchase(GitHubModel):
    """Marketplace Purchase"""

    account: WebhookMarketplacePurchaseChangedPropPreviousMarketplacePurchasePropAccount = (
        Field()
    )
    billing_cycle: str = Field()
    free_trial_ends_on: Union[str, None] = Field()
    next_billing_date: Missing[Union[str, None]] = Field(default=UNSET)
    on_free_trial: Union[bool, None] = Field()
    plan: WebhookMarketplacePurchaseChangedPropPreviousMarketplacePurchasePropPlan = (
        Field()
    )
    unit_count: int = Field()


class WebhookMarketplacePurchaseChangedPropPreviousMarketplacePurchasePropAccount(
    GitHubModel
):
    """WebhookMarketplacePurchaseChangedPropPreviousMarketplacePurchasePropAccount"""

    id: int = Field()
    login: str = Field()
    node_id: str = Field()
    organization_billing_email: Union[str, None] = Field()
    type: str = Field()


class WebhookMarketplacePurchaseChangedPropPreviousMarketplacePurchasePropPlan(
    GitHubModel
):
    """WebhookMarketplacePurchaseChangedPropPreviousMarketplacePurchasePropPlan"""

    bullets: List[str] = Field()
    description: str = Field()
    has_free_trial: bool = Field()
    id: int = Field()
    monthly_price_in_cents: int = Field()
    name: str = Field()
    price_model: Literal["FREE", "FLAT_RATE", "PER_UNIT"] = Field()
    unit_name: Union[str, None] = Field()
    yearly_price_in_cents: int = Field()


model_rebuild(WebhookMarketplacePurchaseChanged)
model_rebuild(WebhookMarketplacePurchaseChangedPropMarketplacePurchase)
model_rebuild(WebhookMarketplacePurchaseChangedPropMarketplacePurchaseMergedAccount)
model_rebuild(WebhookMarketplacePurchaseChangedPropMarketplacePurchaseMergedPlan)
model_rebuild(WebhookMarketplacePurchaseChangedPropPreviousMarketplacePurchase)
model_rebuild(
    WebhookMarketplacePurchaseChangedPropPreviousMarketplacePurchasePropAccount
)
model_rebuild(WebhookMarketplacePurchaseChangedPropPreviousMarketplacePurchasePropPlan)

__all__ = (
    "WebhookMarketplacePurchaseChanged",
    "WebhookMarketplacePurchaseChangedPropMarketplacePurchase",
    "WebhookMarketplacePurchaseChangedPropMarketplacePurchaseMergedAccount",
    "WebhookMarketplacePurchaseChangedPropMarketplacePurchaseMergedPlan",
    "WebhookMarketplacePurchaseChangedPropPreviousMarketplacePurchase",
    "WebhookMarketplacePurchaseChangedPropPreviousMarketplacePurchasePropAccount",
    "WebhookMarketplacePurchaseChangedPropPreviousMarketplacePurchasePropPlan",
)
