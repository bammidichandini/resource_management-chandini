from abc import ABC
from abc import abstractmethod
from gyaan.dtos.dtos import (
    DomainDto,
    DomainStatsDto,
    UserDetailsDto,
    JoinRequestDto,
    PostDto,
    PostReactionsCount,
    PostCommentsCount,
    CommentDto,
    CommentReactionsCount,
    CommentRepliesCount,
    PostTagDetails
)
from typing import List


class StorageInterface(ABC):

    @abstractmethod
    def get_domain_dto(self, domain_id: int) -> DomainDto:
        pass

    @abstractmethod
    def is_user_following(
        self,
        domain_id: int,
        user_id: int
    ) -> bool:
        pass

    @abstractmethod
    def get_domain_stats(self, domain_id: int) -> DomainStatsDto:
        pass

    @abstractmethod
    def get_domain_expert_ids(self, domain_id: int) -> List[int]:
        pass

    @abstractmethod
    def get_expert_details(self, expert_ids: List[int]) -> List[UserDetailsDto]:
        pass

    @abstractmethod
    def is_user_expert(self, user_id: int, domain_id: int) -> bool:
        pass

    @abstractmethod
    def get_join_requests(self, domain_id: int) -> List[JoinRequestDto]:
        pass

    @abstractmethod
    def get_users_details(self, user_ids: List[int]) -> List[UserDetailsDto]:
        pass

    @abstractmethod
    def get_post_ids(self) -> List[int]:
        pass

    @abstractmethod
    def get_post_details(self, post_ids: List[int]) -> List[PostDto]:
        pass

    @abstractmethod
    def get_post_tags(self, post_ids: List[int]) -> List[PostTagDetails]:
        pass

    @abstractmethod
    def get_post_reactions_count(self, post_ids: List[int]) \
    -> List[PostReactionsCount]:
        pass

    @abstractmethod
    def get_comments_count(self, post_ids: List[int]) \
    -> List[PostCommentsCount]:
        pass

    @abstractmethod
    def get_comment_reactions_count(self, comment_ids: List[int]) \
    -> List[CommentReactionsCount]:
        pass

    @abstractmethod
    def get_comment_replies_count(self, comment_ids: List[int]) \
    -> List[CommentRepliesCount]:
        pass

    @abstractmethod
    def get_comment_details(self, comment_ids: List[int]) \
    -> List[CommentDto]:
        pass

    @abstractmethod
    def get_latest_comment_ids(self, post_id: int, no_of_comments: int) \
    -> List[int]:
        pass

    @abstractmethod
    def validate_domain_id(self, domain_id: int):
        pass

    @abstractmethod
    def get_domain_related_post_ids(
        self, domain_id: int,
        offset: int, limit:int
    ) -> List[int]:
        pass
