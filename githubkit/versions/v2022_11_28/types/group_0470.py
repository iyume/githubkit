"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0378 import EnterpriseWebhooksType
from .group_0379 import SimpleInstallationType
from .group_0381 import RepositoryWebhooksType
from .group_0382 import SimpleUserWebhooksType
from .group_0389 import WebhooksWorkflowJobRunType
from .group_0380 import OrganizationSimpleWebhooksType
from .group_0388 import WebhooksApproverType, WebhooksReviewersItemsType


class WebhookDeploymentReviewApprovedType(TypedDict):
    """WebhookDeploymentReviewApproved"""

    action: Literal["approved"]
    approver: NotRequired[WebhooksApproverType]
    comment: NotRequired[str]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: OrganizationSimpleWebhooksType
    repository: RepositoryWebhooksType
    reviewers: NotRequired[List[WebhooksReviewersItemsType]]
    sender: SimpleUserWebhooksType
    since: str
    workflow_job_run: NotRequired[WebhooksWorkflowJobRunType]
    workflow_job_runs: NotRequired[
        List[WebhookDeploymentReviewApprovedPropWorkflowJobRunsItemsType]
    ]
    workflow_run: Union[WebhookDeploymentReviewApprovedPropWorkflowRunType, None]


class WebhookDeploymentReviewApprovedPropWorkflowJobRunsItemsType(TypedDict):
    """WebhookDeploymentReviewApprovedPropWorkflowJobRunsItems"""

    conclusion: NotRequired[None]
    created_at: NotRequired[str]
    environment: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    name: NotRequired[Union[str, None]]
    status: NotRequired[str]
    updated_at: NotRequired[str]


class WebhookDeploymentReviewApprovedPropWorkflowRunType(TypedDict):
    """Deployment Workflow Run"""

    actor: Union[WebhookDeploymentReviewApprovedPropWorkflowRunPropActorType, None]
    artifacts_url: NotRequired[str]
    cancel_url: NotRequired[str]
    check_suite_id: int
    check_suite_node_id: str
    check_suite_url: NotRequired[str]
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
    ]
    created_at: datetime
    display_title: str
    event: str
    head_branch: str
    head_commit: NotRequired[
        Union[WebhookDeploymentReviewApprovedPropWorkflowRunPropHeadCommitType, None]
    ]
    head_repository: NotRequired[
        WebhookDeploymentReviewApprovedPropWorkflowRunPropHeadRepositoryType
    ]
    head_sha: str
    html_url: str
    id: int
    jobs_url: NotRequired[str]
    logs_url: NotRequired[str]
    name: str
    node_id: str
    path: str
    previous_attempt_url: NotRequired[Union[str, None]]
    pull_requests: List[
        WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsType
    ]
    referenced_workflows: NotRequired[
        Union[
            List[
                WebhookDeploymentReviewApprovedPropWorkflowRunPropReferencedWorkflowsItemsType
            ],
            None,
        ]
    ]
    repository: NotRequired[
        WebhookDeploymentReviewApprovedPropWorkflowRunPropRepositoryType
    ]
    rerun_url: NotRequired[str]
    run_attempt: int
    run_number: int
    run_started_at: datetime
    status: Literal[
        "requested", "in_progress", "completed", "queued", "waiting", "pending"
    ]
    triggering_actor: Union[
        WebhookDeploymentReviewApprovedPropWorkflowRunPropTriggeringActorType, None
    ]
    updated_at: datetime
    url: str
    workflow_id: int
    workflow_url: NotRequired[str]


class WebhookDeploymentReviewApprovedPropWorkflowRunPropActorType(TypedDict):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]


class WebhookDeploymentReviewApprovedPropWorkflowRunPropHeadCommitType(TypedDict):
    """WebhookDeploymentReviewApprovedPropWorkflowRunPropHeadCommit"""


class WebhookDeploymentReviewApprovedPropWorkflowRunPropReferencedWorkflowsItemsType(
    TypedDict
):
    """WebhookDeploymentReviewApprovedPropWorkflowRunPropReferencedWorkflowsItems"""

    path: str
    ref: NotRequired[str]
    sha: str


class WebhookDeploymentReviewApprovedPropWorkflowRunPropTriggeringActorType(TypedDict):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]


class WebhookDeploymentReviewApprovedPropWorkflowRunPropHeadRepositoryType(TypedDict):
    """WebhookDeploymentReviewApprovedPropWorkflowRunPropHeadRepository"""

    archive_url: NotRequired[str]
    assignees_url: NotRequired[str]
    blobs_url: NotRequired[str]
    branches_url: NotRequired[str]
    collaborators_url: NotRequired[str]
    comments_url: NotRequired[str]
    commits_url: NotRequired[str]
    compare_url: NotRequired[str]
    contents_url: NotRequired[str]
    contributors_url: NotRequired[str]
    deployments_url: NotRequired[str]
    description: NotRequired[Union[str, None]]
    downloads_url: NotRequired[str]
    events_url: NotRequired[str]
    fork: NotRequired[bool]
    forks_url: NotRequired[str]
    full_name: NotRequired[str]
    git_commits_url: NotRequired[str]
    git_refs_url: NotRequired[str]
    git_tags_url: NotRequired[str]
    hooks_url: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    issue_comment_url: NotRequired[str]
    issue_events_url: NotRequired[str]
    issues_url: NotRequired[str]
    keys_url: NotRequired[str]
    labels_url: NotRequired[str]
    languages_url: NotRequired[str]
    merges_url: NotRequired[str]
    milestones_url: NotRequired[str]
    name: NotRequired[str]
    node_id: NotRequired[str]
    notifications_url: NotRequired[str]
    owner: NotRequired[
        WebhookDeploymentReviewApprovedPropWorkflowRunPropHeadRepositoryPropOwnerType
    ]
    private: NotRequired[bool]
    pulls_url: NotRequired[str]
    releases_url: NotRequired[str]
    stargazers_url: NotRequired[str]
    statuses_url: NotRequired[str]
    subscribers_url: NotRequired[str]
    subscription_url: NotRequired[str]
    tags_url: NotRequired[str]
    teams_url: NotRequired[str]
    trees_url: NotRequired[str]
    url: NotRequired[str]


