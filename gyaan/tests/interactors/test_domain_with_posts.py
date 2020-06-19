import pytest
from unittest.mock import create_autospec, patch
from django_swagger_utils.drf_server.exceptions import NotFound
from gyaan.exceptions.exceptions import (
    InvalidDomainId,
    UserNotFollowing,
    InvalidInput
)
from gyaan.interactors.domain_details import DomainDetailsInteractor
from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.interactors.presenters.presenter_interface import PresenterInterface
from gyaan.interactors.domain_posts import DomainPostsInteractor
from gyaan.interactors.domain_details_with_posts import DomainWithPostsInteractor


@patch.object(DomainDetailsInteractor, 'get_domain_details',side_effect=InvalidDomainId)
def test_domain_with_posts_with_invalid_domain_id(get_domain_details):

    # arrange
    user_id = 1
    domain_id = 1
    offset = 1
    limit = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    presenter.raise_invalid_domain_id.side_effect = NotFound

    wrapper = DomainWithPostsInteractor(
        storage=storage
    )

    # act
    with pytest.raises(NotFound):
        wrapper.get_domain_with_posts_wrapper(
            user_id=user_id,
            domain_id=domain_id,
            offset=offset,
            limit=limit,
            presenter=presenter
        )

    # assert
    presenter.raise_invalid_domain_id.assert_called_once()


@patch.object(DomainPostsInteractor, 'get_domain_posts',side_effect=InvalidInput)
def test_domain_with_posts_with_invalid_offset(get_domain_posts):

    # arrange
    user_id = 1
    domain_id = 1
    offset = -1
    limit = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    presenter.raise_invalid_input.side_effect = NotFound

    wrapper = DomainWithPostsInteractor(
        storage=storage
    )

    # act
    with pytest.raises(NotFound):
        wrapper.get_domain_with_posts_wrapper(
            user_id=user_id,
            domain_id=domain_id,
            offset=offset,
            limit=limit,
            presenter=presenter
        )

    # assert
    presenter.raise_invalid_input.assert_called_once()


@patch.object(DomainPostsInteractor, 'get_domain_posts',side_effect=InvalidInput)
@pytest.mark.parametrize("limit", [
    (-1),(0)
])
def test_domain_with_posts_with_invalid_limit(get_domain_posts, limit):

    # arrange
    user_id = 1
    domain_id = 1
    offset = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    presenter.raise_invalid_input.side_effect = NotFound

    wrapper = DomainWithPostsInteractor(
        storage=storage
    )

    # act
    with pytest.raises(NotFound):
        wrapper.get_domain_with_posts_wrapper(
            user_id=user_id,
            domain_id=domain_id,
            offset=offset,
            limit=limit,
            presenter=presenter
        )

    # assert
    presenter.raise_invalid_input.assert_called_once()


@patch.object(DomainDetailsInteractor, 'get_domain_details',side_effect=UserNotFollowing)
def test_domain_with_posts_with_user_not_following(get_domain_details):

    # arrange
    user_id = 1
    domain_id = 1
    offset = 1
    limit = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    presenter.raise_user_not_following.side_effect = NotFound

    wrapper = DomainWithPostsInteractor(
        storage=storage
    )

    # act
    with pytest.raises(NotFound):
        wrapper.get_domain_with_posts_wrapper(
            user_id=user_id,
            domain_id=domain_id,
            offset=offset,
            limit=limit,
            presenter=presenter
        )

    # assert
    presenter.raise_user_not_following.assert_called_once()


@patch.object(DomainDetailsInteractor, 'get_domain_details')
@patch.object(DomainPostsInteractor, 'get_domain_posts')
def test_domain_with_posts_with_valid_details(
    get_domain_posts,
    get_domain_details,
    complete_post_details,
    domain_details_dto,
    domain_details_with_posts
):

    # arrange
    user_id = 1
    domain_id = 1
    offset = 1
    limit = 1

    get_domain_posts.return_value = complete_post_details
    get_domain_details.return_value = domain_details_dto

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    presenter.get_domain_with_posts_response.return_value = {}


    wrapper = DomainWithPostsInteractor(
        storage=storage
    )

    # act

    response = wrapper.get_domain_with_posts_wrapper(
        user_id=user_id,
        domain_id=domain_id,
        offset=offset,
        limit=limit,
        presenter=presenter
    )

    # assert
    assert response == {}
    presenter.get_domain_with_posts_response.assert_called_once_with(
        domain_details_with_posts
    )


