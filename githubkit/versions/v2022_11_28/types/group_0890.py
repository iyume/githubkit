"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict, NotRequired


class ReposOwnerRepoDependabotSecretsSecretNamePutBodyType(TypedDict):
    """ReposOwnerRepoDependabotSecretsSecretNamePutBody"""

    encrypted_value: NotRequired[str]
    key_id: NotRequired[str]


__all__ = ("ReposOwnerRepoDependabotSecretsSecretNamePutBodyType",)
