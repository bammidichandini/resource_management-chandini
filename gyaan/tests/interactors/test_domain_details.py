import pytest
from unittest.mock import create_autospec
from gyaan.exceptions.exceptions import (
    InvalidDomainId
)
from gyaan.dtos.dtos import DomainDto
from django_swagger_utils.drf_server.exceptions import NotFound
from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.interactors.presenters.presenter_interface import PresenterInterface
from gyaan.interactors.domain_details import DomainDetailsInteractor


def test_domain_details_with_invalid_domain_id():

    # arrange
    user_id = 1
    domain_id = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    wrapper = DomainDetailsInteractor(
        storage=storage
    )

    presenter.raise_invalid_domain_id.side_effect = NotFound
    storage.get_domain_dto.side_effect = InvalidDomainId

    # act
    with pytest.raises(NotFound):
        wrapper.domain_details_wrapper(
            user_id=user_id,
            domain_id=domain_id,
            presenter=presenter
        )

    # assert
    presenter.raise_invalid_domain_id.assert_called_once()
    storage.get_domain_dto.assert_called_once_with(domain_id)


def test_domain_details_if_user_not_following_the_domain(domain_dto):

    # arrange
    user_id = 1
    domain_id = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    wrapper = DomainDetailsInteractor(
        storage=storage
    )

    presenter.raise_user_not_following.side_effect = NotFound
    storage.get_domain_dto.return_value = domain_dto
    storage.is_user_following.return_value = False

    # act
    with pytest.raises(NotFound):
        wrapper.domain_details_wrapper(
            user_id=user_id,
            domain_id=domain_id,
            presenter=presenter
        )

    # assert
    presenter.raise_user_not_following.assert_called_once()
    storage.get_domain_dto.assert_called_once_with(domain_id)
    storage.is_user_following.assert_called_once_with(
        domain_id=domain_id,
        user_id=user_id
    )


@pytest.mark.django_db
def test_domain_details_with_valid_details(
    domain_dto,
    user_details_dto,
    domain_stats_dto,
    join_request_dto,
    domain_details_dto,
    get_domain_details_response
):

    # arrange
    user_id = 1
    domain_id = 1
    expert_ids_list = [1,2,3]
    user_ids  = [1]
    expected_response = get_domain_details_response

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    wrapper = DomainDetailsInteractor(
        storage=storage
    )

    storage.get_domain_dto.return_value = domain_dto
    storage.is_user_following.return_value = True
    storage.get_domain_stats.return_value = domain_stats_dto
    storage.get_domain_expert_ids.return_value = expert_ids_list
    storage.get_expert_details.return_value = user_details_dto
    storage.is_user_expert.return_value = True
    storage.get_join_requests.return_value = join_request_dto
    storage.get_users_details.return_value = user_details_dto
    presenter.get_domain_details_response.return_value = get_domain_details_response

    # act

    response = wrapper.domain_details_wrapper(
            user_id=user_id,
            domain_id=domain_id,
            presenter=presenter
        )

    # assert
    storage.get_domain_dto.assert_called_once_with(domain_id)
    storage.is_user_following.assert_called_once_with(
        domain_id=domain_id,
        user_id=user_id
    )
    storage.get_domain_dto.assert_called_once_with(domain_id)
    storage.get_domain_stats.assert_called_once_with(domain_id)
    storage.get_domain_expert_ids.assert_called_once_with(domain_id)
    storage.get_expert_details.assert_called_once_with(expert_ids_list)
    storage.is_user_expert.assert_called_once_with(
        domain_id=domain_id,
        user_id=user_id
    )
    storage.get_join_requests.assert_called_once_with(domain_id)
    storage.get_users_details.assert_called_once_with(user_ids)
    presenter.get_domain_details_response.assert_called_once_with(domain_details_dto)
    assert expected_response == response

@pytest.mark.django_db
def test_domain_details_with_user_not_as_expert(
    domain_dto,
    domain_stats_dto,
    join_request_dto,
    domain_details_dto_with_empty_users,
    get_domain_details_response
):

    # arrange
    user_id = 1
    domain_id = 1
    expert_ids_list = [1,2,3]
    domain_details_dto = domain_details_dto_with_empty_users
    user_details_dto = []
    expected_response = get_domain_details_response

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    wrapper = DomainDetailsInteractor(
        storage=storage
    )

    storage.get_domain_dto.return_value = domain_dto
    storage.is_user_following.return_value = True
    storage.get_domain_stats.return_value = domain_stats_dto
    storage.get_domain_expert_ids.return_value = expert_ids_list
    storage.get_expert_details.return_value = user_details_dto
    storage.is_user_expert.return_value = False
    presenter.get_domain_details_response.return_value = get_domain_details_response

    # act

    response = wrapper.domain_details_wrapper(
            user_id=user_id,
            domain_id=domain_id,
            presenter=presenter
        )

    # assert
    storage.get_domain_dto.assert_called_once_with(domain_id)
    storage.is_user_following.assert_called_once_with(
        domain_id=domain_id,
        user_id=user_id
    )
    storage.get_domain_dto.assert_called_once_with(domain_id)
    storage.get_domain_stats.assert_called_once_with(domain_id)
    storage.get_domain_expert_ids.assert_called_once_with(domain_id)
    storage.get_expert_details.assert_called_once_with(expert_ids_list)
    storage.is_user_expert.assert_called_once_with(
        domain_id=domain_id,
        user_id=user_id
    )
    presenter.get_domain_details_response.assert_called_once_with(domain_details_dto)
    assert expected_response == response
