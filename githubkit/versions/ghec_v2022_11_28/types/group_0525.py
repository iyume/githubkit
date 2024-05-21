"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0015 import InstallationType
from .group_0412 import WebhooksUserType
from .group_0400 import EnterpriseWebhooksType
from .group_0403 import RepositoryWebhooksType
from .group_0404 import SimpleUserWebhooksType
from .group_0402 import OrganizationSimpleWebhooksType
from .group_0418 import WebhooksRepositoriesAddedItemsType


class WebhookInstallationRepositoriesRemovedType(TypedDict):
    """installation_repositories removed event"""

    action: Literal["removed"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: InstallationType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repositories_added: List[WebhooksRepositoriesAddedItemsType]
    repositories_removed: List[
        WebhookInstallationRepositoriesRemovedPropRepositoriesRemovedItemsType
    ]
    repository: NotRequired[RepositoryWebhooksType]
    repository_selection: Literal["all", "selected"]
    requester: Union[WebhooksUserType, None]
    sender: SimpleUserWebhooksType


class WebhookInstallationRepositoriesRemovedPropRepositoriesRemovedItemsType(TypedDict):
    """WebhookInstallationRepositoriesRemovedPropRepositoriesRemovedItems"""

    full_name: str
    id: int
    name: str
    node_id: str
    private: bool


__all__ = (
    "WebhookInstallationRepositoriesRemovedType",
    "WebhookInstallationRepositoriesRemovedPropRepositoriesRemovedItemsType",
)