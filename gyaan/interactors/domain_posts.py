from gyaan.exceptions.exceptions import (
    InvalidDomainId,
    UserNotFollowing,
    InvalidInput
)
from gyaan.interactors.get_posts import GetPostsInteractor
from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.interactors.presenters.presenter_interface import PresenterInterface


class DomainPostsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage=storage

    def domain_posts_wrapper(
        self, user_id: int,
        domain_id: int,
        offset: int,
        limit: int,
        presenter: PresenterInterface
    ):
        try:
            response = self._get_domain_posts_response(
                user_id=user_id,
                domain_id=domain_id,
                offset=offset,
                limit=limit,
                presenter=presenter
            )
        except InvalidDomainId:
            presenter.raise_invalid_domain_id()
            return
        except UserNotFollowing:
            presenter.raise_user_not_following()
            return
        except InvalidInput:
            presenter.raise_invalid_input()
            return

        return response

    def _get_domain_posts_response(
        self, user_id: int, domain_id: int,
        offset: int, limit: int,
        presenter: PresenterInterface
    ):
        complete_post_details = self.get_domain_posts(
            user_id=user_id, domain_id=domain_id,
            offset=offset, limit=limit
        )
        return presenter.get_domain_posts_response(complete_post_details)


    def get_domain_posts(
        self, user_id: int, domain_id: int,
        offset: int, limit: int
    ):

        self._validate_offset_limit(offset, limit)

        self.storage.validate_domain_id(
            domain_id=domain_id
        )

        is_user_following = self.storage.is_user_following(
            domain_id=domain_id,
            user_id=user_id
        )

        if not is_user_following:
            raise UserNotFollowing

        domain_post_ids = self.storage.get_domain_related_post_ids(
            domain_id=domain_id,
            offset=offset,
            limit=limit
        )

        interactor = GetPostsInteractor(self.storage)

        response = interactor.get_posts(domain_post_ids)

        return response

    def _validate_offset_limit(self, offset: int, limit: int):
        invalid_values = (offset< 0 or limit<=0)
        if invalid_values:
            raise InvalidInput
