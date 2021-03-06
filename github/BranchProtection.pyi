from typing import Any, Dict

from github.PaginatedList import PaginatedList
from github.RequiredPullRequestReviews import RequiredPullRequestReviews
from github.RequiredStatusChecks import RequiredStatusChecks

class BranchProtection:
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def enforce_admins(self) -> bool: ...
    def get_team_push_restrictions(self) -> PaginatedList: ...
    def get_user_push_restrictions(self) -> PaginatedList: ...
    @property
    def required_pull_request_reviews(self) -> RequiredPullRequestReviews: ...
    @property
    def required_status_checks(self) -> RequiredStatusChecks: ...
    @property
    def url(self) -> str: ...
