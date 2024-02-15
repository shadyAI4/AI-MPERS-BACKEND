import json


class UserResolverUtils(object):
  
    def __profile__(request,process=None):
        print("request.context.headers")
        print(request.context.headers)
        user_data = json.loads(request.context.headers['User'])
        
        profile_unique_id=user_data['profile_unique_id']
        return profile_unique_id
