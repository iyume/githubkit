"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired


class ActionsEnterprisePermissionsType(TypedDict):
    """ActionsEnterprisePermissions"""

    enabled_organizations: Literal["all", "none", "selected"]
    selected_organizations_url: NotRequired[str]
    allowed_actions: NotRequired[Literal["all", "local_only", "selected"]]
    selected_actions_url: NotRequired[str]


__all__ = ("ActionsEnterprisePermissionsType",)
