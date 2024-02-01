"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class BranchRestrictionPolicy(GitHubModel):
    """Branch Restriction Policy

    Branch Restriction Policy
    """

    url: str = Field()
    users_url: str = Field()
    teams_url: str = Field()
    apps_url: str = Field()
    users: List[BranchRestrictionPolicyPropUsersItems] = Field()
    teams: List[BranchRestrictionPolicyPropTeamsItems] = Field()
    apps: List[BranchRestrictionPolicyPropAppsItems] = Field()


class BranchRestrictionPolicyPropUsersItems(GitHubModel):
    """BranchRestrictionPolicyPropUsersItems"""

    login: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    avatar_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    type: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)


class BranchRestrictionPolicyPropTeamsItems(GitHubModel):
    """BranchRestrictionPolicyPropTeamsItems"""

    id: Missing[int] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)
    slug: Missing[str] = Field(default=UNSET)
    description: Missing[Union[str, None]] = Field(default=UNSET)
    privacy: Missing[str] = Field(default=UNSET)
    notification_setting: Missing[str] = Field(default=UNSET)
    permission: Missing[str] = Field(default=UNSET)
    members_url: Missing[str] = Field(default=UNSET)
    repositories_url: Missing[str] = Field(default=UNSET)
    parent: Missing[Union[str, None]] = Field(default=UNSET)


class BranchRestrictionPolicyPropAppsItems(GitHubModel):
    """BranchRestrictionPolicyPropAppsItems"""

    id: Missing[int] = Field(default=UNSET)
    slug: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    owner: Missing[BranchRestrictionPolicyPropAppsItemsPropOwner] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)
    description: Missing[str] = Field(default=UNSET)
    external_url: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    created_at: Missing[str] = Field(default=UNSET)
    updated_at: Missing[str] = Field(default=UNSET)
    permissions: Missing[BranchRestrictionPolicyPropAppsItemsPropPermissions] = Field(
        default=UNSET
    )
    events: Missing[List[str]] = Field(default=UNSET)


class BranchRestrictionPolicyPropAppsItemsPropOwner(GitHubModel):
    """BranchRestrictionPolicyPropAppsItemsPropOwner"""

    login: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    hooks_url: Missing[str] = Field(default=UNSET)
    issues_url: Missing[str] = Field(default=UNSET)
    members_url: Missing[str] = Field(default=UNSET)
    public_members_url: Missing[str] = Field(default=UNSET)
    avatar_url: Missing[str] = Field(default=UNSET)
    description: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    type: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)


class BranchRestrictionPolicyPropAppsItemsPropPermissions(GitHubModel):
    """BranchRestrictionPolicyPropAppsItemsPropPermissions"""

    metadata: Missing[str] = Field(default=UNSET)
    contents: Missing[str] = Field(default=UNSET)
    issues: Missing[str] = Field(default=UNSET)
    single_file: Missing[str] = Field(default=UNSET)


model_rebuild(BranchRestrictionPolicy)
model_rebuild(BranchRestrictionPolicyPropUsersItems)
model_rebuild(BranchRestrictionPolicyPropTeamsItems)
model_rebuild(BranchRestrictionPolicyPropAppsItems)
model_rebuild(BranchRestrictionPolicyPropAppsItemsPropOwner)
model_rebuild(BranchRestrictionPolicyPropAppsItemsPropPermissions)

__all__ = (
    "BranchRestrictionPolicy",
    "BranchRestrictionPolicyPropUsersItems",
    "BranchRestrictionPolicyPropTeamsItems",
    "BranchRestrictionPolicyPropAppsItems",
    "BranchRestrictionPolicyPropAppsItemsPropOwner",
    "BranchRestrictionPolicyPropAppsItemsPropPermissions",
)
