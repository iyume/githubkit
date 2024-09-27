"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict, NotRequired

from .group_0056 import SecurityAndAnalysisType


class WebhookSecurityAndAnalysisPropChangesPropFromType(TypedDict):
    """WebhookSecurityAndAnalysisPropChangesPropFrom"""

    security_and_analysis: NotRequired[Union[SecurityAndAnalysisType, None]]


__all__ = ("WebhookSecurityAndAnalysisPropChangesPropFromType",)
