"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ScimError(GitHubModel):
    """Scim Error

    Scim Error
    """

    message: Missing[Union[str, None]] = Field(default=UNSET)
    documentation_url: Missing[Union[str, None]] = Field(default=UNSET)
    detail: Missing[Union[str, None]] = Field(default=UNSET)
    status: Missing[int] = Field(default=UNSET)
    scim_type: Missing[Union[str, None]] = Field(default=UNSET, alias="scimType")
    schemas: Missing[List[str]] = Field(default=UNSET)


model_rebuild(ScimError)

__all__ = ("ScimError",)
