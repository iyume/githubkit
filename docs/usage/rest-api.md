<!-- markdownlint-disable MD046 -->

# Calling REST API

GitHub's REST API enables you to build automation processes, integrate with GitHub and extend GitHub. See the [GitHub REST API documentation](https://docs.github.com/en/rest) for more information.

> APIs are fully typed. Type hints in the following examples are just for reference only.

## The Basics

Calling REST API is simple with githubkit. You just need to create a `GitHub` instance with your authentication strategy and call the REST API methods in categories. For example, to get a repository:

=== "Sync"

    ```python hl_lines="5"
    from githubkit import GitHub, Response
    from githubkit.versions.latest.models import FullRepository

    github = GitHub("<your_token_here>")
    resp: Response[FullRepository] = github.rest.repos.get("owner", "repo")
    repo: FullRepository = resp.parsed_data
    ```

=== "Async"

    ```python hl_lines="5"
    from githubkit import Response
    from githubkit.versions.latest.models import FullRepository

    github = GitHub("<your_token_here>")
    resp: Response[FullRepository] = await github.rest.repos.async_get("owner", "repo")
    repo: FullRepository = resp.parsed_data
    ```

If you are calling an API that requires request body parameters, you can pass the request body as a keyword argument:

=== "Sync"

    ```python hl_lines="5-10"
    from githubkit import GitHub, Response
    from githubkit.versions.latest.models import Issue

    github = GitHub("<your_token_here>")
    resp: Response[Issue] = github.rest.issues.create(
        "owner",
        "repo",
        title="New Issue",
        body="This is issue body",
    )
    issue: Issue = resp.parsed_data
    ```

=== "Async"

    ```python hl_lines="5-10"
    from githubkit import GitHub, Response
    from githubkit.versions.latest.models import Issue

    github = GitHub("<your_token_here>")
    resp: Response[Issue] = await github.rest.issues.async_create(
        "owner",
        "repo",
        title="New Issue",
        body="This is issue body",
    )
    issue: Issue = resp.parsed_data
    ```

Or you can pass the request body as a dictionary:

=== "Sync"

    ```python hl_lines="8"
    from githubkit import GitHub, Response
    from githubkit.versions.latest.models import Issue

    github = GitHub("<your_token_here>")
    resp: Response[Issue] = github.rest.issues.create(
        "owner",
        "repo",
        data={"title": "New Issue", "body": "This is issue body"},
    )
    issue: Issue = resp.parsed_data
    ```

=== "Async"

    ```python hl_lines="8"
    from githubkit import GitHub, Response
    from githubkit.versions.latest.models import Issue

    github = GitHub("<your_token_here>")
    resp: Response[Issue] = await github.rest.issues.async_create(
        "owner",
        "repo",
        data={"title": "New Issue", "body": "This is issue body"},
    )
    issue: Issue = resp.parsed_data
    ```

!!! danger

    Note that you should hold a **strong reference** to the githubkit client instance. Otherwise, githubkit client will fail to call the request.
    For example, you should not do this:

    ```python
    from githubkit import GitHub

    def get_client() -> GitHub:
        return GitHub()

    # This will cause error
    get_client().rest.repos.get("owner", "repo")

    # This is ok
    client = get_client()
    client.rest.repos.get("owner", "repo")
    ```

## Reusing Client

You can make multiple requests with the same client instance in one context:

=== "Sync"

    ```python hl_lines="4"
    from githubkit import GitHub, Response
    from githubkit.versions.latest.models import FullRepository

    with GitHub("<your_token_here>") as github:
        resp: Response[FullRepository] = github.rest.repos.get(owner="owner", repo="repo")
        repo: FullRepository = resp.parsed_data
    ```

=== "Async"

    ```python hl_lines="4"
    from githubkit import GitHub, Response
    from githubkit.versions.latest.models import FullRepository

    async with GitHub("<your_token_here>") as github:
        resp: Response[FullRepository] = await github.rest.repos.async_get(owner="owner", repo="repo")
        repo: FullRepository = resp.parsed_data
    ```

## Data Validation

As shown above, the response data is parsed and validated by accessing the `response.parsed_data` property. This ensures that the data type returned by the API is as expected and your code is safe to use it (with static type checking). But sometimes you may want to get the raw data returned by the API, such as when the schema is not correct. You can use the `response.text` property or `response.json()` method to get the raw data:

```python hl_lines="5"
from typing import Any, Dict
from githubkit import Response

resp: Response[FullRepository] = github.rest.repos.get("owner", "repo")
repo: Dict[str, Any] = resp.json()
```

## REST API Versioning

githubkit supports multiple versions of GitHub API, you can switch between versions as follows:

```python
github.rest("2022-11-28").repos.get("owner", "repo")
```

The code above uses the `2022-11-28` version of the GitHub API.

Besides the REST API methods, the versioned models can also be imported from `githubkit.versions.<version>.models` module. For example:

```python
from githubkit.versions.v2022_11_28.models import FullRepository
```

Specially, the `latest` module is always linked to the latest version of GitHub API:

```python
from githubkit.versions.latest.models import FullRepository
```

!!! note

    For backward compatibility, the `githubkit.rest` module is linked to the models of `latest` version by default.

    ```python
    from githubkit.rest import FullRepository
    ```

You can also get the latest version name of GitHub API and version-module mapping of GitHub API:

```python
from githubkit.versions import LATEST_VERSION, VERSIONS
```

Current supported versions are: (you can find it in the section `[[tool.codegen.descriptions]]` of the `pyproject.toml` file)

- 2022-11-28 (latest)
- ghec-2022-11-28

## REST API Pagination

When a response from the REST API would include many results, GitHub will paginate the results and return a subset of the results. In this case, some APIs provide `page` and `per_page` parameters to control the pagination. See [GitHub Docs - Using pagination in the REST API](https://docs.github.com/en/rest/using-the-rest-api/using-pagination-in-the-rest-api) for more information.

githubkit provides a built-in pagination feature to handle this. You can use the `github.paginate` method to iterate over all the results:

> Pagination typing is checked with Pylance ([Pyright](https://github.com/microsoft/pyright)).

=== "Sync"

    ```python hl_lines="3-5"
    from githubkit.versions.latest.models import Issue

    for issue in github.paginate(
        github.rest.issues.list_for_repo, owner="owner", repo="repo", state="open"
    ):
        issue: Issue
        print(issue.number)
    ```

=== "Async"

    ```python hl_lines="3-5"
    from githubkit.versions.latest.models import Issue

    async for issue in github.paginate(
        github.rest.issues.async_list_for_repo, owner="owner", repo="repo", state="open"
    ):
        issue: Issue
        print(issue.number)
    ```

You can also provide a custom map function to handle complex pagination (such as when the API returns data in a nested field):

=== "Sync"

    ```python hl_lines="5"
    from githubkit.versions.latest.models import Repository

    for accessible_repo in github.paginate(
        github.rest.apps.list_installation_repos_for_authenticated_user,
        map_func=lambda r: r.parsed_data.repositories,
        installation_id=1,
    ):
        accessible_repo: Repository
        print(accessible_repo.full_name)
    ```

=== "Async"

    ```python hl_lines="5"
    from githubkit.versions.latest.models import Repository

    async for accessible_repo in github.paginate(
        github.rest.apps.async_list_installation_repos_for_authenticated_user,
        map_func=lambda r: r.parsed_data.repositories,
        installation_id=1,
    ):
        accessible_repo: Repository
        print(accessible_repo.full_name)
    ```