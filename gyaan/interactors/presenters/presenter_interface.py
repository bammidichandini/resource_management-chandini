from abc import ABC
from abc import abstractmethod
from gyaan.dtos.dtos import (
    DomainDto,
    CompletePostDetails,
    DomainDetailsWithPosts
)
from gyaan.exceptions.exceptions import (
    InvalidPostIds
)


class PresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_domain_id(self):
        pass

    @abstractmethod
    def get_domain_details_response(self, domain_dtos: DomainDto):
        pass

    @abstractmethod
    def raise_user_not_following(self):
        pass

    @abstractmethod
    def get_posts_response(self, post_dtos: CompletePostDetails):
        pass

    @abstractmethod
    def raise_invalid_post_ids(self, error: InvalidPostIds):
        pass

    @abstractmethod
    def get_domain_posts_response(
        self,
        complete_post_details: CompletePostDetails
    ):
        pass

    @abstractmethod
    def raise_invalid_input(self):
        pass

    @abstractmethod
    def get_domain_with_posts_response(self, domain_with_posts_dto: DomainDetailsWithPosts):
        pass
