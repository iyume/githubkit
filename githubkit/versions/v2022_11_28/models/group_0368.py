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

from .group_0351 import EnterpriseWebhooks
from .group_0352 import SimpleInstallation
from .group_0354 import RepositoryWebhooks
from .group_0355 import SimpleUserWebhooks
from .group_0353 import OrganizationSimpleWebhooks


class WebhookBranchProtectionRuleEdited(GitHubModel):
    """branch protection rule edited event"""

    action: Literal["edited"] = Field()
    changes: Missing[WebhookBranchProtectionRuleEditedPropChanges] = Field(
        default=UNSET,
        description="If the action was `edited`, the changes to the rule.",
    )
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
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    rule: WebhookBranchProtectionRuleEditedPropRule = Field(
        title="branch protection rule",
        description="The branch protection rule. Includes a `name` and all the [branch protection settings](https://docs.github.com/github/administering-a-repository/defining-the-mergeability-of-pull-requests/about-protected-branches#about-branch-protection-settings) applied to branches that match the name. Binary settings are boolean. Multi-level configurations are one of `off`, `non_admins`, or `everyone`. Actor and build lists are arrays of strings.",
    )
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


class WebhookBranchProtectionRuleEditedPropRule(GitHubModel):
    """branch protection rule

    The branch protection rule. Includes a `name` and all the [branch protection
    settings](https://docs.github.com/github/administering-a-repository/defining-
    the-mergeability-of-pull-requests/about-protected-branches#about-branch-
    protection-settings) applied to branches that match the name. Binary settings
    are boolean. Multi-level configurations are one of `off`, `non_admins`, or
    `everyone`. Actor and build lists are arrays of strings.
    """

    admin_enforced: bool = Field()
    allow_deletions_enforcement_level: Literal[
        "off", "non_admins", "everyone"
    ] = Field()
    allow_force_pushes_enforcement_level: Literal[
        "off", "non_admins", "everyone"
    ] = Field()
    authorized_actor_names: List[str] = Field()
    authorized_actors_only: bool = Field()
    authorized_dismissal_actors_only: bool = Field()
    create_protected: Missing[bool] = Field(default=UNSET)
    created_at: datetime = Field()
    dismiss_stale_reviews_on_push: bool = Field()
    id: int = Field()
    ignore_approvals_from_contributors: bool = Field()
    linear_history_requirement_enforcement_level: Literal[
        "off", "non_admins", "everyone"
    ] = Field()
    merge_queue_enforcement_level: Literal["off", "non_admins", "everyone"] = Field()
    name: str = Field()
    pull_request_reviews_enforcement_level: Literal[
        "off", "non_admins", "everyone"
    ] = Field()
    repository_id: int = Field()
    require_code_owner_review: bool = Field()
    require_last_push_approval: Missing[bool] = Field(
        default=UNSET,
        description="Whether the most recent push must be approved by someone other than the person who pushed it",
    )
    required_approving_review_count: int = Field()
    required_conversation_resolution_level: Literal[
        "off", "non_admins", "everyone"
    ] = Field()
    required_deployments_enforcement_level: Literal[
        "off", "non_admins", "everyone"
    ] = Field()
    required_status_checks: List[str] = Field()
    required_status_checks_enforcement_level: Literal[
        "off", "non_admins", "everyone"
    ] = Field()
    signature_requirement_enforcement_level: Literal[
        "off", "non_admins", "everyone"
    ] = Field()
    strict_required_status_checks_policy: bool = Field()
    updated_at: datetime = Field()


class WebhookBranchProtectionRuleEditedPropChanges(GitHubModel):
    """WebhookBranchProtectionRuleEditedPropChanges

    If the action was `edited`, the changes to the rule.
    """

    admin_enforced: Missing[
        WebhookBranchProtectionRuleEditedPropChangesPropAdminEnforced
    ] = Field(default=UNSET)
    authorized_actor_names: Missing[
        WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorNames
    ] = Field(default=UNSET)
    authorized_actors_only: Missing[
        WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorsOnly
    ] = Field(default=UNSET)
    authorized_dismissal_actors_only: Missing[
        WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedDismissalActorsOnly
    ] = Field(default=UNSET)
    linear_history_requirement_enforcement_level: Missing[
        WebhookBranchProtectionRuleEditedPropChangesPropLinearHistoryRequirementEnforcementLevel
    ] = Field(default=UNSET)
    required_status_checks: Missing[
        WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecks
    ] = Field(default=UNSET)
    required_status_checks_enforcement_level: Missing[
        WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksEnforcementLevel
    ] = Field(default=UNSET)


class WebhookBranchProtectionRuleEditedPropChangesPropAdminEnforced(GitHubModel):
    """WebhookBranchProtectionRuleEditedPropChangesPropAdminEnforced"""

    from_: Union[bool, None] = Field(alias="from")


class WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorNames(GitHubModel):
    """WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorNames"""

    from_: List[str] = Field(alias="from")


class WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorsOnly(GitHubModel):
    """WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorsOnly"""

    from_: Union[bool, None] = Field(alias="from")


class WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedDismissalActorsOnly(
    GitHubModel
):
    """WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedDismissalActorsOnly"""

    from_: Union[bool, None] = Field(alias="from")


class WebhookBranchProtectionRuleEditedPropChangesPropLinearHistoryRequirementEnforcementLevel(
    GitHubModel
):
    """WebhookBranchProtectionRuleEditedPropChangesPropLinearHistoryRequirementEnforcem
    entLevel
    """

    from_: Literal["off", "non_admins", "everyone"] = Field(alias="from")


class WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecks(GitHubModel):
    """WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecks"""

    from_: List[str] = Field(alias="from")


class WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksEnforcementLevel(
    GitHubModel
):
    """WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksEnforcementL
    evel
    """

    from_: Literal["off", "non_admins", "everyone"] = Field(alias="from")


model_rebuild(WebhookBranchProtectionRuleEdited)
model_rebuild(WebhookBranchProtectionRuleEditedPropRule)
model_rebuild(WebhookBranchProtectionRuleEditedPropChanges)
model_rebuild(WebhookBranchProtectionRuleEditedPropChangesPropAdminEnforced)
model_rebuild(WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorNames)
model_rebuild(WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorsOnly)
model_rebuild(
    WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedDismissalActorsOnly
)
model_rebuild(
    WebhookBranchProtectionRuleEditedPropChangesPropLinearHistoryRequirementEnforcementLevel
)
model_rebuild(WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecks)
model_rebuild(
    WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksEnforcementLevel
)

__all__ = (
    "WebhookBranchProtectionRuleEdited",
    "WebhookBranchProtectionRuleEditedPropRule",
    "WebhookBranchProtectionRuleEditedPropChanges",
    "WebhookBranchProtectionRuleEditedPropChangesPropAdminEnforced",
    "WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorNames",
    "WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorsOnly",
    "WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedDismissalActorsOnly",
    "WebhookBranchProtectionRuleEditedPropChangesPropLinearHistoryRequirementEnforcementLevel",
    "WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecks",
    "WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksEnforcementLevel",
)