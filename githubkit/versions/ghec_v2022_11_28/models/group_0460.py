"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0401 import SimpleInstallation
from .group_0403 import RepositoryWebhooks
from .group_0404 import SimpleUserWebhooks
from .group_0402 import OrganizationSimpleWebhooks
from .group_0407 import CheckRunWithSimpleCheckSuite


class WebhookCheckRunRequestedAction(GitHubModel):
    """Check Run Requested Action Event"""

    action: Literal["requested_action"] = Field()
    check_run: CheckRunWithSimpleCheckSuite = Field(
        title="CheckRun",
        description="A check performed on the code of a given code change",
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/enterprise-cloud@latest//apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    requested_action: Missing[WebhookCheckRunRequestedActionPropRequestedAction] = (
        Field(default=UNSET, description="The action requested by the user.")
    )
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


class WebhookCheckRunRequestedActionPropRequestedAction(GitHubModel):
    """WebhookCheckRunRequestedActionPropRequestedAction

    The action requested by the user.
    """

    identifier: Missing[str] = Field(
        default=UNSET,
        description="The integrator reference of the action requested by the user.",
    )


model_rebuild(WebhookCheckRunRequestedAction)
model_rebuild(WebhookCheckRunRequestedActionPropRequestedAction)

__all__ = (
    "WebhookCheckRunRequestedAction",
    "WebhookCheckRunRequestedActionPropRequestedAction",
)