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

from .group_0029 import Team
from .group_0039 import Milestone
from .group_0228 import AutoMerge
from .group_0002 import SimpleUser
from .group_0231 import PullRequestSimplePropLinks
from .group_0230 import PullRequestSimplePropBase, PullRequestSimplePropHead


class PullRequestSimple(GitHubModel):
    """Pull Request Simple

    Pull Request Simple
    """

    url: str = Field()
    id: int = Field()
    node_id: str = Field()
    html_url: str = Field()
    diff_url: str = Field()
    patch_url: str = Field()
    issue_url: str = Field()
    commits_url: str = Field()
    review_comments_url: str = Field()
    review_comment_url: str = Field()
    comments_url: str = Field()
    statuses_url: str = Field()
    number: int = Field()
    state: str = Field()
    locked: bool = Field()
    title: str = Field()
    user: Union[None, SimpleUser] = Field()
    body: Union[str, None] = Field()
    labels: List[PullRequestSimplePropLabelsItems] = Field()
    milestone: Union[None, Milestone] = Field()
    active_lock_reason: Missing[Union[str, None]] = Field(default=UNSET)
    created_at: datetime = Field()
    updated_at: datetime = Field()
    closed_at: Union[datetime, None] = Field()
    merged_at: Union[datetime, None] = Field()
    merge_commit_sha: Union[str, None] = Field()
    assignee: Union[None, SimpleUser] = Field()
    assignees: Missing[Union[List[SimpleUser], None]] = Field(default=UNSET)
    requested_reviewers: Missing[Union[List[SimpleUser], None]] = Field(default=UNSET)
    requested_teams: Missing[Union[List[Team], None]] = Field(default=UNSET)
    head: PullRequestSimplePropHead = Field()
    base: PullRequestSimplePropBase = Field()
    links: PullRequestSimplePropLinks = Field(alias="_links")
    author_association: Literal[
        "COLLABORATOR",
        "CONTRIBUTOR",
        "FIRST_TIMER",
        "FIRST_TIME_CONTRIBUTOR",
        "MANNEQUIN",
        "MEMBER",
        "NONE",
        "OWNER",
    ] = Field(
        title="author_association",
        description="How the author is associated with the repository.",
    )
    auto_merge: Union[AutoMerge, None] = Field(
        title="Auto merge", description="The status of auto merging a pull request."
    )
    draft: Missing[bool] = Field(
        default=UNSET,
        description="Indicates whether or not the pull request is a draft.",
    )


class PullRequestSimplePropLabelsItems(GitHubModel):
    """PullRequestSimplePropLabelsItems"""

    id: int = Field()
    node_id: str = Field()
    url: str = Field()
    name: str = Field()
    description: Union[str, None] = Field()
    color: str = Field()
    default: bool = Field()


model_rebuild(PullRequestSimple)
model_rebuild(PullRequestSimplePropLabelsItems)

__all__ = (
    "PullRequestSimple",
    "PullRequestSimplePropLabelsItems",
)
