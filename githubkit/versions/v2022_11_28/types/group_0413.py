"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0362 import DiscussionType
from .group_0355 import EnterpriseWebhooksType
from .group_0356 import SimpleInstallationType
from .group_0358 import RepositoryWebhooksType
from .group_0359 import SimpleUserWebhooksType
from .group_0357 import OrganizationSimpleWebhooksType


class WebhookDiscussionCategoryChangedType(TypedDict):
    """discussion category changed event"""

    action: Literal["category_changed"]
    changes: WebhookDiscussionCategoryChangedPropChangesType
    discussion: DiscussionType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


class WebhookDiscussionCategoryChangedPropChangesType(TypedDict):
    """WebhookDiscussionCategoryChangedPropChanges"""

    category: WebhookDiscussionCategoryChangedPropChangesPropCategoryType


class WebhookDiscussionCategoryChangedPropChangesPropCategoryType(TypedDict):
    """WebhookDiscussionCategoryChangedPropChangesPropCategory"""

    from_: WebhookDiscussionCategoryChangedPropChangesPropCategoryPropFromType


class WebhookDiscussionCategoryChangedPropChangesPropCategoryPropFromType(TypedDict):
    """WebhookDiscussionCategoryChangedPropChangesPropCategoryPropFrom"""

    created_at: datetime
    description: str
    emoji: str
    id: int
    is_answerable: bool
    name: str
    node_id: NotRequired[str]
    repository_id: int
    slug: str
    updated_at: str


__all__ = (
    "WebhookDiscussionCategoryChangedType",
    "WebhookDiscussionCategoryChangedPropChangesType",
    "WebhookDiscussionCategoryChangedPropChangesPropCategoryType",
    "WebhookDiscussionCategoryChangedPropChangesPropCategoryPropFromType",
)
