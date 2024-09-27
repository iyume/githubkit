"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoPullsPostBody(GitHubModel):
    """ReposOwnerRepoPullsPostBody"""

    title: Missing[str] = Field(
        default=UNSET,
        description="The title of the new pull request. Required unless `issue` is specified.",
    )
    head: str = Field(
        description="The name of the branch where your changes are implemented. For cross-repository pull requests in the same network, namespace `head` with a user like this: `username:branch`."
    )
    head_repo: Missing[str] = Field(
        default=UNSET,
        description="The name of the repository where the changes in the pull request were made. This field is required for cross-repository pull requests if both repositories are owned by the same organization.",
    )
    base: str = Field(
        description="The name of the branch you want the changes pulled into. This should be an existing branch on the current repository. You cannot submit a pull request to one repository that requests a merge to a base of another repository."
    )
    body: Missing[str] = Field(
        default=UNSET, description="The contents of the pull request."
    )
    maintainer_can_modify: Missing[bool] = Field(
        default=UNSET,
        description="Indicates whether [maintainers can modify](https://docs.github.com/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork/) the pull request.",
    )
    draft: Missing[bool] = Field(
        default=UNSET,
        description='Indicates whether the pull request is a draft. See "[Draft Pull Requests](https://docs.github.com/articles/about-pull-requests#draft-pull-requests)" in the GitHub Help documentation to learn more.',
    )
    issue: Missing[int] = Field(
        default=UNSET,
        description="An issue in the repository to convert to a pull request. The issue title, body, and comments will become the title, body, and comments on the new pull request. Required unless `title` is specified.",
    )


model_rebuild(ReposOwnerRepoPullsPostBody)

__all__ = ("ReposOwnerRepoPullsPostBody",)
