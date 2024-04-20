"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0357 import EnterpriseWebhooksType
from .group_0358 import SimpleInstallationType
from .group_0360 import RepositoryWebhooksType
from .group_0361 import SimpleUserWebhooksType
from .group_0359 import OrganizationSimpleWebhooksType


class WebhookPullRequestReviewRequestedOneof0Type(TypedDict):
    """WebhookPullRequestReviewRequestedOneof0"""

    action: Literal["review_requested"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    number: int
    organization: NotRequired[OrganizationSimpleWebhooksType]
    pull_request: WebhookPullRequestReviewRequestedOneof0PropPullRequestType
    repository: RepositoryWebhooksType
    requested_reviewer: Union[
        WebhookPullRequestReviewRequestedOneof0PropRequestedReviewerType, None
    ]
    sender: SimpleUserWebhooksType


class WebhookPullRequestReviewRequestedOneof0PropRequestedReviewerType(TypedDict):
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
    type: NotRequired[Literal["Bot", "User", "Organization", "Mannequin"]]
    url: NotRequired[str]


class WebhookPullRequestReviewRequestedOneof0PropPullRequestType(TypedDict):
    """Pull Request"""

    links: WebhookPullRequestReviewRequestedOneof0PropPullRequestPropLinksType
    active_lock_reason: Union[
        None, Literal["resolved", "off-topic", "too heated", "spam"]
    ]
    additions: NotRequired[int]
    assignee: Union[
        WebhookPullRequestReviewRequestedOneof0PropPullRequestPropAssigneeType, None
    ]
    assignees: List[
        Union[
            WebhookPullRequestReviewRequestedOneof0PropPullRequestPropAssigneesItemsType,
            None,
        ]
    ]
    author_association: Literal[
        "COLLABORATOR",
        "CONTRIBUTOR",
        "FIRST_TIMER",
        "FIRST_TIME_CONTRIBUTOR",
        "MANNEQUIN",
        "MEMBER",
        "NONE",
        "OWNER",
    ]
    auto_merge: Union[
        WebhookPullRequestReviewRequestedOneof0PropPullRequestPropAutoMergeType, None
    ]
    base: WebhookPullRequestReviewRequestedOneof0PropPullRequestPropBaseType
    body: Union[str, None]
    changed_files: NotRequired[int]
    closed_at: Union[datetime, None]
    comments: NotRequired[int]
    comments_url: str
    commits: NotRequired[int]
    commits_url: str
    created_at: datetime
    deletions: NotRequired[int]
    diff_url: str
    draft: bool
    head: WebhookPullRequestReviewRequestedOneof0PropPullRequestPropHeadType
    html_url: str
    id: int
    issue_url: str
    labels: List[
        WebhookPullRequestReviewRequestedOneof0PropPullRequestPropLabelsItemsType
    ]
    locked: bool
    maintainer_can_modify: NotRequired[bool]
    merge_commit_sha: Union[str, None]
    mergeable: NotRequired[Union[bool, None]]
    mergeable_state: NotRequired[str]
    merged: NotRequired[Union[bool, None]]
    merged_at: Union[datetime, None]
    merged_by: NotRequired[
        Union[
            WebhookPullRequestReviewRequestedOneof0PropPullRequestPropMergedByType, None
        ]
    ]
    milestone: Union[
        WebhookPullRequestReviewRequestedOneof0PropPullRequestPropMilestoneType, None
    ]
    node_id: str
    number: int
    patch_url: str
    rebaseable: NotRequired[Union[bool, None]]
    requested_reviewers: List[
        Union[
            WebhookPullRequestReviewRequestedOneof0PropPullRequestPropRequestedReviewersItemsOneof0Type,
            None,
            WebhookPullRequestReviewRequestedOneof0PropPullRequestPropRequestedReviewersItemsOneof1Type,
        ]
    ]
    requested_teams: List[
        WebhookPullRequestReviewRequestedOneof0PropPullRequestPropRequestedTeamsItemsType
    ]
    review_comment_url: str
    review_comments: NotRequired[int]
    review_comments_url: str
    state: Literal["open", "closed"]
    statuses_url: str
    title: str
    updated_at: datetime
    url: str
    user: Union[
        WebhookPullRequestReviewRequestedOneof0PropPullRequestPropUserType, None
    ]


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropAssigneeType(TypedDict):
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
    type: NotRequired[Literal["Bot", "User", "Organization", "Mannequin"]]
    url: NotRequired[str]


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropAssigneesItemsType(
    TypedDict
):
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
    type: NotRequired[Literal["Bot", "User", "Organization", "Mannequin"]]
    url: NotRequired[str]


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropAutoMergeType(
    TypedDict
):
    """PullRequestAutoMerge

    The status of auto merging a pull request.
    """

    commit_message: Union[str, None]
    commit_title: Union[str, None]
    enabled_by: Union[
        WebhookPullRequestReviewRequestedOneof0PropPullRequestPropAutoMergePropEnabledByType,
        None,
    ]
    merge_method: Literal["merge", "squash", "rebase"]


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropAutoMergePropEnabledByType(
    TypedDict
):
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


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropLabelsItemsType(
    TypedDict
):
    """Label"""

    color: str
    default: bool
    description: Union[str, None]
    id: int
    name: str
    node_id: str
    url: str


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropMergedByType(TypedDict):
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


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropMilestoneType(
    TypedDict
):
    """Milestone

    A collection of related issues and pull requests.
    """

    closed_at: Union[datetime, None]
    closed_issues: int
    created_at: datetime
    creator: Union[
        WebhookPullRequestReviewRequestedOneof0PropPullRequestPropMilestonePropCreatorType,
        None,
    ]
    description: Union[str, None]
    due_on: Union[datetime, None]
    html_url: str
    id: int
    labels_url: str
    node_id: str
    number: int
    open_issues: int
    state: Literal["open", "closed"]
    title: str
    updated_at: datetime
    url: str


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropMilestonePropCreatorType(
    TypedDict
):
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
    type: NotRequired[Literal["Bot", "User", "Organization", "Mannequin"]]
    url: NotRequired[str]


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropRequestedReviewersItemsOneof0Type(
    TypedDict
):
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


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropUserType(TypedDict):
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
    type: NotRequired[Literal["Bot", "User", "Organization", "Mannequin"]]
    url: NotRequired[str]


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropLinksType(TypedDict):
    """WebhookPullRequestReviewRequestedOneof0PropPullRequestPropLinks"""

    comments: (
        WebhookPullRequestReviewRequestedOneof0PropPullRequestPropLinksPropCommentsType
    )
    commits: (
        WebhookPullRequestReviewRequestedOneof0PropPullRequestPropLinksPropCommitsType
    )
    html: WebhookPullRequestReviewRequestedOneof0PropPullRequestPropLinksPropHtmlType
    issue: WebhookPullRequestReviewRequestedOneof0PropPullRequestPropLinksPropIssueType
    review_comment: WebhookPullRequestReviewRequestedOneof0PropPullRequestPropLinksPropReviewCommentType
    review_comments: WebhookPullRequestReviewRequestedOneof0PropPullRequestPropLinksPropReviewCommentsType
    self_: WebhookPullRequestReviewRequestedOneof0PropPullRequestPropLinksPropSelfType
    statuses: (
        WebhookPullRequestReviewRequestedOneof0PropPullRequestPropLinksPropStatusesType
    )


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropLinksPropCommentsType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropLinksPropCommitsType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropLinksPropHtmlType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropLinksPropIssueType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropLinksPropReviewCommentType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropLinksPropReviewCommentsType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropLinksPropSelfType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropLinksPropStatusesType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropBaseType(TypedDict):
    """WebhookPullRequestReviewRequestedOneof0PropPullRequestPropBase"""

    label: str
    ref: str
    repo: WebhookPullRequestReviewRequestedOneof0PropPullRequestPropBasePropRepoType
    sha: str
    user: Union[
        WebhookPullRequestReviewRequestedOneof0PropPullRequestPropBasePropUserType, None
    ]


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropBasePropUserType(
    TypedDict
):
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


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropBasePropRepoType(
    TypedDict
):
    """Repository

    A git repository
    """

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: Union[int, datetime]
    default_branch: str
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: str
    description: Union[str, None]
    disabled: NotRequired[bool]
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: Union[str, None]
    hooks_url: str
    html_url: str
    id: int
    is_template: NotRequired[bool]
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: Union[str, None]
    languages_url: str
    license_: Union[
        WebhookPullRequestReviewRequestedOneof0PropPullRequestPropBasePropRepoPropLicenseType,
        None,
    ]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merges_url: str
    milestones_url: str
    mirror_url: Union[str, None]
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: NotRequired[str]
    owner: Union[
        WebhookPullRequestReviewRequestedOneof0PropPullRequestPropBasePropRepoPropOwnerType,
        None,
    ]
    permissions: NotRequired[
        WebhookPullRequestReviewRequestedOneof0PropPullRequestPropBasePropRepoPropPermissionsType
    ]
    private: bool
    public: NotRequired[bool]
    pulls_url: str
    pushed_at: Union[int, datetime, None]
    releases_url: str
    role_name: NotRequired[Union[str, None]]
    size: int
    squash_merge_commit_message: NotRequired[
        Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]
    ]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    ssh_url: str
    stargazers: NotRequired[int]
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: List[str]
    trees_url: str
    updated_at: datetime
    url: str
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: NotRequired[bool]


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropBasePropRepoPropLicenseType(
    TypedDict
):
    """License"""

    key: str
    name: str
    node_id: str
    spdx_id: str
    url: Union[str, None]


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropBasePropRepoPropOwnerType(
    TypedDict
):
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


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropBasePropRepoPropPermissionsType(
    TypedDict
):
    """WebhookPullRequestReviewRequestedOneof0PropPullRequestPropBasePropRepoPropPermis
    sions
    """

    admin: bool
    maintain: NotRequired[bool]
    pull: bool
    push: bool
    triage: NotRequired[bool]


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropHeadType(TypedDict):
    """WebhookPullRequestReviewRequestedOneof0PropPullRequestPropHead"""

    label: str
    ref: str
    repo: WebhookPullRequestReviewRequestedOneof0PropPullRequestPropHeadPropRepoType
    sha: str
    user: Union[
        WebhookPullRequestReviewRequestedOneof0PropPullRequestPropHeadPropUserType, None
    ]


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropHeadPropUserType(
    TypedDict
):
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


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropHeadPropRepoType(
    TypedDict
):
    """Repository

    A git repository
    """

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: Union[int, datetime]
    default_branch: str
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: str
    description: Union[str, None]
    disabled: NotRequired[bool]
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: Union[str, None]
    hooks_url: str
    html_url: str
    id: int
    is_template: NotRequired[bool]
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: Union[str, None]
    languages_url: str
    license_: Union[
        WebhookPullRequestReviewRequestedOneof0PropPullRequestPropHeadPropRepoPropLicenseType,
        None,
    ]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merges_url: str
    milestones_url: str
    mirror_url: Union[str, None]
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: NotRequired[str]
    owner: Union[
        WebhookPullRequestReviewRequestedOneof0PropPullRequestPropHeadPropRepoPropOwnerType,
        None,
    ]
    permissions: NotRequired[
        WebhookPullRequestReviewRequestedOneof0PropPullRequestPropHeadPropRepoPropPermissionsType
    ]
    private: bool
    public: NotRequired[bool]
    pulls_url: str
    pushed_at: Union[int, datetime, None]
    releases_url: str
    role_name: NotRequired[Union[str, None]]
    size: int
    squash_merge_commit_message: NotRequired[
        Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]
    ]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    ssh_url: str
    stargazers: NotRequired[int]
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: List[str]
    trees_url: str
    updated_at: datetime
    url: str
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: NotRequired[bool]


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropHeadPropRepoPropLicenseType(
    TypedDict
):
    """License"""

    key: str
    name: str
    node_id: str
    spdx_id: str
    url: Union[str, None]


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropHeadPropRepoPropOwnerType(
    TypedDict
):
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


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropHeadPropRepoPropPermissionsType(
    TypedDict
):
    """WebhookPullRequestReviewRequestedOneof0PropPullRequestPropHeadPropRepoPropPermis
    sions
    """

    admin: bool
    maintain: NotRequired[bool]
    pull: bool
    push: bool
    triage: NotRequired[bool]


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropRequestedReviewersItemsOneof1Type(
    TypedDict
):
    """Team

    Groups of organization members that gives permissions on specified repositories.
    """

    deleted: NotRequired[bool]
    description: Union[str, None]
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    parent: NotRequired[
        Union[
            WebhookPullRequestReviewRequestedOneof0PropPullRequestPropRequestedReviewersItemsOneof1PropParentType,
            None,
        ]
    ]
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropRequestedReviewersItemsOneof1PropParentType(
    TypedDict
):
    """WebhookPullRequestReviewRequestedOneof0PropPullRequestPropRequestedReviewersItem
    sOneof1PropParent
    """

    description: Union[str, None]
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropRequestedTeamsItemsType(
    TypedDict
):
    """Team

    Groups of organization members that gives permissions on specified repositories.
    """

    deleted: NotRequired[bool]
    description: NotRequired[Union[str, None]]
    html_url: NotRequired[str]
    id: int
    members_url: NotRequired[str]
    name: str
    node_id: NotRequired[str]
    parent: NotRequired[
        Union[
            WebhookPullRequestReviewRequestedOneof0PropPullRequestPropRequestedTeamsItemsPropParentType,
            None,
        ]
    ]
    permission: NotRequired[str]
    privacy: NotRequired[Literal["open", "closed", "secret"]]
    repositories_url: NotRequired[str]
    slug: NotRequired[str]
    url: NotRequired[str]


