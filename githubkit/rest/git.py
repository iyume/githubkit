"""DO NOT EDIT THIS FILE!

This file is auto generated by github rest api discription.
See https://github.com/github/rest-api-description for more information.
"""


from typing import TYPE_CHECKING, List, Union, Literal, overload

from pydantic import BaseModel, parse_obj_as

from githubkit.utils import UNSET, Unset, exclude_unset

from .models import (
    Blob,
    GitRef,
    GitTag,
    GitTree,
    GitCommit,
    ShortBlob,
    BasicError,
    ValidationError,
    ReposOwnerRepoGitRefsPostBody,
    ReposOwnerRepoGitTagsPostBody,
    ReposOwnerRepoGitBlobsPostBody,
    ReposOwnerRepoGitTreesPostBody,
    ReposOwnerRepoGitCommitsPostBody,
    ReposOwnerRepoGitRefsRefPatchBody,
)
from .types import (
    ReposOwnerRepoGitRefsPostBodyType,
    ReposOwnerRepoGitTagsPostBodyType,
    ReposOwnerRepoGitBlobsPostBodyType,
    ReposOwnerRepoGitTreesPostBodyType,
    ReposOwnerRepoGitCommitsPostBodyType,
    ReposOwnerRepoGitRefsRefPatchBodyType,
    ReposOwnerRepoGitTagsPostBodyPropTaggerType,
    ReposOwnerRepoGitCommitsPostBodyPropAuthorType,
    ReposOwnerRepoGitTreesPostBodyPropTreeItemsType,
    ReposOwnerRepoGitCommitsPostBodyPropCommitterType,
)

if TYPE_CHECKING:
    from githubkit import GitHub
    from githubkit.response import Response


