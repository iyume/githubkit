"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class Autolink(GitHubModel):
    """Autolink reference

    An autolink reference.
    """

    id: int = Field()
    key_prefix: str = Field(description="The prefix of a key that is linkified.")
    url_template: str = Field(
        description="A template for the target URL that is generated if a key was found."
    )
    is_alphanumeric: bool = Field(
        description="Whether this autolink reference matches alphanumeric characters. If false, this autolink reference only matches numeric characters."
    )


model_rebuild(Autolink)

__all__ = ("Autolink",)
