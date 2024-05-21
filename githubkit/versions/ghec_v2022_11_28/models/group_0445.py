"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class WebhooksAlert(GitHubModel):
    """Repository Vulnerability Alert Alert

    The security alert of the vulnerable dependency.
    """

    affected_package_name: str = Field()
    affected_range: str = Field()
    created_at: str = Field()
    dismiss_reason: Missing[str] = Field(default=UNSET)
    dismissed_at: Missing[str] = Field(default=UNSET)
    dismisser: Missing[Union[WebhooksAlertPropDismisser, None]] = Field(
        default=UNSET, title="User"
    )
    external_identifier: str = Field()
    external_reference: Union[str, None] = Field()
    fix_reason: Missing[str] = Field(default=UNSET)
    fixed_at: Missing[datetime] = Field(default=UNSET)
    fixed_in: Missing[str] = Field(default=UNSET)
    ghsa_id: str = Field()
    id: int = Field()
    node_id: str = Field()
    number: int = Field()
    severity: str = Field()
    state: Literal["open"] = Field()


class WebhooksAlertPropDismisser(GitHubModel):
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


model_rebuild(WebhooksAlert)
model_rebuild(WebhooksAlertPropDismisser)

__all__ = (
    "WebhooksAlert",
    "WebhooksAlertPropDismisser",
)