class GitClient:
    def __init__(self, github: "GitHub"):
        self._github = github

    @overload
    def create_blob(
        self, owner: str, repo: str, *, data: ReposOwnerRepoGitBlobsPostBodyType
    ) -> "Response[ShortBlob]":
        ...

    @overload
    def create_blob(
        self,
        owner: str,
        repo: str,
        *,
        data: Unset = UNSET,
        content: str,
        encoding: Union[Unset, str] = "utf-8",
    ) -> "Response[ShortBlob]":
        ...

    def create_blob(
        self,
        owner: str,
        repo: str,
        *,
        data: Union[Unset, ReposOwnerRepoGitBlobsPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[ShortBlob]":
        url = f"/repos/{owner}/{repo}/git/blobs"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(ReposOwnerRepoGitBlobsPostBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=ShortBlob,
            error_models={
                "404": BasicError,
                "409": BasicError,
                "403": BasicError,
                "422": ValidationError,
            },
        )

    @overload
    async def async_create_blob(
        self, owner: str, repo: str, *, data: ReposOwnerRepoGitBlobsPostBodyType
    ) -> "Response[ShortBlob]":
        ...

    @overload
    async def async_create_blob(
        self,
        owner: str,
        repo: str,
        *,
        data: Unset = UNSET,
        content: str,
        encoding: Union[Unset, str] = "utf-8",
    ) -> "Response[ShortBlob]":
        ...

    async def async_create_blob(
        self,
        owner: str,
        repo: str,
        *,
        data: Union[Unset, ReposOwnerRepoGitBlobsPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[ShortBlob]":
        url = f"/repos/{owner}/{repo}/git/blobs"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(ReposOwnerRepoGitBlobsPostBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=ShortBlob,
            error_models={
                "404": BasicError,
                "409": BasicError,
                "403": BasicError,
                "422": ValidationError,
            },
        )

    def get_blob(
        self,
        owner: str,
        repo: str,
        file_sha: str,
    ) -> "Response[Blob]":
        url = f"/repos/{owner}/{repo}/git/blobs/{file_sha}"

        return self._github.request(
            "GET",
            url,
            response_model=Blob,
            error_models={
                "404": BasicError,
                "422": ValidationError,
                "403": BasicError,
            },
        )

    async def async_get_blob(
        self,
        owner: str,
        repo: str,
        file_sha: str,
    ) -> "Response[Blob]":
        url = f"/repos/{owner}/{repo}/git/blobs/{file_sha}"

        return await self._github.arequest(
            "GET",
            url,
            response_model=Blob,
            error_models={
                "404": BasicError,
                "422": ValidationError,
                "403": BasicError,
            },
        )

    @overload
    def create_commit(
        self, owner: str, repo: str, *, data: ReposOwnerRepoGitCommitsPostBodyType
    ) -> "Response[GitCommit]":
        ...

    @overload
    def create_commit(
        self,
        owner: str,
        repo: str,
        *,
        data: Unset = UNSET,
        message: str,
        tree: str,
        parents: Union[Unset, List[str]] = UNSET,
        author: Union[Unset, ReposOwnerRepoGitCommitsPostBodyPropAuthorType] = UNSET,
        committer: Union[
            Unset, ReposOwnerRepoGitCommitsPostBodyPropCommitterType
        ] = UNSET,
        signature: Union[Unset, str] = UNSET,
    ) -> "Response[GitCommit]":
        ...

    def create_commit(
        self,
        owner: str,
        repo: str,
        *,
        data: Union[Unset, ReposOwnerRepoGitCommitsPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[GitCommit]":
        url = f"/repos/{owner}/{repo}/git/commits"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(ReposOwnerRepoGitCommitsPostBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=GitCommit,
            error_models={
                "422": ValidationError,
                "404": BasicError,
            },
        )

    @overload
    async def async_create_commit(
        self, owner: str, repo: str, *, data: ReposOwnerRepoGitCommitsPostBodyType
    ) -> "Response[GitCommit]":
        ...

    @overload
    async def async_create_commit(
        self,
        owner: str,
        repo: str,
        *,
        data: Unset = UNSET,
        message: str,
        tree: str,
        parents: Union[Unset, List[str]] = UNSET,
        author: Union[Unset, ReposOwnerRepoGitCommitsPostBodyPropAuthorType] = UNSET,
        committer: Union[
            Unset, ReposOwnerRepoGitCommitsPostBodyPropCommitterType
        ] = UNSET,
        signature: Union[Unset, str] = UNSET,
    ) -> "Response[GitCommit]":
        ...

    async def async_create_commit(
        self,
        owner: str,
        repo: str,
        *,
        data: Union[Unset, ReposOwnerRepoGitCommitsPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[GitCommit]":
        url = f"/repos/{owner}/{repo}/git/commits"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(ReposOwnerRepoGitCommitsPostBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=GitCommit,
            error_models={
                "422": ValidationError,
                "404": BasicError,
            },
        )

    def get_commit(
        self,
        owner: str,
        repo: str,
        commit_sha: str,
    ) -> "Response[GitCommit]":
        url = f"/repos/{owner}/{repo}/git/commits/{commit_sha}"

        return self._github.request(
            "GET",
            url,
            response_model=GitCommit,
            error_models={
                "404": BasicError,
            },
        )

    async def async_get_commit(
        self,
        owner: str,
        repo: str,
        commit_sha: str,
    ) -> "Response[GitCommit]":
        url = f"/repos/{owner}/{repo}/git/commits/{commit_sha}"

        return await self._github.arequest(
            "GET",
            url,
            response_model=GitCommit,
            error_models={
                "404": BasicError,
            },
        )

    def list_matching_refs(
        self,
        owner: str,
        repo: str,
        ref: str,
        per_page: Union[Unset, int] = 30,
        page: Union[Unset, int] = 1,
    ) -> "Response[List[GitRef]]":
        url = f"/repos/{owner}/{repo}/git/matching-refs/{ref}"

        params = {
            "per_page": per_page,
            "page": page,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[GitRef],
        )

    async def async_list_matching_refs(
        self,
        owner: str,
        repo: str,
        ref: str,
        per_page: Union[Unset, int] = 30,
        page: Union[Unset, int] = 1,
    ) -> "Response[List[GitRef]]":
        url = f"/repos/{owner}/{repo}/git/matching-refs/{ref}"

        params = {
            "per_page": per_page,
            "page": page,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[GitRef],
        )

    def get_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
    ) -> "Response[GitRef]":
        url = f"/repos/{owner}/{repo}/git/ref/{ref}"

        return self._github.request(
            "GET",
            url,
            response_model=GitRef,
            error_models={
                "404": BasicError,
            },
        )

    async def async_get_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
    ) -> "Response[GitRef]":
        url = f"/repos/{owner}/{repo}/git/ref/{ref}"

        return await self._github.arequest(
            "GET",
            url,
            response_model=GitRef,
            error_models={
                "404": BasicError,
            },
        )

    @overload
    def create_ref(
        self, owner: str, repo: str, *, data: ReposOwnerRepoGitRefsPostBodyType
    ) -> "Response[GitRef]":
        ...

    @overload
    def create_ref(
        self,
        owner: str,
        repo: str,
        *,
        data: Unset = UNSET,
        ref: str,
        sha: str,
        key: Union[Unset, str] = UNSET,
    ) -> "Response[GitRef]":
        ...

    def create_ref(
        self,
        owner: str,
        repo: str,
        *,
        data: Union[Unset, ReposOwnerRepoGitRefsPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[GitRef]":
        url = f"/repos/{owner}/{repo}/git/refs"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(ReposOwnerRepoGitRefsPostBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=GitRef,
            error_models={
                "422": ValidationError,
            },
        )

    @overload
    async def async_create_ref(
        self, owner: str, repo: str, *, data: ReposOwnerRepoGitRefsPostBodyType
    ) -> "Response[GitRef]":
        ...

    @overload
    async def async_create_ref(
        self,
        owner: str,
        repo: str,
        *,
        data: Unset = UNSET,
        ref: str,
        sha: str,
        key: Union[Unset, str] = UNSET,
    ) -> "Response[GitRef]":
        ...

    async def async_create_ref(
        self,
        owner: str,
        repo: str,
        *,
        data: Union[Unset, ReposOwnerRepoGitRefsPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[GitRef]":
        url = f"/repos/{owner}/{repo}/git/refs"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(ReposOwnerRepoGitRefsPostBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=GitRef,
            error_models={
                "422": ValidationError,
            },
        )

    def delete_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
    ) -> "Response":
        url = f"/repos/{owner}/{repo}/git/refs/{ref}"

        return self._github.request(
            "DELETE",
            url,
            error_models={
                "422": ValidationError,
            },
        )

    async def async_delete_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
    ) -> "Response":
        url = f"/repos/{owner}/{repo}/git/refs/{ref}"

        return await self._github.arequest(
            "DELETE",
            url,
            error_models={
                "422": ValidationError,
            },
        )

    @overload
    def update_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        data: ReposOwnerRepoGitRefsRefPatchBodyType,
    ) -> "Response[GitRef]":
        ...

    @overload
    def update_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        data: Unset = UNSET,
        sha: str,
        force: Union[Unset, bool] = False,
    ) -> "Response[GitRef]":
        ...

    def update_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        data: Union[Unset, ReposOwnerRepoGitRefsRefPatchBodyType] = UNSET,
        **kwargs,
    ) -> "Response[GitRef]":
        url = f"/repos/{owner}/{repo}/git/refs/{ref}"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(ReposOwnerRepoGitRefsRefPatchBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PATCH",
            url,
            json=exclude_unset(json),
            response_model=GitRef,
            error_models={
                "422": ValidationError,
            },
        )

    @overload
    async def async_update_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        data: ReposOwnerRepoGitRefsRefPatchBodyType,
    ) -> "Response[GitRef]":
        ...

    @overload
    async def async_update_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        data: Unset = UNSET,
        sha: str,
        force: Union[Unset, bool] = False,
    ) -> "Response[GitRef]":
        ...

    async def async_update_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        *,
        data: Union[Unset, ReposOwnerRepoGitRefsRefPatchBodyType] = UNSET,
        **kwargs,
    ) -> "Response[GitRef]":
        url = f"/repos/{owner}/{repo}/git/refs/{ref}"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(ReposOwnerRepoGitRefsRefPatchBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PATCH",
            url,
            json=exclude_unset(json),
            response_model=GitRef,
            error_models={
                "422": ValidationError,
            },
        )

    @overload
    def create_tag(
        self, owner: str, repo: str, *, data: ReposOwnerRepoGitTagsPostBodyType
    ) -> "Response[GitTag]":
        ...

    @overload
    def create_tag(
        self,
        owner: str,
        repo: str,
        *,
        data: Unset = UNSET,
        tag: str,
        message: str,
        object_: str,
        type: Literal["commit", "tree", "blob"],
        tagger: Union[Unset, ReposOwnerRepoGitTagsPostBodyPropTaggerType] = UNSET,
    ) -> "Response[GitTag]":
        ...

    def create_tag(
        self,
        owner: str,
        repo: str,
        *,
        data: Union[Unset, ReposOwnerRepoGitTagsPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[GitTag]":
        url = f"/repos/{owner}/{repo}/git/tags"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(ReposOwnerRepoGitTagsPostBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=GitTag,
            error_models={
                "422": ValidationError,
            },
        )

    @overload
    async def async_create_tag(
        self, owner: str, repo: str, *, data: ReposOwnerRepoGitTagsPostBodyType
    ) -> "Response[GitTag]":
        ...

    @overload
    async def async_create_tag(
        self,
        owner: str,
        repo: str,
        *,
        data: Unset = UNSET,
        tag: str,
        message: str,
        object_: str,
        type: Literal["commit", "tree", "blob"],
        tagger: Union[Unset, ReposOwnerRepoGitTagsPostBodyPropTaggerType] = UNSET,
    ) -> "Response[GitTag]":
        ...

    async def async_create_tag(
        self,
        owner: str,
        repo: str,
        *,
        data: Union[Unset, ReposOwnerRepoGitTagsPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[GitTag]":
        url = f"/repos/{owner}/{repo}/git/tags"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(ReposOwnerRepoGitTagsPostBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=GitTag,
            error_models={
                "422": ValidationError,
            },
        )

    def get_tag(
        self,
        owner: str,
        repo: str,
        tag_sha: str,
    ) -> "Response[GitTag]":
        url = f"/repos/{owner}/{repo}/git/tags/{tag_sha}"

        return self._github.request(
            "GET",
            url,
            response_model=GitTag,
            error_models={
                "404": BasicError,
            },
        )

    async def async_get_tag(
        self,
        owner: str,
        repo: str,
        tag_sha: str,
    ) -> "Response[GitTag]":
        url = f"/repos/{owner}/{repo}/git/tags/{tag_sha}"

        return await self._github.arequest(
            "GET",
            url,
            response_model=GitTag,
            error_models={
                "404": BasicError,
            },
        )

    @overload
    def create_tree(
        self, owner: str, repo: str, *, data: ReposOwnerRepoGitTreesPostBodyType
    ) -> "Response[GitTree]":
        ...

    @overload
    def create_tree(
        self,
        owner: str,
        repo: str,
        *,
        data: Unset = UNSET,
        tree: List[ReposOwnerRepoGitTreesPostBodyPropTreeItemsType],
        base_tree: Union[Unset, str] = UNSET,
    ) -> "Response[GitTree]":
        ...

    def create_tree(
        self,
        owner: str,
        repo: str,
        *,
        data: Union[Unset, ReposOwnerRepoGitTreesPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[GitTree]":
        url = f"/repos/{owner}/{repo}/git/trees"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(ReposOwnerRepoGitTreesPostBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=GitTree,
            error_models={
                "422": ValidationError,
                "404": BasicError,
                "403": BasicError,
            },
        )

    @overload
    async def async_create_tree(
        self, owner: str, repo: str, *, data: ReposOwnerRepoGitTreesPostBodyType
    ) -> "Response[GitTree]":
        ...

    @overload
    async def async_create_tree(
        self,
        owner: str,
        repo: str,
        *,
        data: Unset = UNSET,
        tree: List[ReposOwnerRepoGitTreesPostBodyPropTreeItemsType],
        base_tree: Union[Unset, str] = UNSET,
    ) -> "Response[GitTree]":
        ...

    async def async_create_tree(
        self,
        owner: str,
        repo: str,
        *,
        data: Union[Unset, ReposOwnerRepoGitTreesPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[GitTree]":
        url = f"/repos/{owner}/{repo}/git/trees"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(ReposOwnerRepoGitTreesPostBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=GitTree,
            error_models={
                "422": ValidationError,
                "404": BasicError,
                "403": BasicError,
            },
        )

    def get_tree(
        self,
        owner: str,
        repo: str,
        tree_sha: str,
        recursive: Union[Unset, str] = UNSET,
    ) -> "Response[GitTree]":
        url = f"/repos/{owner}/{repo}/git/trees/{tree_sha}"

        params = {
            "recursive": recursive,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=GitTree,
            error_models={
                "422": ValidationError,
                "404": BasicError,
            },
        )

    async def async_get_tree(
        self,
        owner: str,
        repo: str,
        tree_sha: str,
        recursive: Union[Unset, str] = UNSET,
    ) -> "Response[GitTree]":
        url = f"/repos/{owner}/{repo}/git/trees/{tree_sha}"

        params = {
            "recursive": recursive,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=GitTree,
            error_models={
                "422": ValidationError,
                "404": BasicError,
            },
        )