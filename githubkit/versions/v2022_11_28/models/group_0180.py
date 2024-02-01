"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0179 import DiffEntry
from .group_0001 import SimpleUser
from .group_0181 import CommitPropCommit


class Commit(GitHubModel):
    """Commit

    Commit
    """

    url: str = Field()
    sha: str = Field()
    node_id: str = Field()
    html_url: str = Field()
    comments_url: str = Field()
    commit: CommitPropCommit = Field()
    author: Union[None, SimpleUser] = Field()
    committer: Union[None, SimpleUser] = Field()
    parents: List[CommitPropParentsItems] = Field()
    stats: Missing[CommitPropStats] = Field(default=UNSET)
    files: Missing[List[DiffEntry]] = Field(default=UNSET)


class CommitPropParentsItems(GitHubModel):
    """CommitPropParentsItems"""

    sha: str = Field()
    url: str = Field()
    html_url: Missing[str] = Field(default=UNSET)


class CommitPropStats(GitHubModel):
    """CommitPropStats"""

    additions: Missing[int] = Field(default=UNSET)
    deletions: Missing[int] = Field(default=UNSET)
    total: Missing[int] = Field(default=UNSET)


model_rebuild(Commit)
model_rebuild(CommitPropParentsItems)
model_rebuild(CommitPropStats)

__all__ = (
    "Commit",
    "CommitPropParentsItems",
    "CommitPropStats",
)
