from ai_mpers_role_and_permission.models import UsersWithRoles
from uaa.models import UsersProfiles
from ai_mpers_internal_request.BearerTokenAuthentication import BearerTokenAuthentication
from uaa_dto_builder.UAABuilder import UAABuilder
import uuid


class UserUtils:
    def __profile__(request):
        print("here it ")
        user_data = UserUtils.get_user(request)
        print("But here no")
        return user_data['profile_unique_id']
    
    def get_user_permissions(user):
        print("I think i can get in")
        user_with_role= UsersWithRoles.objects.filter(user_with_role_user=user).first()
        if not user_with_role:
            return []
        user_roles = UAABuilder.get_role_data(id=user_with_role.user_with_role_role.role_unique_id)
        user_permissions =[]
        for permission in user_roles.role_permissions:
            user_permissions.append(permission.permission_code)
        return user_permissions

    def get_user_approval_stages(profile_desigantion):
        my_approval_stages = []
        if profile_desigantion is not None:
            all_stages = profile_desigantion.user_designation.get_designation_approval_stages()
            if all_stages is not None:
                my_approval_stages = list(map(lambda x: {'flow_process':x.stage_flow.flow_process,"stage_unique_id":str(x.stage_unique_id)}, all_stages))
        return my_approval_stages
    
    
    def get_user(user = None, request = None): 
        if user is None:
            is_authenticated, user = BearerTokenAuthentication.authenticate(None,request)
        print("I gues here ")
            
        profile=UsersProfiles.objects.filter(profile_user=user).first()
        print("I dont gues here")
        print("this is the profile", profile.profile_type)
        user_data={
            'profile_unique_id':str(profile.profile_unique_id),
            'first_name':user.first_name,
            'last_name':user.last_name,
            'username':user.username,
            'email':user.email,
            'user_permissions':UserUtils.get_user_permissions(user),
            'user_type':profile.profile_type,
        }

        print("Still guessing")
        return user_data
    
    def get_forgot_password_token():
        token =  str(uuid.uuid4())
        return token
    
    
