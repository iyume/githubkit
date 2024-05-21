"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0080 import OrganizationCustomRepositoryRole


class OrgsOrgCustomRepositoryRolesGetResponse200(GitHubModel):
    """OrgsOrgCustomRepositoryRolesGetResponse200"""

    total_count: Missing[int] = Field(
        default=UNSET, description="The number of custom roles in this organization"
    )
    custom_roles: Missing[List[OrganizationCustomRepositoryRole]] = Field(default=UNSET)


model_rebuild(OrgsOrgCustomRepositoryRolesGetResponse200)

__all__ = ("OrgsOrgCustomRepositoryRolesGetResponse200",)