class WebhookPullRequestReviewRequestedOneof0PropPullRequestPropRequestedTeamsItemsPropParentType(
    TypedDict
):
    """WebhookPullRequestReviewRequestedOneof0PropPullRequestPropRequestedTeamsItemsPro
    pParent
    """

    description: Union[str, None]
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


__all__ = (
    "WebhookPullRequestReviewRequestedOneof0Type",
    "WebhookPullRequestReviewRequestedOneof0PropRequestedReviewerType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropAssigneeType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropAssigneesItemsType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropAutoMergeType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropAutoMergePropEnabledByType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropLabelsItemsType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropMergedByType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropMilestoneType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropMilestonePropCreatorType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropRequestedReviewersItemsOneof0Type",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropUserType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropLinksType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropLinksPropCommentsType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropLinksPropCommitsType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropLinksPropHtmlType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropLinksPropIssueType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropLinksPropReviewCommentType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropLinksPropReviewCommentsType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropLinksPropSelfType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropLinksPropStatusesType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropBaseType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropBasePropUserType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropBasePropRepoType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropBasePropRepoPropLicenseType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropBasePropRepoPropOwnerType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropBasePropRepoPropPermissionsType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropHeadType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropHeadPropUserType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropHeadPropRepoType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropHeadPropRepoPropLicenseType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropHeadPropRepoPropOwnerType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropHeadPropRepoPropPermissionsType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropRequestedReviewersItemsOneof1Type",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropRequestedReviewersItemsOneof1PropParentType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropRequestedTeamsItemsType",
    "WebhookPullRequestReviewRequestedOneof0PropPullRequestPropRequestedTeamsItemsPropParentType",
)
