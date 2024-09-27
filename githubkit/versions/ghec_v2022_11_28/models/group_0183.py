"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0002 import SimpleUser


class ProjectCollaboratorPermission(GitHubModel):
    """Project Collaborator Permission

    Project Collaborator Permission
    """

    permission: str = Field()
    user: Union[None, SimpleUser] = Field()


model_rebuild(ProjectCollaboratorPermission)

__all__ = ("ProjectCollaboratorPermission",)
