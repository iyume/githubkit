"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0002 import SimpleUser
from .group_0008 import Integration


class RemovedFromProjectIssueEvent(GitHubModel):
    """Removed from Project Issue Event

    Removed from Project Issue Event
    """

    id: int = Field()
    node_id: str = Field()
    url: str = Field()
    actor: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    event: Literal["removed_from_project"] = Field()
    commit_id: Union[str, None] = Field()
    commit_url: Union[str, None] = Field()
    created_at: str = Field()
    performed_via_github_app: Union[None, Integration, None] = Field()
    project_card: Missing[RemovedFromProjectIssueEventPropProjectCard] = Field(
        default=UNSET
    )


class RemovedFromProjectIssueEventPropProjectCard(GitHubModel):
    """RemovedFromProjectIssueEventPropProjectCard"""

    id: int = Field()
    url: str = Field()
    project_id: int = Field()
    project_url: str = Field()
    column_name: str = Field()
    previous_column_name: Missing[str] = Field(default=UNSET)


model_rebuild(RemovedFromProjectIssueEvent)
model_rebuild(RemovedFromProjectIssueEventPropProjectCard)

__all__ = (
    "RemovedFromProjectIssueEvent",
    "RemovedFromProjectIssueEventPropProjectCard",
)
