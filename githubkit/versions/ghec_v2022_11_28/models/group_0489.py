"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0409 import WebhooksWorkflow
from .group_0400 import EnterpriseWebhooks
from .group_0401 import SimpleInstallation
from .group_0403 import RepositoryWebhooks
from .group_0404 import SimpleUserWebhooks
from .group_0402 import OrganizationSimpleWebhooks


class WebhookDeploymentCreated(GitHubModel):
    """deployment created event"""

    action: Literal["created"] = Field()
    deployment: WebhookDeploymentCreatedPropDeployment = Field(
        title="Deployment",
        description="The [deployment](https://docs.github.com/enterprise-cloud@latest//rest/deployments/deployments#list-deployments).",
    )
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/enterprise-cloud@latest//admin/overview/about-enterprise-accounts)."\n',
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
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )
    workflow: Union[WebhooksWorkflow, None] = Field(title="Workflow")
    workflow_run: Union[WebhookDeploymentCreatedPropWorkflowRun, None] = Field(
        title="Deployment Workflow Run"
    )


class WebhookDeploymentCreatedPropDeployment(GitHubModel):
    """Deployment

    The [deployment](https://docs.github.com/enterprise-
    cloud@latest//rest/deployments/deployments#list-deployments).
    """

    created_at: str = Field()
    creator: Union[WebhookDeploymentCreatedPropDeploymentPropCreator, None] = Field(
        title="User"
    )
    description: Union[str, None] = Field()
    environment: str = Field()
    id: int = Field()
    node_id: str = Field()
    original_environment: str = Field()
    payload: Union[WebhookDeploymentCreatedPropDeploymentPropPayloadOneof0, str] = (
        Field()
    )
    performed_via_github_app: Missing[
        Union[WebhookDeploymentCreatedPropDeploymentPropPerformedViaGithubApp, None]
    ] = Field(
        default=UNSET,
        title="App",
        description="GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.",
    )
    production_environment: Missing[bool] = Field(default=UNSET)
    ref: str = Field()
    repository_url: str = Field()
    sha: str = Field()
    statuses_url: str = Field()
    task: str = Field()
    transient_environment: Missing[bool] = Field(default=UNSET)
    updated_at: str = Field()
    url: str = Field()


class WebhookDeploymentCreatedPropDeploymentPropCreator(GitHubModel):
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


class WebhookDeploymentCreatedPropDeploymentPropPayloadOneof0(GitHubModel):
    """WebhookDeploymentCreatedPropDeploymentPropPayloadOneof0"""


class WebhookDeploymentCreatedPropDeploymentPropPerformedViaGithubApp(GitHubModel):
    """App

    GitHub apps are a new way to extend GitHub. They can be installed directly on
    organizations and user accounts and granted access to specific repositories.
    They come with granular permissions and built-in webhooks. GitHub apps are first
    class actors within GitHub.
    """

    created_at: Union[datetime, None] = Field()
    description: Union[str, None] = Field()
    events: Missing[
        List[
            Literal[
                "branch_protection_rule",
                "check_run",
                "check_suite",
                "code_scanning_alert",
                "commit_comment",
                "content_reference",
                "create",
                "delete",
                "deployment",
                "deployment_review",
                "deployment_status",
                "deploy_key",
                "discussion",
                "discussion_comment",
                "fork",
                "gollum",
                "issues",
                "issue_comment",
                "label",
                "member",
                "membership",
                "milestone",
                "organization",
                "org_block",
                "page_build",
                "project",
                "project_card",
                "project_column",
                "public",
                "pull_request",
                "pull_request_review",
                "pull_request_review_comment",
                "push",
                "registry_package",
                "release",
                "repository",
                "repository_dispatch",
                "secret_scanning_alert",
                "star",
                "status",
                "team",
                "team_add",
                "watch",
                "workflow_dispatch",
                "workflow_run",
                "workflow_job",
                "pull_request_review_thread",
                "merge_queue_entry",
                "secret_scanning_alert_location",
                "merge_group",
            ]
        ]
    ] = Field(default=UNSET, description="The list of events for the GitHub app")
    external_url: Union[str, None] = Field()
    html_url: str = Field()
    id: Union[int, None] = Field(description="Unique identifier of the GitHub app")
    name: str = Field(description="The name of the GitHub app")
    node_id: str = Field()
    owner: Union[
        WebhookDeploymentCreatedPropDeploymentPropPerformedViaGithubAppPropOwner, None
    ] = Field(title="User")
    permissions: Missing[
        WebhookDeploymentCreatedPropDeploymentPropPerformedViaGithubAppPropPermissions
    ] = Field(default=UNSET, description="The set of permissions for the GitHub app")
    slug: Missing[str] = Field(
        default=UNSET, description="The slug name of the GitHub app"
    )
    updated_at: Union[datetime, None] = Field()


