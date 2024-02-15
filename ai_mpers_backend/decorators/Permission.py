import json
from uaa_dto.Response import ResponseObject


def has_mutation_access(permissions=[]):
    """
    This function validates the access for the given user.
    From the request header, it takes parmission that was obteained from UAA service
    and validate against give permissions that guard the access to specific endpoint.
    """
    
    def decorator(view_func):
        def wrap(info, *args, **kwargs):
            try:
                if not permissions:
                    info.response = ResponseObject.get_response(id="2")
                    return info

                _, headers_part = args 

                user_data = json.loads(headers_part.context.headers['User'])
                has_give_permissions = set(permissions).issubset(set(user_data['user_permissions']))

                if has_give_permissions:
                    return view_func(info, *args, **kwargs)
                else:
                    info.response = ResponseObject.get_response(id="2")
                    try:
                        info.data = None
                    except:
                        pass
                    return info
            except:
                info.response = ResponseObject.get_response(id="2")
                try:
                    info.data = None
                except:
                    pass
                return info
        return wrap

    return decorator


def has_query_access(permissions=[]):
    """
    This function validates the access for the given user.
    From the request header, it takes parmission that was obteained from UAA service
    and validate against give permissions that guard the access to specific endpoint.
    """
    
    def decorator(view_func):
        def wrap(info, *args, **kwargs):
            try:
                if not permissions:
                    return responseObject(response=ResponseObject.get_response(id="9"), data=None)

                headers_part = args[0] 
                responseObject = headers_part.return_type.graphene_type

                user_data = json.loads(headers_part.context.headers['User'])
                has_give_permissions = set(permissions).issubset(set(user_data['user_permissions']))

                if has_give_permissions:
                    return view_func(info, *args, **kwargs)
                else:
                    return responseObject(response=ResponseObject.get_response(id="2"), data=None)
            except:
                return responseObject(response=ResponseObject.get_response(id="2"), data=None)
        return wrap

    return decorator
