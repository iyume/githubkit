"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0053 import DependabotAlertPackage


class DependabotAlertSecurityVulnerability(GitHubModel):
    """DependabotAlertSecurityVulnerability

    Details pertaining to one vulnerable version range for the advisory.
    """

    package: DependabotAlertPackage = Field(
        description="Details for the vulnerable package."
    )
    severity: Literal["low", "medium", "high", "critical"] = Field(
        description="The severity of the vulnerability."
    )
    vulnerable_version_range: str = Field(
        description="Conditions that identify vulnerable versions of this vulnerability's package."
    )
    first_patched_version: Union[
        DependabotAlertSecurityVulnerabilityPropFirstPatchedVersion, None
    ] = Field(
        description="Details pertaining to the package version that patches this vulnerability."
    )


class DependabotAlertSecurityVulnerabilityPropFirstPatchedVersion(GitHubModel):
    """DependabotAlertSecurityVulnerabilityPropFirstPatchedVersion

    Details pertaining to the package version that patches this vulnerability.
    """

    identifier: str = Field(
        description="The package version that patches this vulnerability."
    )


model_rebuild(DependabotAlertSecurityVulnerability)
model_rebuild(DependabotAlertSecurityVulnerabilityPropFirstPatchedVersion)

__all__ = (
    "DependabotAlertSecurityVulnerability",
    "DependabotAlertSecurityVulnerabilityPropFirstPatchedVersion",
)
