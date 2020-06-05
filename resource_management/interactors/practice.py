from resource_management.models import Request

def get_requests():

        requests = Request.objects.all().\
                    values('user__username',
                                'item__name',
                                'user__useraccess_access_level'
                                'resource__name',
                                'duration',
                                'id',
                                'user__profile_pic'
                                )
        request_dict = {}
        for request in requests:
            sub_dict = {
                "name": request["user__username"],
                "access_level": request["user__useraccess_access_level"],
                "duedatetime": request["duedatetime"],
                "resource_name": request["resource_name"],
                "item_name": request["item_name"],
                "url": request["user__profile_pic"]
            }
            request_dict[request.id] = sub_dict

        print(request_dict)
        return request_dict

get_requests()