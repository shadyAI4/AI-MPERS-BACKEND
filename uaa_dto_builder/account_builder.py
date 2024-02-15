from uaa.models import UsersProfiles
from ai_mpers_role_and_permission.models import UsersWithRoles
from uaa_dto_builder.UAABuilder import UAABuilder
from uaa_dto.UserAccount import UserProfileAndRoleObjects, UserProfileObject


class UserAccountBuilder:
    
    @staticmethod
    def get_user_profile_data(id):
        try:
            user_profile=UsersProfiles.objects.filter(profile_unique_id=id).first()
          
            return UserProfileObject(
                id = user_profile.primary_key,
                profile_unique_id = user_profile.profile_unique_id,
                user_first_name = user_profile.profile_user.first_name,
                user_last_name = user_profile.profile_user.last_name,
                user_email = user_profile.profile_user.email,
                profile_title = user_profile.profile_title,
                profile_photo = user_profile.profile_photo,
                profile_is_active = user_profile.profile_is_active,
                profile_type = user_profile.profile_type,
                profile_gender = user_profile.profile_gender,
                user_nickname = user_profile.user_nickname,
                profile_has_been_verified = user_profile.profile_has_been_verified,
                profile_username=user_profile.profile_user.username,
            )
        except Exception as e:
            print("I failed")
            return UserProfileObject()

    @staticmethod
    def get_user_profile_and_role_data(id):
        try:
            user_profile=UsersProfiles.objects.filter(profile_is_active=True,profile_unique_id=id).first()
            user_with_role= UsersWithRoles.objects.filter(user_with_role_user=user_profile.profile_user).first()
        
            
            return UserProfileAndRoleObjects(
                id = user_profile.primary_key,
                user_profile = UserAccountBuilder.get_user_profile_data(user_profile.profile_unique_id),
                user_roles = UAABuilder.get_role_data(id=user_with_role.user_with_role_role.role_unique_id if user_with_role else None),
            )
           
        except Exception as e:
            return UserProfileAndRoleObjects()
        