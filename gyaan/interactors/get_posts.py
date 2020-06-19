from typing import List
from gyaan.exceptions.exceptions import InvalidPostIds
from gyaan.dtos.dtos import CompletePostDetails
from gyaan.interactors.presenters.presenter_interface import PresenterInterface
from gyaan.interactors.storages.storage_interface import StorageInterface


class GetPostsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage


    def get_posts_wrapper(
        self, post_ids: List[int], presenter: PresenterInterface
    ):

        try:
            response = self._get_posts_response(
                post_ids=post_ids, presenter=presenter
            )
        except InvalidPostIds as error:
            presenter.raise_invalid_post_ids(error=error)
            return

        return response

    def _get_posts_response(
        self, post_ids: List[int], presenter: PresenterInterface
    ):

        post_dtos = self.get_posts(post_ids)

        return presenter.get_posts_response(post_dtos)


    def get_posts(self, post_ids: List[int]):
        post_ids = self._get_unique_post_ids(post_ids)

        all_post_ids = self.storage.get_post_ids()

        self._validate_post_ids(
            post_ids=post_ids, all_post_ids=all_post_ids
        )

        #TODO post_details
        post_dtos = self.storage.get_post_details(post_ids=post_ids)

        #TODO post_tags
        post_tag_details = self.storage.get_post_tags(post_ids=post_ids)

        #TODO post_reactions_count
        post_reactions_counts = self.storage.get_post_reactions_count(
            post_ids=post_ids
        )

        #TODOO post_comments_count
        post_comments_counts = self.storage.get_comments_count(
            post_ids=post_ids
        )

        #TODO latest_comment_ids
        comment_ids = self._get_latest_comment_ids(post_ids=post_ids)

        #TODO comment_reactions_count
        comments_reactions_counts = self.storage.\
            get_comment_reactions_count(comment_ids)

        #TODO comment_replies_count
        comment_replies_counts = self.storage.\
            get_comment_replies_count(comment_ids
            )

        #TODO get_comment_details
        comment_dtos = self.storage.get_comment_details(comment_ids)

        #TODO user_ids list from post_dto and comment_dto
        user_ids_list = []
        user_ids_list = [post_dto.posted_by_id
                         for post_dto in post_dtos
                        ]
        user_ids_list += [comment_dto.commented_by_id
                          for comment_dto in comment_dtos
                         ]

        #TODO get_user_details
        user_dtos = self.storage.get_users_details(user_ids_list)

        return CompletePostDetails(
            post_dtos=post_dtos,
            post_reaction_counts=post_reactions_counts,
            comment_counts=post_comments_counts,
            comment_reaction_counts=comments_reactions_counts,
            reply_counts=comment_replies_counts,
            comment_dtos=comment_dtos,
            post_tag_details=post_tag_details,
            users_dtos=user_dtos
        )


    def _get_latest_comment_ids(self, post_ids: List[int]):
        comment_ids_list = []
        for post_id in post_ids:
            comment_ids_list.extend(self.storage.get_latest_comment_ids(
                post_id=post_id, no_of_comments=2
            ))
        return comment_ids_list

    def _get_unique_post_ids(self, post_ids: List[int]):
        return list(set(post_ids))

    def _validate_post_ids(self, post_ids: List[int], all_post_ids: List[int]):

        invalid_post_ids = [
            post_id
            for post_id in post_ids
            if post_id not in all_post_ids
            ]

        if invalid_post_ids:
            raise InvalidPostIds(post_ids=invalid_post_ids)
