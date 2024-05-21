"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from typing_extensions import TypeAlias

from ..models import WebhookInstallationTargetRenamed

Event: TypeAlias = WebhookInstallationTargetRenamed

InstallationTargetEvent: TypeAlias = Event

action_types = WebhookInstallationTargetRenamed

installation_target_action_types = action_types

__all__ = (
    "Event",
    "InstallationTargetEvent",
    "action_types",
    "installation_target_action_types",
)