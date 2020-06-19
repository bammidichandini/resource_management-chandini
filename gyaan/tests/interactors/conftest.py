import pytest
import datetime
from gyaan.dtos.dtos import (
    DomainDto,
    UserDetailsDto,
    DomainStatsDto,
    JoinRequestDto,
    DomainDetailsDto,
    PostDto,
    PostReactionsCount,
    PostCommentsCount,
    CommentDto,
    CommentReactionsCount,
    CommentRepliesCount,
    PostTagDetails,
    CompletePostDetails,
    DomainDetailsWithPosts
)


@pytest.fixture()
def domain_dto():
    response = DomainDto(
        domain_id=1,
        domain_name="name",
        description="description"
    )
    return response


@pytest.fixture()
def user_details_dto():
    response = [UserDetailsDto(
        user_id=1,
        name="chandini",
        profile_pic_url="https://images/chandini.png"
    )]
    return response


@pytest.fixture()
def domain_stats_dto():
    response = DomainStatsDto(
        domain_id=1,
        followers_count=2,
        posts_count=3,
        bookmarked_count=4
    )
    return response


@pytest.fixture()
def join_request_dto():
    response = [JoinRequestDto(
        request_id=1,
        user_id=1
    )]
    return response


@pytest.fixture()
def domain_details_dto():
    response = DomainDetailsDto(
        domain_dto=DomainDto(
        domain_id=1,
        domain_name="name",
        description="description"
        ),
        domainstats=DomainStatsDto(
        domain_id=1,
        followers_count=2,
        posts_count=3,
        bookmarked_count=4
        ),
        domain_experts=[UserDetailsDto(
        user_id=1,
        name="chandini",
        profile_pic_url="https://images/chandini.png"
        )],
        user_id=1,
        is_user_domain_expert=True,
        join_requests=[JoinRequestDto(
        request_id=1,
        user_id=1
        )],
        requested_users=[UserDetailsDto(
        user_id=1,
        name="chandini",
        profile_pic_url="https://images/chandini.png"
        )]
    )
    return response


@pytest.fixture()
def domain_details_dto_with_empty_users():
    response = DomainDetailsDto(
        domain_dto=DomainDto(
        domain_id=1,
        domain_name="name",
        description="description"
        ),
        domainstats=DomainStatsDto(
        domain_id=1,
        followers_count=2,
        posts_count=3,
        bookmarked_count=4
        ),
        domain_experts=[],
        user_id=1,
        is_user_domain_expert=False,
        join_requests=[],
        requested_users=[]
    )
    return response


@pytest.fixture()
def get_domain_details_response():
    response = {
        "domain_id": 1,
        "domain_name": "name",
        "description": "description",
        "domainstats": {
            "domain_id": 1,
            "followers_count": 2,
            "posts_count":3,
            "bookmarked_count": 4
        },
        "domain_experts": {
            "user_id": 1,
            "name": "chandini",
            "profile_pic_url": "https://images/chandini.png"
        },
        "user_id": 1,
        "is_user_domain_expert": True,
        "join_requests": {
            "request_id": 1,
            "user_id": 1
        },
        "requested_users": {
            "user_id": 1,
            "name": "chandini",
            "profile_pic_url": "https://images/chandini.png"
        }
    }
    return response


@pytest.fixture()
def post_dtos():
    response = [
        PostDto(
            post_id=1,
            posted_at=datetime.datetime(2020, 10, 10),
            posted_by_id=1,
            title="title",
            content="content"
        )
        ]
    return response


@pytest.fixture()
def comment_dtos():
    response = [
        CommentDto(
            post_id=1,
            comment_id=1,
            commented_at=datetime.datetime(2020, 10, 10),
            commented_by_id=2,
            content="content"
        )
        ]
    return response


@pytest.fixture()
def post_tag_details():
    response = PostTagDetails(
            tag_id=1,
            tag_name="tag_name",
            post_id=1
        )

    return response

