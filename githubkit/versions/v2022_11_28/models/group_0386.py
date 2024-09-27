"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class WebhooksDeployKey(GitHubModel):
    """WebhooksDeployKey

    The [`deploy key`](https://docs.github.com/rest/deploy-keys/deploy-keys#get-a-
    deploy-key) resource.
    """

    added_by: Missing[Union[str, None]] = Field(default=UNSET)
    created_at: str = Field()
    id: int = Field()
    key: str = Field()
    last_used: Missing[Union[str, None]] = Field(default=UNSET)
    read_only: bool = Field()
    title: str = Field()
    url: str = Field()
    verified: bool = Field()


model_rebuild(WebhooksDeployKey)

__all__ = ("WebhooksDeployKey",)