class WebhookDeploymentCreatedPropDeploymentPropPerformedViaGithubAppPropOwner(
    GitHubModel
):
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


class WebhookDeploymentCreatedPropDeploymentPropPerformedViaGithubAppPropPermissions(
    GitHubModel
):
    """WebhookDeploymentCreatedPropDeploymentPropPerformedViaGithubAppPropPermissions

    The set of permissions for the GitHub app
    """

    actions: Missing[Literal["read", "write"]] = Field(default=UNSET)
    administration: Missing[Literal["read", "write"]] = Field(default=UNSET)
    checks: Missing[Literal["read", "write"]] = Field(default=UNSET)
    content_references: Missing[Literal["read", "write"]] = Field(default=UNSET)
    contents: Missing[Literal["read", "write"]] = Field(default=UNSET)
    deployments: Missing[Literal["read", "write"]] = Field(default=UNSET)
    discussions: Missing[Literal["read", "write"]] = Field(default=UNSET)
    emails: Missing[Literal["read", "write"]] = Field(default=UNSET)
    environments: Missing[Literal["read", "write"]] = Field(default=UNSET)
    issues: Missing[Literal["read", "write"]] = Field(default=UNSET)
    keys: Missing[Literal["read", "write"]] = Field(default=UNSET)
    members: Missing[Literal["read", "write"]] = Field(default=UNSET)
    metadata: Missing[Literal["read", "write"]] = Field(default=UNSET)
    organization_administration: Missing[Literal["read", "write"]] = Field(
        default=UNSET
    )
    organization_hooks: Missing[Literal["read", "write"]] = Field(default=UNSET)
    organization_packages: Missing[Literal["read", "write"]] = Field(default=UNSET)
    organization_plan: Missing[Literal["read", "write"]] = Field(default=UNSET)
    organization_projects: Missing[Literal["read", "write"]] = Field(default=UNSET)
    organization_secrets: Missing[Literal["read", "write"]] = Field(default=UNSET)
    organization_self_hosted_runners: Missing[Literal["read", "write"]] = Field(
        default=UNSET
    )
    organization_user_blocking: Missing[Literal["read", "write"]] = Field(default=UNSET)
    packages: Missing[Literal["read", "write"]] = Field(default=UNSET)
    pages: Missing[Literal["read", "write"]] = Field(default=UNSET)
    pull_requests: Missing[Literal["read", "write"]] = Field(default=UNSET)
    repository_hooks: Missing[Literal["read", "write"]] = Field(default=UNSET)
    repository_projects: Missing[Literal["read", "write"]] = Field(default=UNSET)
    secret_scanning_alerts: Missing[Literal["read", "write"]] = Field(default=UNSET)
    secrets: Missing[Literal["read", "write"]] = Field(default=UNSET)
    security_events: Missing[Literal["read", "write"]] = Field(default=UNSET)
    security_scanning_alert: Missing[Literal["read", "write"]] = Field(default=UNSET)
    single_file: Missing[Literal["read", "write"]] = Field(default=UNSET)
    statuses: Missing[Literal["read", "write"]] = Field(default=UNSET)
    team_discussions: Missing[Literal["read", "write"]] = Field(default=UNSET)
    vulnerability_alerts: Missing[Literal["read", "write"]] = Field(default=UNSET)
    workflows: Missing[Literal["read", "write"]] = Field(default=UNSET)


