"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0168 import DeploymentType
from .group_0357 import EnterpriseWebhooksType
from .group_0358 import SimpleInstallationType
from .group_0360 import RepositoryWebhooksType
from .group_0361 import SimpleUserWebhooksType
from .group_0359 import OrganizationSimpleWebhooksType


class WebhookWorkflowJobCompletedType(TypedDict):
    """workflow_job completed event"""

    action: Literal["completed"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType
    workflow_job: WebhookWorkflowJobCompletedPropWorkflowJobType
    deployment: NotRequired[DeploymentType]


class WebhookWorkflowJobCompletedPropWorkflowJobType(TypedDict):
    """WebhookWorkflowJobCompletedPropWorkflowJob"""

    check_run_url: str
    completed_at: str
    conclusion: Literal[
        "success",
        "failure",
        "skipped",
        "cancelled",
        "action_required",
        "neutral",
        "timed_out",
    ]
    created_at: str
    head_sha: str
    html_url: str
    id: int
    labels: List[str]
    name: str
    node_id: str
    run_attempt: int
    run_id: int
    run_url: str
    runner_group_id: Union[Union[int, None], None]
    runner_group_name: Union[Union[str, None], None]
    runner_id: Union[Union[int, None], None]
    runner_name: Union[Union[str, None], None]
    started_at: str
    status: Literal["queued", "in_progress", "completed", "waiting"]
    head_branch: Union[Union[str, None], None]
    workflow_name: Union[Union[str, None], None]
    steps: List[WebhookWorkflowJobCompletedPropWorkflowJobMergedStepsType]
    url: str


class WebhookWorkflowJobCompletedPropWorkflowJobMergedStepsType(TypedDict):
    """WebhookWorkflowJobCompletedPropWorkflowJobMergedSteps"""

    completed_at: Union[str, None]
    conclusion: Union[None, Literal["failure", "skipped", "success", "cancelled"]]
    name: str
    number: int
    started_at: Union[str, None]
    status: Literal["in_progress", "completed", "queued"]


__all__ = (
    "WebhookWorkflowJobCompletedType",
    "WebhookWorkflowJobCompletedPropWorkflowJobType",
    "WebhookWorkflowJobCompletedPropWorkflowJobMergedStepsType",
)
