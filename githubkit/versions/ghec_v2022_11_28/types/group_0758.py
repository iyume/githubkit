"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0416 import SimpleInstallationType
from .group_0418 import RepositoryWebhooksType
from .group_0419 import SimpleUserWebhooksType
from .group_0417 import OrganizationSimpleWebhooksType
from .group_0464 import SecretScanningAlertWebhookType


class WebhookSecretScanningAlertLocationCreatedType(TypedDict):
    """Secret Scanning Alert Location Created Event"""

    action: Literal["created"]
    alert: SecretScanningAlertWebhookType
    installation: NotRequired[SimpleInstallationType]
    location: SecretScanningLocationType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


class SecretScanningLocationType(TypedDict):
    """SecretScanningLocation"""

    type: NotRequired[
        Literal[
            "commit",
            "wiki_commit",
            "issue_title",
            "issue_body",
            "issue_comment",
            "discussion_title",
            "discussion_body",
            "discussion_comment",
            "pull_request_title",
            "pull_request_body",
            "pull_request_comment",
            "pull_request_review",
            "pull_request_review_comment",
        ]
    ]
    details: NotRequired[
        Union[
            SecretScanningLocationCommitType,
            SecretScanningLocationWikiCommitType,
            SecretScanningLocationIssueTitleType,
            SecretScanningLocationIssueBodyType,
            SecretScanningLocationIssueCommentType,
            SecretScanningLocationDiscussionTitleType,
            SecretScanningLocationDiscussionBodyType,
            SecretScanningLocationDiscussionCommentType,
            SecretScanningLocationPullRequestTitleType,
            SecretScanningLocationPullRequestBodyType,
            SecretScanningLocationPullRequestCommentType,
            SecretScanningLocationPullRequestReviewType,
            SecretScanningLocationPullRequestReviewCommentType,
        ]
    ]


class SecretScanningLocationCommitType(TypedDict):
    """SecretScanningLocationCommit

    Represents a 'commit' secret scanning location type. This location type shows
    that a secret was detected inside a commit to a repository.
    """

    path: str
    start_line: float
    end_line: float
    start_column: float
    end_column: float
    blob_sha: str
    blob_url: str
    commit_sha: str
    commit_url: str


class SecretScanningLocationWikiCommitType(TypedDict):
    """SecretScanningLocationWikiCommit

    Represents a 'wiki_commit' secret scanning location type. This location type
    shows that a secret was detected inside a commit to a repository wiki.
    """

    path: str
    start_line: float
    end_line: float
    start_column: float
    end_column: float
    blob_sha: str
    page_url: str
    commit_sha: str
    commit_url: str


class SecretScanningLocationIssueTitleType(TypedDict):
    """SecretScanningLocationIssueTitle

    Represents an 'issue_title' secret scanning location type. This location type
    shows that a secret was detected in the title of an issue.
    """

    issue_title_url: str


class SecretScanningLocationIssueBodyType(TypedDict):
    """SecretScanningLocationIssueBody

    Represents an 'issue_body' secret scanning location type. This location type
    shows that a secret was detected in the body of an issue.
    """

    issue_body_url: str


class SecretScanningLocationIssueCommentType(TypedDict):
    """SecretScanningLocationIssueComment

    Represents an 'issue_comment' secret scanning location type. This location type
    shows that a secret was detected in a comment on an issue.
    """

    issue_comment_url: str


class SecretScanningLocationDiscussionTitleType(TypedDict):
    """SecretScanningLocationDiscussionTitle

    Represents a 'discussion_title' secret scanning location type. This location
    type shows that a secret was detected in the title of a discussion.
    """

    discussion_title_url: str


class SecretScanningLocationDiscussionBodyType(TypedDict):
    """SecretScanningLocationDiscussionBody

    Represents a 'discussion_body' secret scanning location type. This location type
    shows that a secret was detected in the body of a discussion.
    """

    discussion_body_url: str


class SecretScanningLocationDiscussionCommentType(TypedDict):
    """SecretScanningLocationDiscussionComment

    Represents a 'discussion_comment' secret scanning location type. This location
    type shows that a secret was detected in a comment on a discussion.
    """

    discussion_comment_url: str


class SecretScanningLocationPullRequestTitleType(TypedDict):
    """SecretScanningLocationPullRequestTitle

    Represents a 'pull_request_title' secret scanning location type. This location
    type shows that a secret was detected in the title of a pull request.
    """

    pull_request_title_url: str


class SecretScanningLocationPullRequestBodyType(TypedDict):
    """SecretScanningLocationPullRequestBody

    Represents a 'pull_request_body' secret scanning location type. This location
    type shows that a secret was detected in the body of a pull request.
    """

    pull_request_body_url: str


class SecretScanningLocationPullRequestCommentType(TypedDict):
    """SecretScanningLocationPullRequestComment

    Represents a 'pull_request_comment' secret scanning location type. This location
    type shows that a secret was detected in a comment on a pull request.
    """

    pull_request_comment_url: str


class SecretScanningLocationPullRequestReviewType(TypedDict):
    """SecretScanningLocationPullRequestReview

    Represents a 'pull_request_review' secret scanning location type. This location
    type shows that a secret was detected in a review on a pull request.
    """

    pull_request_review_url: str


class SecretScanningLocationPullRequestReviewCommentType(TypedDict):
    """SecretScanningLocationPullRequestReviewComment

    Represents a 'pull_request_review_comment' secret scanning location type. This
    location type shows that a secret was detected in a review comment on a pull
    request.
    """

    pull_request_review_comment_url: str


__all__ = (
    "WebhookSecretScanningAlertLocationCreatedType",
    "SecretScanningLocationType",
    "SecretScanningLocationCommitType",
    "SecretScanningLocationWikiCommitType",
    "SecretScanningLocationIssueTitleType",
    "SecretScanningLocationIssueBodyType",
    "SecretScanningLocationIssueCommentType",
    "SecretScanningLocationDiscussionTitleType",
    "SecretScanningLocationDiscussionBodyType",
    "SecretScanningLocationDiscussionCommentType",
    "SecretScanningLocationPullRequestTitleType",
    "SecretScanningLocationPullRequestBodyType",
    "SecretScanningLocationPullRequestCommentType",
    "SecretScanningLocationPullRequestReviewType",
    "SecretScanningLocationPullRequestReviewCommentType",
)
