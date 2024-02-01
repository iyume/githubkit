"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0355 import EnterpriseWebhooksType
from .group_0356 import SimpleInstallationType
from .group_0358 import RepositoryWebhooksType
from .group_0359 import SimpleUserWebhooksType
from .group_0357 import OrganizationSimpleWebhooksType


class WebhookCodeScanningAlertAppearedInBranchType(TypedDict):
    """code_scanning_alert appeared_in_branch event"""

    action: Literal["appeared_in_branch"]
    alert: WebhookCodeScanningAlertAppearedInBranchPropAlertType
    commit_oid: str
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    ref: str
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


class WebhookCodeScanningAlertAppearedInBranchPropAlertType(TypedDict):
    """WebhookCodeScanningAlertAppearedInBranchPropAlert

    The code scanning alert involved in the event.
    """

    created_at: datetime
    dismissed_at: Union[datetime, None]
    dismissed_by: Union[
        WebhookCodeScanningAlertAppearedInBranchPropAlertPropDismissedByType, None
    ]
    dismissed_reason: Union[
        None, Literal["false positive", "won't fix", "used in tests"]
    ]
    html_url: str
    most_recent_instance: NotRequired[
        Union[
            WebhookCodeScanningAlertAppearedInBranchPropAlertPropMostRecentInstanceType,
            None,
        ]
    ]
    number: int
    rule: WebhookCodeScanningAlertAppearedInBranchPropAlertPropRuleType
    state: Literal["open", "dismissed", "fixed"]
    tool: WebhookCodeScanningAlertAppearedInBranchPropAlertPropToolType
    url: str


class WebhookCodeScanningAlertAppearedInBranchPropAlertPropDismissedByType(TypedDict):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]


class WebhookCodeScanningAlertAppearedInBranchPropAlertPropMostRecentInstanceType(
    TypedDict
):
    """Alert Instance"""

    analysis_key: str
    category: NotRequired[str]
    classifications: NotRequired[List[str]]
    commit_sha: NotRequired[str]
    environment: str
    location: NotRequired[
        WebhookCodeScanningAlertAppearedInBranchPropAlertPropMostRecentInstancePropLocationType
    ]
    message: NotRequired[
        WebhookCodeScanningAlertAppearedInBranchPropAlertPropMostRecentInstancePropMessageType
    ]
    ref: str
    state: Literal["open", "dismissed", "fixed"]


class WebhookCodeScanningAlertAppearedInBranchPropAlertPropMostRecentInstancePropLocationType(
    TypedDict
):
    """WebhookCodeScanningAlertAppearedInBranchPropAlertPropMostRecentInstancePropLocat
    ion
    """

    end_column: NotRequired[int]
    end_line: NotRequired[int]
    path: NotRequired[str]
    start_column: NotRequired[int]
    start_line: NotRequired[int]


class WebhookCodeScanningAlertAppearedInBranchPropAlertPropMostRecentInstancePropMessageType(
    TypedDict
):
    """WebhookCodeScanningAlertAppearedInBranchPropAlertPropMostRecentInstancePropMessa
    ge
    """

    text: NotRequired[str]


class WebhookCodeScanningAlertAppearedInBranchPropAlertPropRuleType(TypedDict):
    """WebhookCodeScanningAlertAppearedInBranchPropAlertPropRule"""

    description: str
    id: str
    severity: Union[None, Literal["none", "note", "warning", "error"]]


class WebhookCodeScanningAlertAppearedInBranchPropAlertPropToolType(TypedDict):
    """WebhookCodeScanningAlertAppearedInBranchPropAlertPropTool"""

    name: str
    version: Union[str, None]


__all__ = (
    "WebhookCodeScanningAlertAppearedInBranchType",
    "WebhookCodeScanningAlertAppearedInBranchPropAlertType",
    "WebhookCodeScanningAlertAppearedInBranchPropAlertPropDismissedByType",
    "WebhookCodeScanningAlertAppearedInBranchPropAlertPropMostRecentInstanceType",
    "WebhookCodeScanningAlertAppearedInBranchPropAlertPropMostRecentInstancePropLocationType",
    "WebhookCodeScanningAlertAppearedInBranchPropAlertPropMostRecentInstancePropMessageType",
    "WebhookCodeScanningAlertAppearedInBranchPropAlertPropRuleType",
    "WebhookCodeScanningAlertAppearedInBranchPropAlertPropToolType",
)
