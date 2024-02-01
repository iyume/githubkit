"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class OrgsOrgTeamsTeamSlugReposOwnerRepoPutBody(GitHubModel):
    """OrgsOrgTeamsTeamSlugReposOwnerRepoPutBody"""

    permission: Missing[str] = Field(
        default=UNSET,
        description="The permission to grant the team on this repository. We accept the following permissions to be set: `pull`, `triage`, `push`, `maintain`, `admin` and you can also specify a custom repository role name, if the owning organization has defined any. If no permission is specified, the team's `permission` attribute will be used to determine what permission to grant the team on this repository.",
    )


model_rebuild(OrgsOrgTeamsTeamSlugReposOwnerRepoPutBody)

__all__ = ("OrgsOrgTeamsTeamSlugReposOwnerRepoPutBody",)
