import pytest
from unittest.mock import create_autospec, patch
from django_swagger_utils.drf_server.exceptions import NotFound
from gyaan.exceptions.exceptions \
    import InvalidDomainId
from gyaan.interactors.domain_posts import DomainPostsInteractor
from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.presenters.presenter_interface \
        import PresenterInterface
from gyaan.interactors.get_posts import GetPostsInteractor


def test_domain_posts_with_invalid_domain():

    # arrange
    domain_id = 1
    user_id = 1
    offset = 1
    limit = 2

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.validate_domain_id.side_effect = InvalidDomainId
    presenter.raise_invalid_domain_id.side_effect = NotFound

    wrapper = DomainPostsInteractor(
        storage=storage
    )

    # act
    with pytest.raises(NotFound):
        wrapper.domain_posts_wrapper(
            user_id=user_id,
            domain_id=domain_id,
            presenter=presenter,
            offset=offset,
            limit=limit
        )

    # assert
    storage.validate_domain_id.assert_called_once_with(
        domain_id=domain_id
    )
    presenter.raise_invalid_domain_id.assert_called_once()

@pytest.mark.parametrize("limit", [
    (-1),(0)
])
def test_domain_posts_with_invalid_limit(limit):

    # arrange
    domain_id = 1
    user_id = 1
    offset = 1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    presenter.raise_invalid_input.side_effect = NotFound

    wrapper = DomainPostsInteractor(
        storage=storage
    )

    # act
    with pytest.raises(NotFound):
        wrapper.domain_posts_wrapper(
            user_id=user_id,
            domain_id=domain_id,
            presenter=presenter,
            offset=offset,
            limit=limit
        )

def test_domain_posts_with_invalid_offset():

    # arrange
    domain_id = 1
    user_id = 1
    offset = -1
    limit = 2

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    presenter.raise_invalid_input.side_effect = NotFound

    wrapper = DomainPostsInteractor(
        storage=storage
    )

    # act
    with pytest.raises(NotFound):
        wrapper.domain_posts_wrapper(
            user_id=user_id,
            domain_id=domain_id,
            presenter=presenter,
            offset=offset,
            limit=limit
        )


def test_domain_posts_with_user_not_following_domain():

    # arrange
    domain_id = 1
    user_id = 1
    offset = 1
    limit = 2

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.is_user_following.return_value = False
    presenter.raise_user_not_following.side_effect = NotFound

    wrapper = DomainPostsInteractor(
        storage=storage
    )

    # act
    with pytest.raises(NotFound):
        wrapper.domain_posts_wrapper(
            user_id=user_id,
            domain_id=domain_id,
            presenter=presenter,
            offset=offset,
            limit=limit
        )

    # assert
    storage.validate_domain_id.assert_called_once_with(domain_id=domain_id)
    presenter.raise_user_not_following.assert_called_once()



@patch.object(GetPostsInteractor, 'get_posts')
def test_domain_posts_with_valid_details(get_posts, complete_post_details):

    # arrange
    user_id = 1
    domain_id = 1
    offset = 1
    limit = 2

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.is_user_following.return_value = True
    get_posts.return_value = complete_post_details
    presenter.get_domain_posts_response.return_value = {}
    storage.get_domain_related_post_ids.return_value = [1,1]

    wrapper = DomainPostsInteractor(
        storage=storage
    )

    # act
    response = wrapper.domain_posts_wrapper(
        user_id=user_id,
        domain_id=domain_id,
        offset=offset,
        limit=limit,
        presenter=presenter
    )

    # assert
    storage.is_user_following.assert_called_once_with(
        user_id=user_id,
        domain_id=domain_id
    )
    get_posts.assert_called_once_with([1,1])
    presenter.get_domain_posts_response.assert_called_once_with(complete_post_details)
    assert response == {}
