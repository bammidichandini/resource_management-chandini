from abc import ABC
from abc import abstractmethod
from common.dtos import UserAuthTokensDTO
from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface
from typing import List
from resource_management.constants.enums import TimeFormat
from django_swagger_utils.drf_server.exceptions import (
    BadRequest,
    Forbidden,
    NotFound
)
from resource_management.constants.exception_messages import (
    INVALID_ID,
    INVALID_INPUT,
    FORBIDDEN
)
from resource_management.dtos.dtos import (
    ResourceDto,
    RequestsDto,
    RequestDto,
    UserDto,
    Itemdto,
    userdto,
    RegisterUserDto,
    IndividualUserRequestsDto,
    ItemDto,
    ResourceItemDto,
    GetUserRequestsDto,
    getuserrequestsdto,
    ResourceItemParametersDto
    )

from resource_management.exceptions.exceptions import UserCannotManipulateException
from resource_management.exceptions.exceptions import (
    InvalidUserException,
    InvalidPasswordException,
    UserAlreadyExistedException,
    InvalidIdException,
    InvalidDetailsException
    )
from resource_management.constants.exception_messages import (
    INVALID_ID,
    INVALID_INPUT,
    EXISTED_USER,
    INVALID_USER,
    INVALID_PASSWORD
)
class PresenterImplementation(PresenterInterface):

    def raise_invalid_password_exception(self):
        raise BadRequest(*INVALID_PASSWORD)


    def raise_invalid_username_exception(self):
        raise BadRequest(*INVALID_USER)


    def get_login_response(self,
                           access_token_dto_obj: UserAuthTokensDTO,
                           role: bool
                           ):
        format = TimeFormat.FORMAT.value
        dict = {
            "user_id": access_token_dto_obj.user_id,
            "access_token": access_token_dto_obj.access_token,
            "refresh_token": access_token_dto_obj.refresh_token,
            "expires_in": (access_token_dto_obj.expires_in).strftime(format)
        }
        result = {
            "role": role,
            "access_token": dict
        }
        return result

    def get_signup_response(self,
                           access_token_dto_obj: UserAuthTokensDTO
                           ):
        format = TimeFormat.FORMAT.value
        dict = {
            "user_id": access_token_dto_obj.user_id,
            "access_token": access_token_dto_obj.access_token,
            "refresh_token": access_token_dto_obj.refresh_token,
            "expires_in": (access_token_dto_obj.expires_in).strftime(format)
        }

        return dict

    def get_resources_response(
        self,
        resources_dto_list: List[ResourceDto]
        ):

        resources_dict_list = []

        for resource_dto in resources_dto_list:

            resource_dict = {
            "id": 0,
            "image_url": "",
            "link": "",
            "name": "",
            "description": "",
            "item_name": ""
            }

            resource_dict["id"] = resource_dto.id
            resource_dict["item_name"] = resource_dto.item_name
            resource_dict["link"] = resource_dto.link
            resource_dict["name"] = resource_dto.name
            resource_dict["description"] = resource_dto.description
            resource_dict["image_url"] = resource_dto.image_url
            resources_dict_list.append(resource_dict)

        return resources_dict_list

    def raise_user_cannot_manipulate_exception(self):
        raise Forbidden(*FORBIDDEN)


    def get_resource_items_response(
        self,
        items_dto : ResourceItemDto
        ):

        items_dict_list = []
        item_dtos = items_dto.item
        for item_dto in item_dtos:

            items_dict_list.append( {
            "id": item_dto.id,
            "item_name": item_dto.item_name ,
            "link": item_dto.link,
            "description": item_dto.description,
            })
        resource_item_dict = {
            "id": items_dto.id,
            "resource_name": items_dto.resource_name,
            "description": items_dto.description,
            "link": items_dto.link,
            "item_count": items_dto.items_count,
            "image_url": items_dto.image_url,
            "item": items_dict_list
        }

        return resource_item_dict

    def get_requests_response(
        self,
        user_dtos: List[userdto],
        request_dto: List[RequestsDto]
        ):
        format = TimeFormat.FORMAT.value
        request_dto_list = []
        user_dict = {}
        for user_dto in user_dtos:
            user_dict[user_dto.id]= user_dto

        for request_obj in request_dto:
            request_dict = {
                "id": request_obj.id,
                "url": user_dict[request_obj.user_id].profile_pic,
                "name": user_dict[request_obj.user_id].person_name,
                "item_name": request_obj.item_name,
                "access_level":request_obj.access_level,
                "duedatetime":(request_obj.duedatetime).strftime(format),
                "resource":request_obj.resource_name
            }
            request_dto_list.append(request_dict)
        return request_dto_list

    def get_user_for_items_response(
            self,
            user_dtos: userdto,
            request_dto: List[RequestDto],
            count: int
        ):
        user_dict = {}
        for user_dto in user_dtos:
            user_dict[user_dto.id] = user_dto

        list_of_user = []
        for dto_obj in request_dto:
            list_of_user .append( {
                "id": user_dict[dto_obj.id].id,
                "person_name": user_dict[dto_obj.id].person_name,
                "department": user_dict[dto_obj.id].department,
                "job_role": user_dict[dto_obj.id].job_role,
                "access_level": dto_obj.access_level,
            })
        user_dict = {
            "count": count,
            "users": list_of_user
        }
        return user_dict

    def raise_user_already_existed_exception(self):
        raise BadRequest(*EXISTED_USER)


    def raise_invalid_id_exception(self):
        raise NotFound(*INVALID_ID)

    def raise_invalid_details_exception(self):
        raise InvalidDetailsException

    def get_user_details_to_admin_response(
        self,
        user_dto: List[RegisterUserDto]
        ):
        users_dict_list = []
        for dto in user_dto:
            users_dict_list.append(
                {
                "user_id": dto.id,
                "person_name": dto.person_name,
                "job_role": dto.job_role,
                "department": dto.department,
                "profile_pic": dto.profile_pic
            })
        return users_dict_list


    def get_individual_user_details_to_admin_response(self,
    user_requests_dto: List[IndividualUserRequestsDto],
    user_dto: List[userdto]

    ):
        user_dict = {}
        for dto in user_dto:
            user_dict[dto.id]=dto

        list_of_users = []
        for dto in user_requests_dto:
            list_of_users.append(
                {
                    "person_name": user_dict[dto.id].person_name,
                    "department":user_dict[dto.id].department,
                    "job_role":user_dict[dto.id].job_role,
                    "profile_pic":user_dict[dto.id].profile_pic,
                    "resource_name":dto.resource_name,
                    "item_name":dto.item_name,
                    "access_level":dto.access_level,
                    "description":dto.description,
                    "link":dto.link
                }
                )
        return list_of_users

    def get_user_resources_response(self, items_dto: List[Itemdto]):
        items_list = []
        for item in items_dto:
            print("*"* 100,item)
            items_list.append(
                {
                    "id":item.id,
                    "resource_name": item.resource_name,
                    "item_name": item.item_name,
                    "link": item.link,
                    "access_level": item.access_level
                }
                )
        return items_list


    def get_user_requests_response(self, user_dto: getuserrequestsdto):
        request_dict_list = []
        requests = user_dto.requests
        for request_dto in requests:
            request_dict_list.append(
                {
                    "id": request_dto.id,
                    "item_name": request_dto.item_name,
                    "resource_name": request_dto.resource_name,
                    "status": request_dto.status,
                    "access_level": request_dto.access_level
                }
                )
        result_dict = {
            "total_count": user_dto.count,
            "requests": request_dict_list
        }
        return result_dict


    def raise_invalid_input_exception(self):
        raise BadRequest(*INVALID_INPUT)
