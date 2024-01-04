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


class OrgsOrgHooksHookIdPatchBody(GitHubModel):
    """OrgsOrgHooksHookIdPatchBody"""

    config: Missing[OrgsOrgHooksHookIdPatchBodyPropConfig] = Field(
        default=UNSET,
        description="Key/value pairs to provide settings for this webhook.",
    )
    events: Missing[List[str]] = Field(
        default=UNSET,
        description="Determines what [events](https://docs.github.com/webhooks/event-payloads) the hook is triggered for.",
    )
    active: Missing[bool] = Field(
        default=UNSET,
        description="Determines if notifications are sent when the webhook is triggered. Set to `true` to send notifications.",
    )
    name: Missing[str] = Field(default=UNSET)


class OrgsOrgHooksHookIdPatchBodyPropConfig(GitHubModel):
    """OrgsOrgHooksHookIdPatchBodyPropConfig

    Key/value pairs to provide settings for this webhook.
    """

    url: str = Field(description="The URL to which the payloads will be delivered.")
    content_type: Missing[str] = Field(
        default=UNSET,
        description="The media type used to serialize the payloads. Supported values include `json` and `form`. The default is `form`.",
    )
    secret: Missing[str] = Field(
        default=UNSET,
        description="If provided, the `secret` will be used as the `key` to generate the HMAC hex digest value for [delivery signature headers](https://docs.github.com/webhooks/event-payloads/#delivery-headers).",
    )
    insecure_ssl: Missing[Union[str, float]] = Field(default=UNSET)


model_rebuild(OrgsOrgHooksHookIdPatchBody)
model_rebuild(OrgsOrgHooksHookIdPatchBodyPropConfig)

__all__ = (
    "OrgsOrgHooksHookIdPatchBody",
    "OrgsOrgHooksHookIdPatchBodyPropConfig",
)