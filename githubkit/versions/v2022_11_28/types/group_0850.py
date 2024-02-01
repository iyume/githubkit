"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Literal
from typing_extensions import TypedDict, NotRequired


class OrgsOrgActionsSecretsSecretNamePutBodyType(TypedDict):
    """OrgsOrgActionsSecretsSecretNamePutBody"""

    encrypted_value: NotRequired[str]
    key_id: NotRequired[str]
    visibility: Literal["all", "private", "selected"]
    selected_repository_ids: NotRequired[List[int]]


__all__ = ("OrgsOrgActionsSecretsSecretNamePutBodyType",)
