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


class WebhookSponsorshipEdited(GitHubModel):
    """sponsorship edited event"""

    action: Literal["edited"] = Field()
    changes: WebhookSponsorshipEditedPropChanges = Field()
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
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    repository: Missing[RepositoryWebhooks] = Field(
        default=UNSET,
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )
    sponsorship: WebhookSponsorshipEditedPropSponsorship = Field()


class WebhookSponsorshipEditedPropChanges(GitHubModel):
    """WebhookSponsorshipEditedPropChanges"""

    privacy_level: Missing[WebhookSponsorshipEditedPropChangesPropPrivacyLevel] = Field(
        default=UNSET
    )


class WebhookSponsorshipEditedPropChangesPropPrivacyLevel(GitHubModel):
    """WebhookSponsorshipEditedPropChangesPropPrivacyLevel"""

    from_: str = Field(
        alias="from",
        description="The `edited` event types include the details about the change when someone edits a sponsorship to change the privacy.",
    )


class WebhookSponsorshipEditedPropSponsorship(GitHubModel):
    """WebhookSponsorshipEditedPropSponsorship"""

    created_at: str = Field()
    maintainer: Missing[WebhookSponsorshipEditedPropSponsorshipPropMaintainer] = Field(
        default=UNSET
    )
    node_id: str = Field()
    privacy_level: str = Field()
    sponsor: Union[WebhookSponsorshipEditedPropSponsorshipPropSponsor, None] = Field(
        title="User"
    )
    sponsorable: Union[
        WebhookSponsorshipEditedPropSponsorshipPropSponsorable, None
    ] = Field(title="User")
    tier: WebhookSponsorshipEditedPropSponsorshipPropTier = Field(
        title="Sponsorship Tier",
        description="The `tier_changed` and `pending_tier_change` will include the original tier before the change or pending change. For more information, see the pending tier change payload.",
    )


class WebhookSponsorshipEditedPropSponsorshipPropMaintainer(GitHubModel):
    """WebhookSponsorshipEditedPropSponsorshipPropMaintainer"""

    avatar_url: Missing[str] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    login: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookSponsorshipEditedPropSponsorshipPropSponsor(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookSponsorshipEditedPropSponsorshipPropSponsorable(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookSponsorshipEditedPropSponsorshipPropTier(GitHubModel):
    """Sponsorship Tier

    The `tier_changed` and `pending_tier_change` will include the original tier
    before the change or pending change. For more information, see the pending tier
    change payload.
    """

    created_at: str = Field()
    description: str = Field()
    is_custom_ammount: Missing[bool] = Field(default=UNSET)
    is_custom_amount: Missing[bool] = Field(default=UNSET)
    is_one_time: bool = Field()
    monthly_price_in_cents: int = Field()
    monthly_price_in_dollars: int = Field()
    name: str = Field()
    node_id: str = Field()


model_rebuild(WebhookSponsorshipEdited)
model_rebuild(WebhookSponsorshipEditedPropChanges)
model_rebuild(WebhookSponsorshipEditedPropChangesPropPrivacyLevel)
model_rebuild(WebhookSponsorshipEditedPropSponsorship)
model_rebuild(WebhookSponsorshipEditedPropSponsorshipPropMaintainer)
model_rebuild(WebhookSponsorshipEditedPropSponsorshipPropSponsor)
model_rebuild(WebhookSponsorshipEditedPropSponsorshipPropSponsorable)
model_rebuild(WebhookSponsorshipEditedPropSponsorshipPropTier)

__all__ = (
    "WebhookSponsorshipEdited",
    "WebhookSponsorshipEditedPropChanges",
    "WebhookSponsorshipEditedPropChangesPropPrivacyLevel",
    "WebhookSponsorshipEditedPropSponsorship",
    "WebhookSponsorshipEditedPropSponsorshipPropMaintainer",
    "WebhookSponsorshipEditedPropSponsorshipPropSponsor",
    "WebhookSponsorshipEditedPropSponsorshipPropSponsorable",
    "WebhookSponsorshipEditedPropSponsorshipPropTier",
)
