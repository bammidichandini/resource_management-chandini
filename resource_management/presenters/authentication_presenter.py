from abc import ABC
from abc import abstractmethod
from common.dtos import UserAuthTokensDTO
from resource_management.interactors.presenters.presenter_interface \
    import PresenterInterface
from typing import List
from resource_management.constants.enums import TimeFormat
from resource_management.dtos.dtos import (
    ResourceDto,
    RequestsDto,
    UserDto,
    Itemdto,
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

class PresenterImplementation(PresenterInterface):

    def raise_invalid_password_exception(self):
        raise InvalidPasswordException


    def raise_invalid_username_exception(self):
        raise InvalidUserException


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
        raise UserCannotManipulateException


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
        request_dto: List[RequestsDto]
        ):
        format = TimeFormat.FORMAT.value
        request_dto_list = []
        for request_obj in request_dto:
            request_dict = {
                "id": request_obj.id,
                "url": request_obj.url,
                "name": request_obj.name,
                "item_name": request_obj.item_name,
                "access_level":request_obj.access_level,
                "duedatetime":(request_obj.duedatetime).strftime(format),
                "resource":request_obj.resource_name
            }
            request_dto_list.append(request_dict)
        return request_dto_list

    def get_user_for_items_response(
            self,
            user_dto: UserDto):
        user_dtos = user_dto.users
        list_of_user = []
        for dto_obj in user_dtos:
            list_of_user .append( {
                "id": dto_obj.id,
                "person_name": dto_obj.person_name,
                "department": dto_obj.department,
                "job_role": dto_obj.job_role,
                "access_level": dto_obj.access_level,
            })
        user_dict = {
            "count": user_dto.count,
            "users": list_of_user
        }
        return user_dict

    def raise_user_already_existed_exception(self):
        raise UserAlreadyExistedException


    def raise_invalid_id_exception(self):
        raise InvalidIdException

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
                "profile_pic": dto.url
            })
        return users_dict_list


    def get_individual_user_details_to_admin_response(self,
    user_requests_dto: List[IndividualUserRequestsDto]
    ):
        list_of_users = []
        for dto in user_requests_dto:
            list_of_users.append(
                {
                    "person_name": dto.person_name,
                    "department":dto.department,
                    "job_role":dto.job_role,
                    "profile_pic":dto.profile_pic,
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


