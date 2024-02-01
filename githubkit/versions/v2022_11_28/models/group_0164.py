"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ReviewCustomGatesStateRequired(GitHubModel):
    """ReviewCustomGatesStateRequired"""

    environment_name: str = Field(
        description="The name of the environment to approve or reject."
    )
    state: Literal["approved", "rejected"] = Field(
        description="Whether to approve or reject deployment to the specified environments."
    )
    comment: Missing[str] = Field(
        default=UNSET, description="Optional comment to include with the review."
    )


model_rebuild(ReviewCustomGatesStateRequired)

__all__ = ("ReviewCustomGatesStateRequired",)
