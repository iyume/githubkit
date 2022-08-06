"""DO NOT EDIT THIS FILE!

This file is auto generated by github rest api discription.
See https://github.com/github/rest-api-description for more information.
"""


from datetime import datetime
from typing import TYPE_CHECKING, List, Union, Literal, overload

from pydantic import BaseModel, parse_obj_as

from githubkit.utils import UNSET, Unset, exclude_unset

from .types import (
    ReposOwnerRepoCodeScanningSarifsPostBodyType,
    ReposOwnerRepoCodeScanningAlertsAlertNumberPatchBodyType,
)
from .models import (
    BasicError,
    CodeScanningAlert,
    CodeScanningAnalysis,
    CodeScanningAlertItems,
    CodeScanningSarifsStatus,
    CodeScanningAlertInstance,
    CodeScanningSarifsReceipt,
    CodeScanningAnalysisDeletion,
    CodeScanningOrganizationAlertItems,
    ReposOwnerRepoCodeScanningSarifsPostBody,
    ReposOwnerRepoCodeScanningAlertsAlertNumberPatchBody,
    EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
)

if TYPE_CHECKING:
    from githubkit import GitHub
    from githubkit.response import Response


class CodeScanningClient:
    def __init__(self, github: "GitHub"):
        self._github = github

    def list_alerts_for_enterprise(
        self,
        enterprise: str,
        tool_name: Union[Unset, str] = UNSET,
        tool_guid: Union[Unset, Union[str, None]] = UNSET,
        before: Union[Unset, str] = UNSET,
        after: Union[Unset, str] = UNSET,
        page: Union[Unset, int] = 1,
        per_page: Union[Unset, int] = 30,
        direction: Union[Unset, Literal["asc", "desc"]] = "desc",
        state: Union[Unset, Literal["open", "closed", "dismissed", "fixed"]] = UNSET,
        sort: Union[Unset, Literal["created", "updated"]] = "created",
    ) -> "Response[List[CodeScanningOrganizationAlertItems]]":
        url = f"/enterprises/{enterprise}/code-scanning/alerts"

        params = {
            "tool_name": tool_name,
            "tool_guid": tool_guid,
            "before": before,
            "after": after,
            "page": page,
            "per_page": per_page,
            "direction": direction,
            "state": state,
            "sort": sort,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[CodeScanningOrganizationAlertItems],
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )

    async def async_list_alerts_for_enterprise(
        self,
        enterprise: str,
        tool_name: Union[Unset, str] = UNSET,
        tool_guid: Union[Unset, Union[str, None]] = UNSET,
        before: Union[Unset, str] = UNSET,
        after: Union[Unset, str] = UNSET,
        page: Union[Unset, int] = 1,
        per_page: Union[Unset, int] = 30,
        direction: Union[Unset, Literal["asc", "desc"]] = "desc",
        state: Union[Unset, Literal["open", "closed", "dismissed", "fixed"]] = UNSET,
        sort: Union[Unset, Literal["created", "updated"]] = "created",
    ) -> "Response[List[CodeScanningOrganizationAlertItems]]":
        url = f"/enterprises/{enterprise}/code-scanning/alerts"

        params = {
            "tool_name": tool_name,
            "tool_guid": tool_guid,
            "before": before,
            "after": after,
            "page": page,
            "per_page": per_page,
            "direction": direction,
            "state": state,
            "sort": sort,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[CodeScanningOrganizationAlertItems],
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )

    def list_alerts_for_org(
        self,
        org: str,
        tool_name: Union[Unset, str] = UNSET,
        tool_guid: Union[Unset, Union[str, None]] = UNSET,
        before: Union[Unset, str] = UNSET,
        after: Union[Unset, str] = UNSET,
        page: Union[Unset, int] = 1,
        per_page: Union[Unset, int] = 30,
        direction: Union[Unset, Literal["asc", "desc"]] = "desc",
        state: Union[Unset, Literal["open", "closed", "dismissed", "fixed"]] = UNSET,
        sort: Union[Unset, Literal["created", "updated"]] = "created",
    ) -> "Response[List[CodeScanningOrganizationAlertItems]]":
        url = f"/orgs/{org}/code-scanning/alerts"

        params = {
            "tool_name": tool_name,
            "tool_guid": tool_guid,
            "before": before,
            "after": after,
            "page": page,
            "per_page": per_page,
            "direction": direction,
            "state": state,
            "sort": sort,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[CodeScanningOrganizationAlertItems],
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )

    async def async_list_alerts_for_org(
        self,
        org: str,
        tool_name: Union[Unset, str] = UNSET,
        tool_guid: Union[Unset, Union[str, None]] = UNSET,
        before: Union[Unset, str] = UNSET,
        after: Union[Unset, str] = UNSET,
        page: Union[Unset, int] = 1,
        per_page: Union[Unset, int] = 30,
        direction: Union[Unset, Literal["asc", "desc"]] = "desc",
        state: Union[Unset, Literal["open", "closed", "dismissed", "fixed"]] = UNSET,
        sort: Union[Unset, Literal["created", "updated"]] = "created",
    ) -> "Response[List[CodeScanningOrganizationAlertItems]]":
        url = f"/orgs/{org}/code-scanning/alerts"

        params = {
            "tool_name": tool_name,
            "tool_guid": tool_guid,
            "before": before,
            "after": after,
            "page": page,
            "per_page": per_page,
            "direction": direction,
            "state": state,
            "sort": sort,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[CodeScanningOrganizationAlertItems],
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )

    def list_alerts_for_repo(
        self,
        owner: str,
        repo: str,
        tool_name: Union[Unset, str] = UNSET,
        tool_guid: Union[Unset, Union[str, None]] = UNSET,
        page: Union[Unset, int] = 1,
        per_page: Union[Unset, int] = 30,
        ref: Union[Unset, str] = UNSET,
        direction: Union[Unset, Literal["asc", "desc"]] = "desc",
        sort: Union[Unset, Literal["created", "updated"]] = "created",
        state: Union[Unset, Literal["open", "closed", "dismissed", "fixed"]] = UNSET,
    ) -> "Response[List[CodeScanningAlertItems]]":
        url = f"/repos/{owner}/{repo}/code-scanning/alerts"

        params = {
            "tool_name": tool_name,
            "tool_guid": tool_guid,
            "page": page,
            "per_page": per_page,
            "ref": ref,
            "direction": direction,
            "sort": sort,
            "state": state,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[CodeScanningAlertItems],
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )

    async def async_list_alerts_for_repo(
        self,
        owner: str,
        repo: str,
        tool_name: Union[Unset, str] = UNSET,
        tool_guid: Union[Unset, Union[str, None]] = UNSET,
        page: Union[Unset, int] = 1,
        per_page: Union[Unset, int] = 30,
        ref: Union[Unset, str] = UNSET,
        direction: Union[Unset, Literal["asc", "desc"]] = "desc",
        sort: Union[Unset, Literal["created", "updated"]] = "created",
        state: Union[Unset, Literal["open", "closed", "dismissed", "fixed"]] = UNSET,
    ) -> "Response[List[CodeScanningAlertItems]]":
        url = f"/repos/{owner}/{repo}/code-scanning/alerts"

        params = {
            "tool_name": tool_name,
            "tool_guid": tool_guid,
            "page": page,
            "per_page": per_page,
            "ref": ref,
            "direction": direction,
            "sort": sort,
            "state": state,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[CodeScanningAlertItems],
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )

    def get_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
    ) -> "Response[CodeScanningAlert]":
        url = f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}"

        return self._github.request(
            "GET",
            url,
            response_model=CodeScanningAlert,
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )

    async def async_get_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
    ) -> "Response[CodeScanningAlert]":
        url = f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}"

        return await self._github.arequest(
            "GET",
            url,
            response_model=CodeScanningAlert,
            error_models={
                "403": BasicError,
                "404": BasicError,
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
        data: ReposOwnerRepoCodeScanningAlertsAlertNumberPatchBodyType,
    ) -> "Response[CodeScanningAlert]":
        ...

    @overload
    def update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        data: Unset = UNSET,
        state: Literal["open", "dismissed"],
        dismissed_reason: Union[
            Unset, Union[None, Literal["false positive", "won't fix", "used in tests"]]
        ] = UNSET,
        dismissed_comment: Union[Unset, Union[str, None]] = UNSET,
    ) -> "Response[CodeScanningAlert]":
        ...

    def update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        data: Union[
            Unset, ReposOwnerRepoCodeScanningAlertsAlertNumberPatchBodyType
        ] = UNSET,
        **kwargs,
    ) -> "Response[CodeScanningAlert]":
        url = f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(ReposOwnerRepoCodeScanningAlertsAlertNumberPatchBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PATCH",
            url,
            json=exclude_unset(json),
            response_model=CodeScanningAlert,
            error_models={
                "403": BasicError,
                "404": BasicError,
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
        data: ReposOwnerRepoCodeScanningAlertsAlertNumberPatchBodyType,
    ) -> "Response[CodeScanningAlert]":
        ...

    @overload
    async def async_update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        data: Unset = UNSET,
        state: Literal["open", "dismissed"],
        dismissed_reason: Union[
            Unset, Union[None, Literal["false positive", "won't fix", "used in tests"]]
        ] = UNSET,
        dismissed_comment: Union[Unset, Union[str, None]] = UNSET,
    ) -> "Response[CodeScanningAlert]":
        ...

    async def async_update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        data: Union[
            Unset, ReposOwnerRepoCodeScanningAlertsAlertNumberPatchBodyType
        ] = UNSET,
        **kwargs,
    ) -> "Response[CodeScanningAlert]":
        url = f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(ReposOwnerRepoCodeScanningAlertsAlertNumberPatchBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PATCH",
            url,
            json=exclude_unset(json),
            response_model=CodeScanningAlert,
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )

    def list_alert_instances(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        page: Union[Unset, int] = 1,
        per_page: Union[Unset, int] = 30,
        ref: Union[Unset, str] = UNSET,
    ) -> "Response[List[CodeScanningAlertInstance]]":
        url = f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/instances"

        params = {
            "page": page,
            "per_page": per_page,
            "ref": ref,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[CodeScanningAlertInstance],
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )

    async def async_list_alert_instances(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        page: Union[Unset, int] = 1,
        per_page: Union[Unset, int] = 30,
        ref: Union[Unset, str] = UNSET,
    ) -> "Response[List[CodeScanningAlertInstance]]":
        url = f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/instances"

        params = {
            "page": page,
            "per_page": per_page,
            "ref": ref,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[CodeScanningAlertInstance],
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )

    def list_recent_analyses(
        self,
        owner: str,
        repo: str,
        tool_name: Union[Unset, str] = UNSET,
        tool_guid: Union[Unset, Union[str, None]] = UNSET,
        page: Union[Unset, int] = 1,
        per_page: Union[Unset, int] = 30,
        ref: Union[Unset, str] = UNSET,
        sarif_id: Union[Unset, str] = UNSET,
    ) -> "Response[List[CodeScanningAnalysis]]":
        url = f"/repos/{owner}/{repo}/code-scanning/analyses"

        params = {
            "tool_name": tool_name,
            "tool_guid": tool_guid,
            "page": page,
            "per_page": per_page,
            "ref": ref,
            "sarif_id": sarif_id,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[CodeScanningAnalysis],
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )

    async def async_list_recent_analyses(
        self,
        owner: str,
        repo: str,
        tool_name: Union[Unset, str] = UNSET,
        tool_guid: Union[Unset, Union[str, None]] = UNSET,
        page: Union[Unset, int] = 1,
        per_page: Union[Unset, int] = 30,
        ref: Union[Unset, str] = UNSET,
        sarif_id: Union[Unset, str] = UNSET,
    ) -> "Response[List[CodeScanningAnalysis]]":
        url = f"/repos/{owner}/{repo}/code-scanning/analyses"

        params = {
            "tool_name": tool_name,
            "tool_guid": tool_guid,
            "page": page,
            "per_page": per_page,
            "ref": ref,
            "sarif_id": sarif_id,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[CodeScanningAnalysis],
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )

    def get_analysis(
        self,
        owner: str,
        repo: str,
        analysis_id: int,
    ) -> "Response[CodeScanningAnalysis]":
        url = f"/repos/{owner}/{repo}/code-scanning/analyses/{analysis_id}"

        return self._github.request(
            "GET",
            url,
            response_model=CodeScanningAnalysis,
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )

    async def async_get_analysis(
        self,
        owner: str,
        repo: str,
        analysis_id: int,
    ) -> "Response[CodeScanningAnalysis]":
        url = f"/repos/{owner}/{repo}/code-scanning/analyses/{analysis_id}"

        return await self._github.arequest(
            "GET",
            url,
            response_model=CodeScanningAnalysis,
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )

    def delete_analysis(
        self,
        owner: str,
        repo: str,
        analysis_id: int,
        confirm_delete: Union[Unset, Union[str, None]] = UNSET,
    ) -> "Response[CodeScanningAnalysisDeletion]":
        url = f"/repos/{owner}/{repo}/code-scanning/analyses/{analysis_id}"

        params = {
            "confirm_delete": confirm_delete,
        }

        return self._github.request(
            "DELETE",
            url,
            params=exclude_unset(params),
            response_model=CodeScanningAnalysisDeletion,
            error_models={
                "400": BasicError,
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )

    async def async_delete_analysis(
        self,
        owner: str,
        repo: str,
        analysis_id: int,
        confirm_delete: Union[Unset, Union[str, None]] = UNSET,
    ) -> "Response[CodeScanningAnalysisDeletion]":
        url = f"/repos/{owner}/{repo}/code-scanning/analyses/{analysis_id}"

        params = {
            "confirm_delete": confirm_delete,
        }

        return await self._github.arequest(
            "DELETE",
            url,
            params=exclude_unset(params),
            response_model=CodeScanningAnalysisDeletion,
            error_models={
                "400": BasicError,
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )

    @overload
    def upload_sarif(
        self,
        owner: str,
        repo: str,
        *,
        data: ReposOwnerRepoCodeScanningSarifsPostBodyType,
    ) -> "Response[CodeScanningSarifsReceipt]":
        ...

    @overload
    def upload_sarif(
        self,
        owner: str,
        repo: str,
        *,
        data: Unset = UNSET,
        commit_sha: str,
        ref: str,
        sarif: str,
        checkout_uri: Union[Unset, str] = UNSET,
        started_at: Union[Unset, datetime] = UNSET,
        tool_name: Union[Unset, str] = UNSET,
    ) -> "Response[CodeScanningSarifsReceipt]":
        ...

    def upload_sarif(
        self,
        owner: str,
        repo: str,
        *,
        data: Union[Unset, ReposOwnerRepoCodeScanningSarifsPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[CodeScanningSarifsReceipt]":
        url = f"/repos/{owner}/{repo}/code-scanning/sarifs"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(ReposOwnerRepoCodeScanningSarifsPostBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=CodeScanningSarifsReceipt,
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )

    @overload
    async def async_upload_sarif(
        self,
        owner: str,
        repo: str,
        *,
        data: ReposOwnerRepoCodeScanningSarifsPostBodyType,
    ) -> "Response[CodeScanningSarifsReceipt]":
        ...

    @overload
    async def async_upload_sarif(
        self,
        owner: str,
        repo: str,
        *,
        data: Unset = UNSET,
        commit_sha: str,
        ref: str,
        sarif: str,
        checkout_uri: Union[Unset, str] = UNSET,
        started_at: Union[Unset, datetime] = UNSET,
        tool_name: Union[Unset, str] = UNSET,
    ) -> "Response[CodeScanningSarifsReceipt]":
        ...

    async def async_upload_sarif(
        self,
        owner: str,
        repo: str,
        *,
        data: Union[Unset, ReposOwnerRepoCodeScanningSarifsPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[CodeScanningSarifsReceipt]":
        url = f"/repos/{owner}/{repo}/code-scanning/sarifs"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(ReposOwnerRepoCodeScanningSarifsPostBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=CodeScanningSarifsReceipt,
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )

    def get_sarif(
        self,
        owner: str,
        repo: str,
        sarif_id: str,
    ) -> "Response[CodeScanningSarifsStatus]":
        url = f"/repos/{owner}/{repo}/code-scanning/sarifs/{sarif_id}"

        return self._github.request(
            "GET",
            url,
            response_model=CodeScanningSarifsStatus,
            error_models={
                "403": BasicError,
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )

    async def async_get_sarif(
        self,
        owner: str,
        repo: str,
        sarif_id: str,
    ) -> "Response[CodeScanningSarifsStatus]":
        url = f"/repos/{owner}/{repo}/code-scanning/sarifs/{sarif_id}"

        return await self._github.arequest(
            "GET",
            url,
            response_model=CodeScanningSarifsStatus,
            error_models={
                "403": BasicError,
                "503": EnterprisesEnterpriseCodeScanningAlertsGetResponse503,
            },
        )