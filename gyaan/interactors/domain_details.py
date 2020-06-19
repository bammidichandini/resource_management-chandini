from gyaan.exceptions.exceptions import (
    InvalidDomainId,
    UserNotFollowing
)
from gyaan.dtos.dtos import DomainDetailsDto
from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.interactors.presenters.presenter_interface import PresenterInterface


class DomainDetailsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage


    def domain_details_wrapper(
        self,
        domain_id: int,
        user_id: int,
        presenter: PresenterInterface
    ):

        try:
            response = self._get_domain_related_details_response(
                user_id=user_id,
                domain_id=domain_id,
                presenter=presenter
            )
        except InvalidDomainId:
            presenter.raise_invalid_domain_id()
        except UserNotFollowing:
            presenter.raise_user_not_following()

        return response


    def _get_domain_related_details_response(
        self,
        user_id: int,
        domain_id: int,
        presenter: PresenterInterface
    ):
        domain_dtos = self.get_domain_details(
            user_id=user_id,
            domain_id=domain_id
        )
        return presenter.get_domain_details_response(domain_dtos)


    def get_domain_details(
        self,
        user_id: int,
        domain_id: int
    ):

        #TODO: get_domain_dto
        domain_dto = self.storage.get_domain_dto(domain_id)

        #TODO: check_whether_user_following_or_not
        is_user_following = self.storage.is_user_following(
            domain_id=domain_id,
            user_id=user_id
        )

        is_user_not_following = not is_user_following

        if is_user_not_following:
            raise UserNotFollowing

        #TODO: if_user_followed_get_domain_stats
        domain_stats = self.storage.get_domain_stats(domain_id=domain_id)

        #TODO: get_domain_experts
        expert_ids = self.storage.get_domain_expert_ids(domain_id=domain_id)

        #TODO: get_expert_details
        expert_details = self.storage.get_expert_details(expert_ids)

        #TODO: get_user_requests, requested_user_dtos, is_user_expert
        is_user_expert, domain_user_requests, requested_user_dtos = \
            self._get_user_expert_details(
            user_id=user_id,
            domain_id=domain_id
        )

        response = DomainDetailsDto(
            domain_dto=domain_dto,
            domainstats=domain_stats,
            domain_experts=expert_details,
            user_id=user_id,
            is_user_domain_expert=is_user_expert,
            join_requests=domain_user_requests,
            requested_users=requested_user_dtos
        )
        return response


    def _get_user_expert_details(self, user_id: int, domain_id: int):
        is_user_domain_expert = self.storage.is_user_expert(
            domain_id, user_id
        )
        join_requests = []
        requested_user_dtos = []

        if is_user_domain_expert:
            join_requests = self.storage.get_join_requests(
                domain_id
            )
        if join_requests:
            requested_user_dtos = self.storage.get_users_details(
                user_ids=[dto.user_id for dto in join_requests]
            )
        return is_user_domain_expert, join_requests, requested_user_dtos



