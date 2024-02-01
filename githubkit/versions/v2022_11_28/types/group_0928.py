"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List
from typing_extensions import TypedDict, NotRequired


class ProjectsProjectIdDeleteResponse403Type(TypedDict):
    """ProjectsProjectIdDeleteResponse403"""

    message: NotRequired[str]
    documentation_url: NotRequired[str]
    errors: NotRequired[List[str]]


__all__ = ("ProjectsProjectIdDeleteResponse403Type",)
