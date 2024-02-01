"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0070 import CodespaceMachine


class ReposOwnerRepoCodespacesMachinesGetResponse200(GitHubModel):
    """ReposOwnerRepoCodespacesMachinesGetResponse200"""

    total_count: int = Field()
    machines: List[CodespaceMachine] = Field()


model_rebuild(ReposOwnerRepoCodespacesMachinesGetResponse200)

__all__ = ("ReposOwnerRepoCodespacesMachinesGetResponse200",)
