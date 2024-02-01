"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class OrganizationSimpleWebhooks(GitHubModel):
    """Organization Simple

    A GitHub organization. Webhook payloads contain the `organization` property when
    the webhook is configured for an
    organization, or when the event occurs from activity in a repository owned by an
    organization.
    """

    login: str = Field()
    id: int = Field()
    node_id: str = Field()
    url: str = Field()
    repos_url: str = Field()
    events_url: str = Field()
    hooks_url: str = Field()
    issues_url: str = Field()
    members_url: str = Field()
    public_members_url: str = Field()
    avatar_url: str = Field()
    description: Union[str, None] = Field()


model_rebuild(OrganizationSimpleWebhooks)

__all__ = ("OrganizationSimpleWebhooks",)