@pytest.fixture()
def post_reactions_counts():
    response = [
        PostReactionsCount(
            post_id=1,
            reactions_count=4
        )
    ]
    return response

@pytest.fixture()
def comment_reactions_counts():
    response = [CommentReactionsCount(
            comment_id=1,
            reactions_count=3
        )]
    return response

@pytest.fixture()
def post_comments_counts():
    response = [
        PostCommentsCount(
            post_id=1,
            comments_count=4
        )
    ]
    return response

@pytest.fixture()
def comment_replies_counts():
    response = [CommentRepliesCount(
            comment_id=1,
            replies_count=3
        )]
    return response

@pytest.fixture()
def complete_post_details():
    response = CompletePostDetails(
        post_dtos=[
            PostDto(
                post_id=1,
                posted_at=datetime.datetime(2020, 10, 10),
                posted_by_id=1,
                title="title",
                content="content"
            )
        ],
        post_reaction_counts=[
            PostReactionsCount(
                post_id=1,
                reactions_count=4
            )
        ],
        comment_reaction_counts=[CommentReactionsCount(
            comment_id=1,
            reactions_count=3
        )],
        comment_counts=[
        PostCommentsCount(
            post_id=1,
            comments_count=4
        )
        ],
        reply_counts=[CommentRepliesCount(
            comment_id=1,
            replies_count=3
        )],
        comment_dtos=[
        CommentDto(
            post_id=1,
            comment_id=1,
            commented_at=datetime.datetime(2020, 10, 10),
            commented_by_id=2,
            content="content"
        )
        ],
        post_tag_details=[PostTagDetails(
            tag_id=1,
            tag_name="tag",
            post_id=1
        )],
        users_dtos=[UserDetailsDto(
        user_id=1,
        name="chandini",
        profile_pic_url="https://images/chandini.png"
        )]
    )
    return response


@pytest.fixture()
def posts_response():
    response = {}
    return response


@pytest.fixture()
def domain_details_with_posts():
    response = DomainDetailsWithPosts(
        post_details=CompletePostDetails(
        post_dtos=[
            PostDto(
                post_id=1,
                posted_at=datetime.datetime(2020, 10, 10),
                posted_by_id=1,
                title="title",
                content="content"
            )
        ],
        post_reaction_counts=[
            PostReactionsCount(
                post_id=1,
                reactions_count=4
            )
        ],
        comment_reaction_counts=[CommentReactionsCount(
            comment_id=1,
            reactions_count=3
        )],
        comment_counts=[
        PostCommentsCount(
            post_id=1,
            comments_count=4
        )
        ],
        reply_counts=[CommentRepliesCount(
            comment_id=1,
            replies_count=3
        )],
        comment_dtos=[
        CommentDto(
            post_id=1,
            comment_id=1,
            commented_at=datetime.datetime(2020, 10, 10),
            commented_by_id=2,
            content="content"
        )
        ],
        post_tag_details=[PostTagDetails(
            tag_id=1,
            tag_name="tag",
            post_id=1
        )],
        users_dtos=[UserDetailsDto(
        user_id=1,
        name="chandini",
        profile_pic_url="https://images/chandini.png"
        )]
    ),
    domain_details=DomainDetailsDto(
        domain_dto=DomainDto(
        domain_id=1,
        domain_name="name",
        description="description"
        ),
        domainstats=DomainStatsDto(
        domain_id=1,
        followers_count=2,
        posts_count=3,
        bookmarked_count=4
        ),
        domain_experts=[UserDetailsDto(
        user_id=1,
        name="chandini",
        profile_pic_url="https://images/chandini.png"
        )],
        user_id=1,
        is_user_domain_expert=True,
        join_requests=[JoinRequestDto(
        request_id=1,
        user_id=1
        )],
        requested_users=[UserDetailsDto(
        user_id=1,
        name="chandini",
        profile_pic_url="https://images/chandini.png"
        )]
    )
    )
    return response