class WebhookDeploymentCreatedPropWorkflowRun(GitHubModel):
    """Deployment Workflow Run"""

    actor: Union[WebhookDeploymentCreatedPropWorkflowRunPropActor, None] = Field(
        title="User"
    )
    artifacts_url: Missing[str] = Field(default=UNSET)
    cancel_url: Missing[str] = Field(default=UNSET)
    check_suite_id: int = Field()
    check_suite_node_id: str = Field()
    check_suite_url: Missing[str] = Field(default=UNSET)
    conclusion: Union[
        None,
        Literal[
            "success",
            "failure",
            "neutral",
            "cancelled",
            "timed_out",
            "action_required",
            "stale",
        ],
    ] = Field()
    created_at: datetime = Field()
    display_title: str = Field()
    event: str = Field()
    head_branch: str = Field()
    head_commit: Missing[None] = Field(default=UNSET)
    head_repository: Missing[
        WebhookDeploymentCreatedPropWorkflowRunPropHeadRepository
    ] = Field(default=UNSET)
    head_sha: str = Field()
    html_url: str = Field()
    id: int = Field()
    jobs_url: Missing[str] = Field(default=UNSET)
    logs_url: Missing[str] = Field(default=UNSET)
    name: str = Field()
    node_id: str = Field()
    path: str = Field()
    previous_attempt_url: Missing[None] = Field(default=UNSET)
    pull_requests: List[
        WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItems
    ] = Field()
    referenced_workflows: Missing[
        Union[
            List[WebhookDeploymentCreatedPropWorkflowRunPropReferencedWorkflowsItems],
            None,
        ]
    ] = Field(default=UNSET)
    repository: Missing[WebhookDeploymentCreatedPropWorkflowRunPropRepository] = Field(
        default=UNSET
    )
    rerun_url: Missing[str] = Field(default=UNSET)
    run_attempt: int = Field()
    run_number: int = Field()
    run_started_at: datetime = Field()
    status: Literal[
        "requested", "in_progress", "completed", "queued", "waiting", "pending"
    ] = Field()
    triggering_actor: Missing[
        Union[WebhookDeploymentCreatedPropWorkflowRunPropTriggeringActor, None]
    ] = Field(default=UNSET, title="User")
    updated_at: datetime = Field()
    url: str = Field()
    workflow_id: int = Field()
    workflow_url: Missing[str] = Field(default=UNSET)


class WebhookDeploymentCreatedPropWorkflowRunPropActor(GitHubModel):
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


class WebhookDeploymentCreatedPropWorkflowRunPropReferencedWorkflowsItems(GitHubModel):
    """WebhookDeploymentCreatedPropWorkflowRunPropReferencedWorkflowsItems"""

    path: str = Field()
    ref: Missing[str] = Field(default=UNSET)
    sha: str = Field()


class WebhookDeploymentCreatedPropWorkflowRunPropTriggeringActor(GitHubModel):
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


