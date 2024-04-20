"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0130 import RepositoryRuleUpdateType
from .group_0150 import RepositoryRuleWorkflowsType
from .group_0135 import RepositoryRulePullRequestType
from .group_0118 import RepositoryRulesetConditionsType
from .group_0117 import RepositoryRulesetBypassActorType
from .group_0147 import RepositoryRuleTagNamePatternType
from .group_0145 import RepositoryRuleBranchNamePatternType
from .group_0133 import RepositoryRuleRequiredDeploymentsType
from .group_0137 import RepositoryRuleRequiredStatusChecksType
from .group_0139 import RepositoryRuleCommitMessagePatternType
from .group_0132 import RepositoryRuleRequiredLinearHistoryType
from .group_0143 import RepositoryRuleCommitterEmailPatternType
from .group_0141 import RepositoryRuleCommitAuthorEmailPatternType
from .group_0129 import (
    RepositoryRuleCreationType,
    RepositoryRuleDeletionType,
    RepositoryRuleNonFastForwardType,
    RepositoryRuleRequiredSignaturesType,
)


class ReposOwnerRepoRulesetsRulesetIdPutBodyType(TypedDict):
    """ReposOwnerRepoRulesetsRulesetIdPutBody"""

    name: NotRequired[str]
    target: NotRequired[Literal["branch", "tag"]]
    enforcement: NotRequired[Literal["disabled", "active", "evaluate"]]
    bypass_actors: NotRequired[List[RepositoryRulesetBypassActorType]]
    conditions: NotRequired[RepositoryRulesetConditionsType]
    rules: NotRequired[
        List[
            Union[
                RepositoryRuleCreationType,
                RepositoryRuleUpdateType,
                RepositoryRuleDeletionType,
                RepositoryRuleRequiredLinearHistoryType,
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
                RepositoryRuleWorkflowsType,
            ]
        ]
    ]


__all__ = ("ReposOwnerRepoRulesetsRulesetIdPutBodyType",)
