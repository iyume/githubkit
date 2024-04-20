"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_1004 import ReposOwnerRepoPagesPutBodyPropSourceAnyof1


class ReposOwnerRepoPagesPutBodyAnyof2(GitHubModel):
    """ReposOwnerRepoPagesPutBodyAnyof2"""

    cname: Union[str, None] = Field(
        description='Specify a custom domain for the repository. Sending a `null` value will remove the custom domain. For more about custom domains, see "[Using a custom domain with GitHub Pages](https://docs.github.com/enterprise-cloud@latest//articles/using-a-custom-domain-with-github-pages/)."'
    )
    https_enforced: Missing[bool] = Field(
        default=UNSET,
        description="Specify whether HTTPS should be enforced for the repository.",
    )
    build_type: Missing[Literal["legacy", "workflow"]] = Field(
        default=UNSET,
        description="The process by which the GitHub Pages site will be built. `workflow` means that the site is built by a custom GitHub Actions workflow. `legacy` means that the site is built by GitHub when changes are pushed to a specific branch.",
    )
    source: Missing[
        Union[
            Literal["gh-pages", "master", "master /docs"],
            ReposOwnerRepoPagesPutBodyPropSourceAnyof1,
        ]
    ] = Field(default=UNSET)
    public: Missing[bool] = Field(
        default=UNSET,
        description="Configures access controls for the GitHub Pages site. If public is set to `true`, the site is accessible to anyone on the internet. If set to `false`, the site will only be accessible to users who have at least `read` access to the repository that published the site. This includes anyone in your Enterprise if the repository is set to `internal` visibility.",
    )


model_rebuild(ReposOwnerRepoPagesPutBodyAnyof2)

__all__ = ("ReposOwnerRepoPagesPutBodyAnyof2",)