class WebhookDeploymentReviewApprovedPropWorkflowRunPropHeadRepositoryPropOwnerType(
    TypedDict
):
    """WebhookDeploymentReviewApprovedPropWorkflowRunPropHeadRepositoryPropOwner"""

    avatar_url: NotRequired[str]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    login: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[str]
    url: NotRequired[str]


class WebhookDeploymentReviewApprovedPropWorkflowRunPropRepositoryType(TypedDict):
    """WebhookDeploymentReviewApprovedPropWorkflowRunPropRepository"""

    archive_url: NotRequired[str]
    assignees_url: NotRequired[str]
    blobs_url: NotRequired[str]
    branches_url: NotRequired[str]
    collaborators_url: NotRequired[str]
    comments_url: NotRequired[str]
    commits_url: NotRequired[str]
    compare_url: NotRequired[str]
    contents_url: NotRequired[str]
    contributors_url: NotRequired[str]
    deployments_url: NotRequired[str]
    description: NotRequired[Union[str, None]]
    downloads_url: NotRequired[str]
    events_url: NotRequired[str]
    fork: NotRequired[bool]
    forks_url: NotRequired[str]
    full_name: NotRequired[str]
    git_commits_url: NotRequired[str]
    git_refs_url: NotRequired[str]
    git_tags_url: NotRequired[str]
    hooks_url: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    issue_comment_url: NotRequired[str]
    issue_events_url: NotRequired[str]
    issues_url: NotRequired[str]
    keys_url: NotRequired[str]
    labels_url: NotRequired[str]
    languages_url: NotRequired[str]
    merges_url: NotRequired[str]
    milestones_url: NotRequired[str]
    name: NotRequired[str]
    node_id: NotRequired[str]
    notifications_url: NotRequired[str]
    owner: NotRequired[
        WebhookDeploymentReviewApprovedPropWorkflowRunPropRepositoryPropOwnerType
    ]
    private: NotRequired[bool]
    pulls_url: NotRequired[str]
    releases_url: NotRequired[str]
    stargazers_url: NotRequired[str]
    statuses_url: NotRequired[str]
    subscribers_url: NotRequired[str]
    subscription_url: NotRequired[str]
    tags_url: NotRequired[str]
    teams_url: NotRequired[str]
    trees_url: NotRequired[str]
    url: NotRequired[str]


class WebhookDeploymentReviewApprovedPropWorkflowRunPropRepositoryPropOwnerType(
    TypedDict
):
    """WebhookDeploymentReviewApprovedPropWorkflowRunPropRepositoryPropOwner"""

    avatar_url: NotRequired[str]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    login: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[str]
    url: NotRequired[str]


class WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsType(
    TypedDict
):
    """Check Run Pull Request"""

    base: (
        WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropBaseType
    )
    head: (
        WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropHeadType
    )
    id: int
    number: int
    url: str


class WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropBaseType(
    TypedDict
):
    """WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropBase"""

    ref: str
    repo: WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropBasePropRepoType
    sha: str


class WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropBasePropRepoType(
    TypedDict
):
    """Repo Ref"""

    id: int
    name: str
    url: str


class WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropHeadType(
    TypedDict
):
    """WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropHead"""

    ref: str
    repo: WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepoType
    sha: str


class WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepoType(
    TypedDict
):
    """Repo Ref"""

    id: int
    name: str
    url: str


__all__ = (
    "WebhookDeploymentReviewApprovedType",
    "WebhookDeploymentReviewApprovedPropWorkflowJobRunsItemsType",
    "WebhookDeploymentReviewApprovedPropWorkflowRunType",
    "WebhookDeploymentReviewApprovedPropWorkflowRunPropActorType",
    "WebhookDeploymentReviewApprovedPropWorkflowRunPropHeadCommitType",
    "WebhookDeploymentReviewApprovedPropWorkflowRunPropReferencedWorkflowsItemsType",
    "WebhookDeploymentReviewApprovedPropWorkflowRunPropTriggeringActorType",
    "WebhookDeploymentReviewApprovedPropWorkflowRunPropHeadRepositoryType",
    "WebhookDeploymentReviewApprovedPropWorkflowRunPropHeadRepositoryPropOwnerType",
    "WebhookDeploymentReviewApprovedPropWorkflowRunPropRepositoryType",
    "WebhookDeploymentReviewApprovedPropWorkflowRunPropRepositoryPropOwnerType",
    "WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsType",
    "WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropBaseType",
    "WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropBasePropRepoType",
    "WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropHeadType",
    "WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepoType",
)
