from abc import ABC
from abc import abstractmethod
from typing import List
from django.db.models import Prefetch
from collections import defaultdict
from resource_management.models import(
     Request,
     Resource,
     Item,
     UserAccess
    )
from resource_management.exceptions.exceptions import(
    InvalidIdException,
    InvalidDetailsException
    )
from resource_management.dtos.dtos import (
    RequestsDto,
    RequestsUpdateDto,
    getuserrequestsdto,
    IndividualUserRequestsDto,
    CreateUserRequestsDto,
    GetUserRequestsDto
    )
from resource_management.models import User
from django.core.exceptions import ObjectDoesNotExist
from resource_management.constants.enums import RequestStatus
from resource_management.interactors.storages.requests_storage_interface \
    import StorageInterface


class StorageImplementation(StorageInterface):


    def get_requests(self) -> List[RequestsDto]:

        queryset = Item.objects.prefetch_related('useraccess')
        requests = Request.objects.prefetch_related(Prefetch('item',queryset=queryset),'user','resource').\
                    values('user__username',
                                'item__name',
                                'item__useraccess__access_level'
                                'resource__name',
                                'duration',
                                'id',
                                'user__profile_pic'
                                )
        request_dict = {}
        for request in requests:
            sub_dict = {
                "name": request["user__username"],
                "access_level": request["item__useraccess__access_level"],
                "duedatetime": request["duedatetime"],
                "resource_name": request["resource_name"],
                "item_name": request["item__name"],
                "url": request["user__profile_pic"]
            }
            request_dict[request["id"]] = sub_dict


        list_of_requests = []

        for key,request in request_dict.items():
            list_of_requests.append(
                RequestsDto(
                    id = key,
                    name=request["name"],
                    access_level=request["access_level"],
                    duedatetime=request["duedatetime"],
                    resource_name=request["resource_name"],
                    item_name=request["item__name"],
                    url=request["url"]
                    )
                )
        return list_of_requests


    def set_status(
        self,
        status: str,
        request_ids_list: List[int],
        reason: str
        ):

        if status == "Accepted":
            status = RequestStatus.Accepted.value
        elif status == "Rejected":
            status = RequestStatus.Rejected.value

        requests = Request.objects.filter(id__in=request_ids_list)
        if len(requests) == 0:
            raise ObjectDoesNotExist
        requests.update(status=status,reason=reason)
        list_levels = []
        for request in requests:
            list_levels.append(UserAccess(
                item=request.item,
                user=request.user,
                access_level=request.access_level))
        UserAccess.objects.bulk_create(list_levels)

    def get_individual_user_details_to_admin(self, user_id: int):

        user_items = Request.objects.filter(user_id=user_id).prefetch_related('item','resource').\
            values(
                'user__name',
                'user__department',
                'user__job_role',
                'user__profile_pic',
                'resource__name',
                'item__name',
                'access_level',
                'item__description',
                'item__link'
                )
        items_list = []
        if not len(user_items) == 0:
            for item in user_items:
                items_list.append(IndividualUserRequestsDto(
                    person_name=item["user__name"],
                    department=item["user__department"],
                    job_role=item["user__job_role"],
                    profile_pic=item["user__profile_pic"],
                    resource_name=item["resource__name"],
                    item_name=item["item__name"],
                    access_level=item["access_level"],
                    description=item["item__description"],
                    link=item["item__link"],
                    ))
        return items_list


    def update_user_request(
        self,
        user_id: int,
        request_id: int,
        update_dto: RequestsUpdateDto
        ):
            resource = Resource.objects.get(name=update_dto.resource_name)
            item = Item.objects.get(resource=resource,name=update_dto.item_name)
            request = Request.objects.filter(id=request_id)
            if len(request):
                raise ObjectDoesNotExist

            request.update(
                    resource=resource,
                    item=item,
                    user_id=user_id,
                    duration=update_dto.duedatetime,
                    reason=update_dto.access_reason,
                    remarks=update_dto.remarks,
                    access_llevel=update_dto.access_level
                )

            UserAccess.objects.filter(item=item,resource=resource,user_id=user_id).update(
                access_level=update_dto.access_level,
                item=item,
                user_id=user_id
                )


    def delete_user_request(self, user_id: int, request_id: int):

        request = Request.objects.filter(id=request_id)
        if len(request) == 0:
            raise ObjectDoesNotExist
        request.delete()


    def create_new_user_request(
        self,
        user_id: int,
        request_dto: CreateUserRequestsDto
    ):
        resource = Resource.objects.get(name=request_dto.resource_name)
        item = Item.objects.get(resource=resource,name=request_dto.item_name)
        Request.objects.create(
            item=item,
            resource=resource,
            user_id=user_id,
            duration=request_dto.duedatetime,
            reason=request_dto.access_reason,
            access_level=request_dto.access_level
            )
        UserAccess.objects.create(
            item=item,
            user_id=user_id,
            access_level=request_dto.access_level
            )


    def get_user_requests(self, user_id: int,
    offset, limit
    ) -> getuserrequestsdto:

        count = Request.objects.filter(user_id=user_id).count()
        user_requests = Request.objects.filter(user_id=user_id).\
            values(
                'id',
                'item__name',
                'resource__name',
                'status',
                'access_level'
            )[offset:offset+limit]
        user_dto = []
        for user_request in user_requests:
            user_dto.append(GetUserRequestsDto(
                id=user_request["id"],
                item_name=user_request['item__name'],
                resource_name=user_request['resource__name'],
                status=user_request['status'],
                access_level=user_request['access_level']
                ))
        request_dto = getuserrequestsdto(
            count=count,
            requests=user_dto
            )
        return request_dto

    def check_for_valid_input(self, list_ids: List[int]) -> bool:
        for id in list_ids:
            if id <= 0 :
                return False
        return True

    def is_admin(self, user_id: int) -> bool:
        is_admin = User.objects.get(id=user_id).is_admin
        return is_admin

    def check_for_valid_offset(self, offset):
        if offset < 0:
            return False
        return True
