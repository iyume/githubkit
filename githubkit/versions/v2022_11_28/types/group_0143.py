"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0116 import RepositoryRuleUpdateType
from .group_0142 import RepositoryRuleOneof18Type
from .group_0138 import RepositoryRuleWorkflowsType
from .group_0119 import RepositoryRuleMergeQueueType
from .group_0123 import RepositoryRulePullRequestType
from .group_0112 import OrgRulesetConditionsOneof0Type
from .group_0113 import OrgRulesetConditionsOneof1Type
from .group_0114 import OrgRulesetConditionsOneof2Type
from .group_0140 import RepositoryRuleCodeScanningType
from .group_0104 import RepositoryRulesetConditionsType
from .group_0103 import RepositoryRulesetBypassActorType
from .group_0135 import RepositoryRuleTagNamePatternType
from .group_0133 import RepositoryRuleBranchNamePatternType
from .group_0121 import RepositoryRuleRequiredDeploymentsType
from .group_0125 import RepositoryRuleRequiredStatusChecksType
from .group_0127 import RepositoryRuleCommitMessagePatternType
from .group_0131 import RepositoryRuleCommitterEmailPatternType
from .group_0129 import RepositoryRuleCommitAuthorEmailPatternType
from .group_0118 import (
    RepositoryRuleOneof16Type,
    RepositoryRuleRequiredLinearHistoryType,
)
from .group_0115 import (
    RepositoryRuleOneof15Type,
    RepositoryRuleOneof17Type,
    RepositoryRuleCreationType,
    RepositoryRuleDeletionType,
    RepositoryRuleNonFastForwardType,
    RepositoryRuleRequiredSignaturesType,
)


class RepositoryRulesetType(TypedDict):
    """Repository ruleset

    A set of rules to apply when specified conditions are met.
    """

    id: int
    name: str
    target: NotRequired[Literal["branch", "tag", "push"]]
    source_type: NotRequired[Literal["Repository", "Organization"]]
    source: str
    enforcement: Literal["disabled", "active", "evaluate"]
    bypass_actors: NotRequired[List[RepositoryRulesetBypassActorType]]
    current_user_can_bypass: NotRequired[
        Literal["always", "pull_requests_only", "never"]
    ]
    node_id: NotRequired[str]
    links: NotRequired[RepositoryRulesetPropLinksType]
    conditions: NotRequired[
        Union[
            RepositoryRulesetConditionsType,
            OrgRulesetConditionsOneof0Type,
            OrgRulesetConditionsOneof1Type,
            OrgRulesetConditionsOneof2Type,
            None,
        ]
    ]
    rules: NotRequired[
        List[
            Union[
                RepositoryRuleCreationType,
                RepositoryRuleUpdateType,
                RepositoryRuleDeletionType,
                RepositoryRuleRequiredLinearHistoryType,
                RepositoryRuleMergeQueueType,
                RepositoryRuleRequiredDeploymentsType,
                RepositoryRuleRequiredSignaturesType,
                RepositoryRulePullRequestType,
                RepositoryRuleRequiredStatusChecksType,
                RepositoryRuleNonFastForwardType,
                RepositoryRuleCommitMessagePatternType,
                RepositoryRuleCommitAuthorEmailPatternType,
                RepositoryRuleCommitterEmailPatternType,
                RepositoryRuleBranchNamePatternType,
                RepositoryRuleTagNamePatternType,
                RepositoryRuleOneof15Type,
                RepositoryRuleOneof16Type,
                RepositoryRuleOneof17Type,
                RepositoryRuleOneof18Type,
                RepositoryRuleWorkflowsType,
                RepositoryRuleCodeScanningType,
            ]
        ]
    ]
    created_at: NotRequired[datetime]
    updated_at: NotRequired[datetime]


class RepositoryRulesetPropLinksType(TypedDict):
    """RepositoryRulesetPropLinks"""

    self_: NotRequired[RepositoryRulesetPropLinksPropSelfType]
    html: NotRequired[RepositoryRulesetPropLinksPropHtmlType]


class RepositoryRulesetPropLinksPropSelfType(TypedDict):
    """RepositoryRulesetPropLinksPropSelf"""

    href: NotRequired[str]


class RepositoryRulesetPropLinksPropHtmlType(TypedDict):
    """RepositoryRulesetPropLinksPropHtml"""

    href: NotRequired[str]


__all__ = (
    "RepositoryRulesetType",
    "RepositoryRulesetPropLinksType",
    "RepositoryRulesetPropLinksPropSelfType",
    "RepositoryRulesetPropLinksPropHtmlType",
)
