from typing_extensions import Self
from typing import Any, Union, Optional
from dataclasses import asdict, dataclass

import httpx

from .retry import RETRY_DEFAULT
from .typing import RetryDecisionFunc
from .cache import DEFAULT_CACHE_STRATEGY, BaseCacheStrategy


@dataclass(frozen=True)
class Config:
    base_url: httpx.URL
    accept: str
    user_agent: str
    follow_redirects: bool
    timeout: httpx.Timeout
    cache_strategy: BaseCacheStrategy
    http_cache: bool
    auto_retry: Optional[RetryDecisionFunc]
    rest_api_validate_body: bool

    def dict(self) -> dict[str, Any]:
        return asdict(self)

    def copy(self) -> Self:
        return self.__class__(**self.dict())


def build_base_url(base_url: Optional[Union[str, httpx.URL]]) -> httpx.URL:
    base_url = base_url or httpx.URL("https://api.github.com/")
    base_url = base_url if isinstance(base_url, httpx.URL) else httpx.URL(base_url)
    # enforce trailing slash
    if not base_url.raw_path.endswith(b"/"):
        base_url = base_url.copy_with(raw_path=base_url.raw_path + b"/")
    return base_url


def build_accept(
    accept_format: Optional[str] = None, previews: Optional[list[str]] = None
) -> str:
    if accept_format:
        accept_format = (
            accept_format if accept_format.startswith(".") else f".{accept_format}"
        )
    accept_format = accept_format or "+json"

    if previews:
        accepts = [
            f"application/vnd.github.{preview}-preview{accept_format}"
            for preview in previews
        ]
    else:
        accepts = [f"application/vnd.github{accept_format}"]
    return ",".join(accepts)


def build_user_agent(user_agent: Optional[str] = None) -> str:
    return user_agent or "GitHubKit/Python"


def build_timeout(
    timeout: Optional[Union[float, httpx.Timeout]] = None,
) -> httpx.Timeout:
    return timeout if isinstance(timeout, httpx.Timeout) else httpx.Timeout(timeout)


def build_cache_strategy(
    cache_strategy: Optional[BaseCacheStrategy],
) -> BaseCacheStrategy:
    return cache_strategy or DEFAULT_CACHE_STRATEGY


def build_auto_retry(
    auto_retry: Union[bool, RetryDecisionFunc] = True,
) -> Optional[RetryDecisionFunc]:
    if auto_retry is True:
        return RETRY_DEFAULT
    elif auto_retry:
        return auto_retry
    else:
        return None


def get_config(
    *,
    base_url: Optional[Union[str, httpx.URL]] = None,
    accept_format: Optional[str] = None,
    previews: Optional[list[str]] = None,
    user_agent: Optional[str] = None,
    follow_redirects: bool = True,
    timeout: Optional[Union[float, httpx.Timeout]] = None,
    cache_strategy: Optional[BaseCacheStrategy] = None,
    http_cache: bool = True,
    auto_retry: Union[bool, RetryDecisionFunc] = True,
    rest_api_validate_body: bool = True,
) -> Config:
    return Config(
        build_base_url(base_url),
        build_accept(accept_format, previews),
        build_user_agent(user_agent),
        follow_redirects,
        build_timeout(timeout),
        build_cache_strategy(cache_strategy),
        http_cache,
        build_auto_retry(auto_retry),
        rest_api_validate_body,
    )
