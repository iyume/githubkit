"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List
from typing_extensions import Annotated

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class OrgsOrgActionsRunnersRunnerIdLabelsPutBody(GitHubModel):
    """OrgsOrgActionsRunnersRunnerIdLabelsPutBody"""

    labels: List[str] = Field(
        max_length=100,
        description="The names of the custom labels to set for the runner. You can pass an empty array to remove all custom labels.",
    )


model_rebuild(OrgsOrgActionsRunnersRunnerIdLabelsPutBody)

__all__ = ("OrgsOrgActionsRunnersRunnerIdLabelsPutBody",)
