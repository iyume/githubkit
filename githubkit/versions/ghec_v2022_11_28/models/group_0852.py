"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class EnterprisesEnterpriseActionsRunnerGroupsRunnerGroupIdOrganizationsPutBody(
    GitHubModel
):
    """EnterprisesEnterpriseActionsRunnerGroupsRunnerGroupIdOrganizationsPutBody"""

    selected_organization_ids: list[int] = Field(
        description="List of organization IDs that can access the runner group."
    )


model_rebuild(EnterprisesEnterpriseActionsRunnerGroupsRunnerGroupIdOrganizationsPutBody)

__all__ = ("EnterprisesEnterpriseActionsRunnerGroupsRunnerGroupIdOrganizationsPutBody",)
