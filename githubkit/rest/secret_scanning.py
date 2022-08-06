"""DO NOT EDIT THIS FILE!

This file is auto generated by github rest api discription.
See https://github.com/github/rest-api-description for more information.
"""


from typing import TYPE_CHECKING, List, Union, Literal, overload

from pydantic import BaseModel, parse_obj_as

from githubkit.utils import UNSET, Unset, exclude_unset

from .types import ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBodyType
from .models import (
    BasicError,
    SecretScanningAlert,
    SecretScanningLocation,
    OrganizationSecretScanningAlert,
    EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
    ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBody,
)

if TYPE_CHECKING:
    from githubkit import GitHub
    from githubkit.response import Response


class SecretScanningClient:
    def __init__(self, github: "GitHub"):
        self._github = github

    def list_alerts_for_enterprise(
        self,
        enterprise: str,
        state: Union[Unset, Literal["open", "resolved"]] = UNSET,
        secret_type: Union[Unset, str] = UNSET,
        resolution: Union[Unset, str] = UNSET,
        sort: Union[Unset, Literal["created", "updated"]] = "created",
        direction: Union[Unset, Literal["asc", "desc"]] = "desc",
        per_page: Union[Unset, int] = 30,
        before: Union[Unset, str] = UNSET,
        after: Union[Unset, str] = UNSET,
    ) -> "Response[List[OrganizationSecretScanningAlert]]":
        url = f"/enterprises/{enterprise}/secret-scanning/alerts"

        params = {
            "state": state,
            "secret_type": secret_type,
            "resolution": resolution,
            "sort": sort,
            "direction": direction,
            "per_page": per_page,
            "before": before,
            "after": after,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[OrganizationSecretScanningAlert],
            error_models={
                "404": BasicError,
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )

    async def async_list_alerts_for_enterprise(
        self,
        enterprise: str,
        state: Union[Unset, Literal["open", "resolved"]] = UNSET,
        secret_type: Union[Unset, str] = UNSET,
        resolution: Union[Unset, str] = UNSET,
        sort: Union[Unset, Literal["created", "updated"]] = "created",
        direction: Union[Unset, Literal["asc", "desc"]] = "desc",
        per_page: Union[Unset, int] = 30,
        before: Union[Unset, str] = UNSET,
        after: Union[Unset, str] = UNSET,
    ) -> "Response[List[OrganizationSecretScanningAlert]]":
        url = f"/enterprises/{enterprise}/secret-scanning/alerts"

        params = {
            "state": state,
            "secret_type": secret_type,
            "resolution": resolution,
            "sort": sort,
            "direction": direction,
            "per_page": per_page,
            "before": before,
            "after": after,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[OrganizationSecretScanningAlert],
            error_models={
                "404": BasicError,
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )

    def list_alerts_for_org(
        self,
        org: str,
        state: Union[Unset, Literal["open", "resolved"]] = UNSET,
        secret_type: Union[Unset, str] = UNSET,
        resolution: Union[Unset, str] = UNSET,
        sort: Union[Unset, Literal["created", "updated"]] = "created",
        direction: Union[Unset, Literal["asc", "desc"]] = "desc",
        page: Union[Unset, int] = 1,
        per_page: Union[Unset, int] = 30,
        before: Union[Unset, str] = UNSET,
        after: Union[Unset, str] = UNSET,
    ) -> "Response[List[OrganizationSecretScanningAlert]]":
        url = f"/orgs/{org}/secret-scanning/alerts"

        params = {
            "state": state,
            "secret_type": secret_type,
            "resolution": resolution,
            "sort": sort,
            "direction": direction,
            "page": page,
            "per_page": per_page,
            "before": before,
            "after": after,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[OrganizationSecretScanningAlert],
            error_models={
                "404": BasicError,
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )

    async def async_list_alerts_for_org(
        self,
        org: str,
        state: Union[Unset, Literal["open", "resolved"]] = UNSET,
        secret_type: Union[Unset, str] = UNSET,
        resolution: Union[Unset, str] = UNSET,
        sort: Union[Unset, Literal["created", "updated"]] = "created",
        direction: Union[Unset, Literal["asc", "desc"]] = "desc",
        page: Union[Unset, int] = 1,
        per_page: Union[Unset, int] = 30,
        before: Union[Unset, str] = UNSET,
        after: Union[Unset, str] = UNSET,
    ) -> "Response[List[OrganizationSecretScanningAlert]]":
        url = f"/orgs/{org}/secret-scanning/alerts"

        params = {
            "state": state,
            "secret_type": secret_type,
            "resolution": resolution,
            "sort": sort,
            "direction": direction,
            "page": page,
            "per_page": per_page,
            "before": before,
            "after": after,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[OrganizationSecretScanningAlert],
            error_models={
                "404": BasicError,
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )

    def list_alerts_for_repo(
        self,
        owner: str,
        repo: str,
        state: Union[Unset, Literal["open", "resolved"]] = UNSET,
        secret_type: Union[Unset, str] = UNSET,
        resolution: Union[Unset, str] = UNSET,
        sort: Union[Unset, Literal["created", "updated"]] = "created",
        direction: Union[Unset, Literal["asc", "desc"]] = "desc",
        page: Union[Unset, int] = 1,
        per_page: Union[Unset, int] = 30,
        before: Union[Unset, str] = UNSET,
        after: Union[Unset, str] = UNSET,
    ) -> "Response[List[SecretScanningAlert]]":
        url = f"/repos/{owner}/{repo}/secret-scanning/alerts"

        params = {
            "state": state,
            "secret_type": secret_type,
            "resolution": resolution,
            "sort": sort,
            "direction": direction,
            "page": page,
            "per_page": per_page,
            "before": before,
            "after": after,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[SecretScanningAlert],
            error_models={
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )

    async def async_list_alerts_for_repo(
        self,
        owner: str,
        repo: str,
        state: Union[Unset, Literal["open", "resolved"]] = UNSET,
        secret_type: Union[Unset, str] = UNSET,
        resolution: Union[Unset, str] = UNSET,
        sort: Union[Unset, Literal["created", "updated"]] = "created",
        direction: Union[Unset, Literal["asc", "desc"]] = "desc",
        page: Union[Unset, int] = 1,
        per_page: Union[Unset, int] = 30,
        before: Union[Unset, str] = UNSET,
        after: Union[Unset, str] = UNSET,
    ) -> "Response[List[SecretScanningAlert]]":
        url = f"/repos/{owner}/{repo}/secret-scanning/alerts"

        params = {
            "state": state,
            "secret_type": secret_type,
            "resolution": resolution,
            "sort": sort,
            "direction": direction,
            "page": page,
            "per_page": per_page,
            "before": before,
            "after": after,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[SecretScanningAlert],
            error_models={
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )

    def get_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
    ) -> "Response[SecretScanningAlert]":
        url = f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}"

        return self._github.request(
            "GET",
            url,
            response_model=SecretScanningAlert,
            error_models={
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )

    async def async_get_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
    ) -> "Response[SecretScanningAlert]":
        url = f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}"

        return await self._github.arequest(
            "GET",
            url,
            response_model=SecretScanningAlert,
            error_models={
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )

    @overload
    def update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        data: ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBodyType,
    ) -> "Response[SecretScanningAlert]":
        ...

    @overload
    def update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        data: Unset = UNSET,
        state: Literal["open", "resolved"],
        resolution: Union[
            Unset,
            Union[
                None, Literal["false_positive", "wont_fix", "revoked", "used_in_tests"]
            ],
        ] = UNSET,
    ) -> "Response[SecretScanningAlert]":
        ...

    def update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        data: Union[
            Unset, ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBodyType
        ] = UNSET,
        **kwargs,
    ) -> "Response[SecretScanningAlert]":
        url = f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(
            ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBody, json
        )
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PATCH",
            url,
            json=exclude_unset(json),
            response_model=SecretScanningAlert,
            error_models={
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )

    @overload
    async def async_update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        data: ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBodyType,
    ) -> "Response[SecretScanningAlert]":
        ...

    @overload
    async def async_update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        data: Unset = UNSET,
        state: Literal["open", "resolved"],
        resolution: Union[
            Unset,
            Union[
                None, Literal["false_positive", "wont_fix", "revoked", "used_in_tests"]
            ],
        ] = UNSET,
    ) -> "Response[SecretScanningAlert]":
        ...

    async def async_update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        data: Union[
            Unset, ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBodyType
        ] = UNSET,
        **kwargs,
    ) -> "Response[SecretScanningAlert]":
        url = f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(
            ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBody, json
        )
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PATCH",
            url,
            json=exclude_unset(json),
            response_model=SecretScanningAlert,
            error_models={
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )

    def list_locations_for_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        page: Union[Unset, int] = 1,
        per_page: Union[Unset, int] = 30,
    ) -> "Response[List[SecretScanningLocation]]":
        url = f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}/locations"

        params = {
            "page": page,
            "per_page": per_page,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[SecretScanningLocation],
            error_models={
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )

    async def async_list_locations_for_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        page: Union[Unset, int] = 1,
        per_page: Union[Unset, int] = 30,
    ) -> "Response[List[SecretScanningLocation]]":
        url = f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}/locations"

        params = {
            "page": page,
            "per_page": per_page,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[SecretScanningLocation],
            error_models={
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )