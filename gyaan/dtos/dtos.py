from typing import List
from dataclasses import dataclass
from datetime import datetime



@dataclass
class DomainDto:
    domain_id: int
    domain_name: str
    description: str

@dataclass
class DomainStatsDto:
    domain_id: int
    followers_count: int
    posts_count: int
    bookmarked_count: int


@dataclass
class UserDetailsDto:
    user_id: int
    name: str
    profile_pic_url: str

@dataclass
class JoinRequestDto:
    request_id: int
    user_id: int


@dataclass
class DomainDetailsDto:
    domain_dto: DomainDto
    domainstats: DomainStatsDto
    domain_experts: List[UserDetailsDto]
    user_id: int
    is_user_domain_expert: bool
    join_requests: List[JoinRequestDto]
    requested_users: List[UserDetailsDto]

@dataclass
class PostDto:
    post_id: int
    posted_at: datetime
    posted_by_id: int
    title: str
    content: str


@dataclass
class CommentDto:
    post_id: int
    comment_id: int
    commented_at: datetime
    commented_by_id: int
    content: str

@dataclass
class PostTagDetails:
    tag_id: int
    post_id: int
    tag_name:str

@dataclass
class PostReactionsCount:
    post_id: int
    reactions_count: int


@dataclass
class CommentReactionsCount:
    comment_id: int
    reactions_count: int


@dataclass
class PostCommentsCount:
    post_id: int
    comments_count: int


@dataclass
class CommentRepliesCount:
    comment_id: int
    replies_count: int


@dataclass()
class CompletePostDetails:
    post_dtos: List[PostDto]
    post_reaction_counts: List[PostReactionsCount]
    comment_reaction_counts: List[CommentReactionsCount]
    comment_counts: List[PostCommentsCount]
    reply_counts: List[CommentRepliesCount]
    comment_dtos: List[CommentDto]
    post_tag_details: List[PostTagDetails]
    users_dtos: List[UserDetailsDto]

@dataclass
class DomainDetailsWithPosts:
    post_details: CompletePostDetails
    domain_details: DomainDetailsDto
