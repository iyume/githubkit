"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired


class GistsPostBodyType(TypedDict):
    """GistsPostBody"""

    description: NotRequired[str]
    files: GistsPostBodyPropFilesType
    public: NotRequired[Union[bool, Literal["true", "false"]]]


class GistsPostBodyPropFilesType(TypedDict):
    """GistsPostBodyPropFiles

    Names and content for the files that make up the gist

    Examples:
        {'hello.rb': {'content': 'puts "Hello, World!"'}}
    """


__all__ = (
    "GistsPostBodyType",
    "GistsPostBodyPropFilesType",
)