class WebhookDeploymentCreatedPropWorkflowRunPropHeadRepository(GitHubModel):
    """WebhookDeploymentCreatedPropWorkflowRunPropHeadRepository"""

    archive_url: Missing[str] = Field(default=UNSET)
    assignees_url: Missing[str] = Field(default=UNSET)
    blobs_url: Missing[str] = Field(default=UNSET)
    branches_url: Missing[str] = Field(default=UNSET)
    collaborators_url: Missing[str] = Field(default=UNSET)
    comments_url: Missing[str] = Field(default=UNSET)
    commits_url: Missing[str] = Field(default=UNSET)
    compare_url: Missing[str] = Field(default=UNSET)
    contents_url: Missing[str] = Field(default=UNSET)
    contributors_url: Missing[str] = Field(default=UNSET)
    deployments_url: Missing[str] = Field(default=UNSET)
    description: Missing[None] = Field(default=UNSET)
    downloads_url: Missing[str] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    fork: Missing[bool] = Field(default=UNSET)
    forks_url: Missing[str] = Field(default=UNSET)
    full_name: Missing[str] = Field(default=UNSET)
    git_commits_url: Missing[str] = Field(default=UNSET)
    git_refs_url: Missing[str] = Field(default=UNSET)
    git_tags_url: Missing[str] = Field(default=UNSET)
    hooks_url: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    issue_comment_url: Missing[str] = Field(default=UNSET)
    issue_events_url: Missing[str] = Field(default=UNSET)
    issues_url: Missing[str] = Field(default=UNSET)
    keys_url: Missing[str] = Field(default=UNSET)
    labels_url: Missing[str] = Field(default=UNSET)
    languages_url: Missing[str] = Field(default=UNSET)
    merges_url: Missing[str] = Field(default=UNSET)
    milestones_url: Missing[str] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    notifications_url: Missing[str] = Field(default=UNSET)
    owner: Missing[
        WebhookDeploymentCreatedPropWorkflowRunPropHeadRepositoryPropOwner
    ] = Field(default=UNSET)
    private: Missing[bool] = Field(default=UNSET)
    pulls_url: Missing[str] = Field(default=UNSET)
    releases_url: Missing[str] = Field(default=UNSET)
    stargazers_url: Missing[str] = Field(default=UNSET)
    statuses_url: Missing[str] = Field(default=UNSET)
    subscribers_url: Missing[str] = Field(default=UNSET)
    subscription_url: Missing[str] = Field(default=UNSET)
    tags_url: Missing[str] = Field(default=UNSET)
    teams_url: Missing[str] = Field(default=UNSET)
    trees_url: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookDeploymentCreatedPropWorkflowRunPropHeadRepositoryPropOwner(GitHubModel):
    """WebhookDeploymentCreatedPropWorkflowRunPropHeadRepositoryPropOwner"""

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


class WebhookDeploymentCreatedPropWorkflowRunPropRepository(GitHubModel):
    """WebhookDeploymentCreatedPropWorkflowRunPropRepository"""

    archive_url: Missing[str] = Field(default=UNSET)
    assignees_url: Missing[str] = Field(default=UNSET)
    blobs_url: Missing[str] = Field(default=UNSET)
    branches_url: Missing[str] = Field(default=UNSET)
    collaborators_url: Missing[str] = Field(default=UNSET)
    comments_url: Missing[str] = Field(default=UNSET)
    commits_url: Missing[str] = Field(default=UNSET)
    compare_url: Missing[str] = Field(default=UNSET)
    contents_url: Missing[str] = Field(default=UNSET)
    contributors_url: Missing[str] = Field(default=UNSET)
    deployments_url: Missing[str] = Field(default=UNSET)
    description: Missing[None] = Field(default=UNSET)
    downloads_url: Missing[str] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    fork: Missing[bool] = Field(default=UNSET)
    forks_url: Missing[str] = Field(default=UNSET)
    full_name: Missing[str] = Field(default=UNSET)
    git_commits_url: Missing[str] = Field(default=UNSET)
    git_refs_url: Missing[str] = Field(default=UNSET)
    git_tags_url: Missing[str] = Field(default=UNSET)
    hooks_url: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    issue_comment_url: Missing[str] = Field(default=UNSET)
    issue_events_url: Missing[str] = Field(default=UNSET)
    issues_url: Missing[str] = Field(default=UNSET)
    keys_url: Missing[str] = Field(default=UNSET)
    labels_url: Missing[str] = Field(default=UNSET)
    languages_url: Missing[str] = Field(default=UNSET)
    merges_url: Missing[str] = Field(default=UNSET)
    milestones_url: Missing[str] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    notifications_url: Missing[str] = Field(default=UNSET)
    owner: Missing[WebhookDeploymentCreatedPropWorkflowRunPropRepositoryPropOwner] = (
        Field(default=UNSET)
    )
    private: Missing[bool] = Field(default=UNSET)
    pulls_url: Missing[str] = Field(default=UNSET)
    releases_url: Missing[str] = Field(default=UNSET)
    stargazers_url: Missing[str] = Field(default=UNSET)
    statuses_url: Missing[str] = Field(default=UNSET)
    subscribers_url: Missing[str] = Field(default=UNSET)
    subscription_url: Missing[str] = Field(default=UNSET)
    tags_url: Missing[str] = Field(default=UNSET)
    teams_url: Missing[str] = Field(default=UNSET)
    trees_url: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookDeploymentCreatedPropWorkflowRunPropRepositoryPropOwner(GitHubModel):
    """WebhookDeploymentCreatedPropWorkflowRunPropRepositoryPropOwner"""

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


class WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItems(GitHubModel):
    """Check Run Pull Request"""

    base: WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropBase = Field()
    head: WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropHead = Field()
    id: int = Field()
    number: int = Field()
    url: str = Field()


class WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropBase(GitHubModel):
    """WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropBase"""

    ref: str = Field()
    repo: WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropBasePropRepo = Field(
        title="Repo Ref"
    )
    sha: str = Field()


class WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropBasePropRepo(
    GitHubModel
):
    """Repo Ref"""

    id: int = Field()
    name: str = Field()
    url: str = Field()


class WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropHead(GitHubModel):
    """WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropHead"""

    ref: str = Field()
    repo: WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepo = Field(
        title="Repo Ref"
    )
    sha: str = Field()


class WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepo(
    GitHubModel
):
    """Repo Ref"""

    id: int = Field()
    name: str = Field()
    url: str = Field()


model_rebuild(WebhookDeploymentCreated)
model_rebuild(WebhookDeploymentCreatedPropDeployment)
model_rebuild(WebhookDeploymentCreatedPropDeploymentPropCreator)
model_rebuild(WebhookDeploymentCreatedPropDeploymentPropPayloadOneof0)
model_rebuild(WebhookDeploymentCreatedPropDeploymentPropPerformedViaGithubApp)
model_rebuild(WebhookDeploymentCreatedPropDeploymentPropPerformedViaGithubAppPropOwner)
model_rebuild(
    WebhookDeploymentCreatedPropDeploymentPropPerformedViaGithubAppPropPermissions
)
model_rebuild(WebhookDeploymentCreatedPropWorkflowRun)
model_rebuild(WebhookDeploymentCreatedPropWorkflowRunPropActor)
model_rebuild(WebhookDeploymentCreatedPropWorkflowRunPropReferencedWorkflowsItems)
model_rebuild(WebhookDeploymentCreatedPropWorkflowRunPropTriggeringActor)
model_rebuild(WebhookDeploymentCreatedPropWorkflowRunPropHeadRepository)
model_rebuild(WebhookDeploymentCreatedPropWorkflowRunPropHeadRepositoryPropOwner)
model_rebuild(WebhookDeploymentCreatedPropWorkflowRunPropRepository)
model_rebuild(WebhookDeploymentCreatedPropWorkflowRunPropRepositoryPropOwner)
model_rebuild(WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItems)
model_rebuild(WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropBase)
model_rebuild(
    WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropBasePropRepo
)
model_rebuild(WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropHead)
model_rebuild(
    WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepo
)

__all__ = (
    "WebhookDeploymentCreated",
    "WebhookDeploymentCreatedPropDeployment",
    "WebhookDeploymentCreatedPropDeploymentPropCreator",
    "WebhookDeploymentCreatedPropDeploymentPropPayloadOneof0",
    "WebhookDeploymentCreatedPropDeploymentPropPerformedViaGithubApp",
    "WebhookDeploymentCreatedPropDeploymentPropPerformedViaGithubAppPropOwner",
    "WebhookDeploymentCreatedPropDeploymentPropPerformedViaGithubAppPropPermissions",
    "WebhookDeploymentCreatedPropWorkflowRun",
    "WebhookDeploymentCreatedPropWorkflowRunPropActor",
    "WebhookDeploymentCreatedPropWorkflowRunPropReferencedWorkflowsItems",
    "WebhookDeploymentCreatedPropWorkflowRunPropTriggeringActor",
    "WebhookDeploymentCreatedPropWorkflowRunPropHeadRepository",
    "WebhookDeploymentCreatedPropWorkflowRunPropHeadRepositoryPropOwner",
    "WebhookDeploymentCreatedPropWorkflowRunPropRepository",
    "WebhookDeploymentCreatedPropWorkflowRunPropRepositoryPropOwner",
    "WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItems",
    "WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropBase",
    "WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropBasePropRepo",
    "WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropHead",
    "WebhookDeploymentCreatedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepo",
)