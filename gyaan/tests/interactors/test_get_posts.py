import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound
from gyaan.interactors.get_posts import GetPostsInteractor
from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.interactors.presenters.presenter_interface import PresenterInterface



def test_get_posts_with_invalid_post_ids():

    # arrange
    post_ids = [1,2,9,1,4,5,8]
    all_post_ids = [1,2,3,4]
    invalid_post_ids = [5,8,9]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.get_post_ids.return_value = all_post_ids
    presenter.raise_invalid_post_ids.side_effect = NotFound

    wrapper = GetPostsInteractor(
        storage=storage
    )

    # act
    with pytest.raises(NotFound):
        wrapper.get_posts_wrapper(
            post_ids=post_ids,
            presenter=presenter
        )

    # assert
    storage.get_post_ids.assert_called_once()
    error = presenter.raise_invalid_post_ids.call_args.kwargs['error'].post_ids
    assert error ==  invalid_post_ids

def test_get_posts_with_valid_post_ids(
    comment_dtos,
    post_dtos,
    post_tag_details,
    post_reactions_counts,
    comment_reactions_counts,
    post_comments_counts,
    comment_replies_counts,
    complete_post_details,
    user_details_dto,
    posts_response
):

    # arrange
    post_ids = [1,1]
    user_ids_list = [1,2]
    valid_post_ids = [1]
    all_post_ids = [1,2,3,4]
    comment_ids_list = [1,2]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.get_post_ids.return_value = all_post_ids
    storage.get_post_details.return_value = post_dtos
    storage.get_post_tags.return_value = post_tag_details
    storage.get_post_reactions_count.return_value = post_reactions_counts
    storage.get_comments_count.return_value = post_comments_counts
    storage.get_comment_reactions_count.return_value = comment_reactions_counts
    storage.get_comment_replies_count.return_value = comment_replies_counts
    storage.get_comment_details.return_value = comment_dtos
    storage.get_users_details.return_value = user_details_dto
    storage.get_latest_comment_ids.return_value = comment_ids_list
    presenter.get_posts_response.return_value = posts_response

    wrapper = GetPostsInteractor(
        storage=storage
    )

    # act
    response = wrapper.get_posts_wrapper(
        post_ids=post_ids,
        presenter=presenter
    )

    # assert
    storage.get_post_ids.assert_called_once()
    presenter.get_posts_response(post_dtos=complete_post_details)
    storage.get_post_details.assert_called_once_with(valid_post_ids)
    storage.get_post_tags.assert_called_once_with(valid_post_ids)
    storage.get_post_reactions_count.assert_called_once_with(valid_post_ids)
    storage.get_comments_count.assert_called_once_with(valid_post_ids)
    storage.get_comment_reactions_count.assert_called_once_with(comment_ids_list)
    storage.get_comment_replies_count.assert_called_once_with(comment_ids_list)
    storage.get_comment_details.assert_called_once_with(comment_ids_list)
    storage.get_users_details.assert_called_once_with(user_ids_list)
    m = storage.get_latest_comment_ids.call_args_list
    assert m[0].kwargs['post_id'] == 1
    assert m[0].kwargs['no_of_comments'] == 2
    assert response == posts_response
