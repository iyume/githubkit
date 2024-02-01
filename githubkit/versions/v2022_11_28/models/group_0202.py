"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class CodespacesPermissionsCheckForDevcontainer(GitHubModel):
    """Codespaces Permissions Check

    Permission check result for a given devcontainer config.
    """

    accepted: bool = Field(
        description="Whether the user has accepted the permissions defined by the devcontainer config"
    )


model_rebuild(CodespacesPermissionsCheckForDevcontainer)

__all__ = ("CodespacesPermissionsCheckForDevcontainer",)
