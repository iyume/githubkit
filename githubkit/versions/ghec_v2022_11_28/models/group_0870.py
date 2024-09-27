"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class OrgsOrgActionsSecretsSecretNamePutBody(GitHubModel):
    """OrgsOrgActionsSecretsSecretNamePutBody"""

    encrypted_value: Missing[str] = Field(
        pattern="^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{4})$",
        default=UNSET,
        description="Value for your secret, encrypted with [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using the public key retrieved from the [Get an organization public key](https://docs.github.com/enterprise-cloud@latest//rest/actions/secrets#get-an-organization-public-key) endpoint.",
    )
    key_id: Missing[str] = Field(
        default=UNSET, description="ID of the key you used to encrypt the secret."
    )
    visibility: Literal["all", "private", "selected"] = Field(
        description="Which type of organization repositories have access to the organization secret. `selected` means only the repositories specified by `selected_repository_ids` can access the secret."
    )
    selected_repository_ids: Missing[List[int]] = Field(
        default=UNSET,
        description="An array of repository ids that can access the organization secret. You can only provide a list of repository ids when the `visibility` is set to `selected`. You can manage the list of selected repositories using the [List selected repositories for an organization secret](https://docs.github.com/enterprise-cloud@latest//rest/actions/secrets#list-selected-repositories-for-an-organization-secret), [Set selected repositories for an organization secret](https://docs.github.com/enterprise-cloud@latest//rest/actions/secrets#set-selected-repositories-for-an-organization-secret), and [Remove selected repository from an organization secret](https://docs.github.com/enterprise-cloud@latest//rest/actions/secrets#remove-selected-repository-from-an-organization-secret) endpoints.",
    )


model_rebuild(OrgsOrgActionsSecretsSecretNamePutBody)

__all__ = ("OrgsOrgActionsSecretsSecretNamePutBody",)
