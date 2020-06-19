from gyaan.exceptions.exceptions import (
    InvalidDomainId,
    UserNotFollowing,
    InvalidInput
)
from gyaan.interactors.domain_details import \
            DomainDetailsInteractor
from gyaan.interactors.domain_posts import \
            DomainPostsInteractor
from gyaan.dtos.dtos import DomainDetailsWithPosts
from gyaan.interactors.presenters.presenter_interface import PresenterInterface
from gyaan.interactors.storages.storage_interface import StorageInterface


class DomainWithPostsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_domain_with_posts_wrapper(self, user_id: int, domain_id: int,
                                      offset: int, limit: int,
                                      presenter: PresenterInterface):

        try:
            return self._get_domain_with_posts_response(
                user_id=user_id, domain_id=domain_id,
                offset=offset, limit=limit,
                presenter=presenter
            )
        except InvalidDomainId:
            presenter.raise_invalid_domain_id()
        except UserNotFollowing:
            presenter.raise_user_not_following()
        except InvalidInput:
            presenter.raise_invalid_input()


    def _get_domain_with_posts_response(self, user_id: int, domain_id: int,
                                        offset: int, limit: int,
                                        presenter: PresenterInterface):

        domain_with_posts_dto = self.get_domain_with_posts(
            user_id=user_id,
            domain_id=domain_id,
            offset=offset,
            limit=limit
        )

        return presenter.get_domain_with_posts_response(domain_with_posts_dto)

    def get_domain_with_posts(self, user_id: int, domain_id: int,
                              offset: int, limit: int):

        domain_details_interactor = DomainDetailsInteractor(
            storage=self.storage
        )

        domain_details = domain_details_interactor.get_domain_details(
            user_id=user_id,
            domain_id=domain_id
        )

        domain_posts_interactor = DomainPostsInteractor(
            storage=self.storage
        )
        domain_posts = domain_posts_interactor.get_domain_posts(
            user_id=user_id,
            domain_id=domain_id,
            offset=offset,
            limit=limit
        )

        return DomainDetailsWithPosts(
            domain_details=domain_details,
            post_details=domain_posts
        )
