"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict, NotRequired

from .group_0390 import EnterpriseWebhooksType
from .group_0391 import SimpleInstallationType
from .group_0393 import RepositoryWebhooksType
from .group_0394 import SimpleUserWebhooksType
from .group_0470 import WebhookForkPropForkeeType
from .group_0392 import OrganizationSimpleWebhooksType


class WebhookForkType(TypedDict):
    """fork event

    A user forks a repository.
    """

    enterprise: NotRequired[EnterpriseWebhooksType]
    forkee: WebhookForkPropForkeeType
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


__all__ = ("WebhookForkType",)
