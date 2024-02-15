import datetime
import graphene
from graphene_federation import build_schema
# from peyha_backend.decorators.Permission import has_mutation_access
# from nircmis_uaaa_utils.EmailUtils import EmailNotifications
from uaa_utils.UserResolver import UserResolverUtils

from uaa_dto.UserAccount import  ForgotPasswordInputObject, UserInputObject, UserProfileAndRoleObjects, UserProfileObject, ChangePasswordInputObject, UserRegistrationInputObject
from uaa_dto.Response import ResponseObject

from django.contrib.auth.models import User
from ai_mpers_role_and_permission.models import UserRoles, UsersWithRoles
from uaa.models import ForgotPasswordRequestUsers, UsersProfiles

from uaa_dto_builder.account_builder import UserAccountBuilder
from uaa_utils.UserUtils import UserUtils
# from uaa_utils.NotificationUtils import NotificationsUtils


# from dotenv import dotenv_values

# config = dotenv_values(".env")

class RegisterUsersMutation(graphene.Mutation):
    class Arguments:
        input = UserRegistrationInputObject(required=True)
    response = graphene.Field(ResponseObject)

    @classmethod
    def mutate(self, root, info, input):
        # if input.password != input.confirm_password:
        #     self(response=ResponseObject.get_response(id="17"))
        # if input.password == input.confirm_password:
        if User.objects.filter(username = input.user_nickname).exists():
            return self(response=ResponseObject.get_response(id="3"))
        else:
            
            user = User.objects.create(
                first_name=input.user_first_name,
                last_name=input.user_last_name,
                username=input.user_nickname,                
            )
            user.set_password(input.user_nickname)
            user.save()

            user_profile = UsersProfiles.objects.create(
                profile_type=input.profile_type,
                profile_user=user,
                profile_title = input.profile_title,
                profile_is_active =True,
                user_nickname =input.user_nickname,
                profile_has_been_verified =True,
                profile_gender = None,
            )
            if input.profile_type == "DOCTOR":
                return self(response=ResponseObject.get_response(id="1"))
            else:
                return self(response=ResponseObject.get_response(id="4"))


class CreateUsersMutation(graphene.Mutation):
    class Arguments:
        input = UserInputObject(required=True)
        

    response = graphene.Field(ResponseObject)
    data = graphene.Field(UserProfileAndRoleObjects)

    @classmethod
    # @has_mutation_access(permissions=['can_manage_settings'])
    def mutate(self, root, info,  input):

        if "255"  not in str(input.profile_phone):          
            return self(response=ResponseObject.get_response(id="1"))



        user = User.objects.create(
            first_name=input.user_first_name,
            last_name=input.user_last_name,
            username=input.user_email,
            email=input.user_email,
        )


        user_profile = UsersProfiles.objects.create(
            profile_type=input.profile_type.value,
            profile_phone=input.profile_phone,
            profile_title=input.profile_title,
            profile_user=user,
            profile_gender = input.profile_gender.value if input.profile_gender else None,
        )

        UsersWithRoles.objects.create(
            user_with_role_role = UserRoles.objects.filter(role_unique_id=input.role_unique_id).first(),
            user_with_role_user=user
        )


        response_body = UserAccountBuilder.get_user_profile_and_role_data(id=user_profile.profile_unique_id)

        return self(response=ResponseObject.get_response(id="1"), data=response_body)

class UpdateUsersMutation(graphene.Mutation):
    class Arguments:
        input = UserInputObject(required=True)

    response = graphene.Field(ResponseObject)
    data = graphene.Field(UserProfileAndRoleObjects)

    @classmethod
    # @has_mutation_access(permissions=['can_manage_settings'])
    def mutate(self, root, info,  input):



        profile = UsersProfiles.objects.filter(profile_is_active=True, profile_unique_id=input.profile_unique_id).first()

        if profile is None:
            return self(response=ResponseObject.get_response(id="6"), data=None)

        if "255"  not in str(input.profile_phone):          
            return self(response=ResponseObject.get_response(id="20"))

        profile.profile_phone = input.profile_phone
        profile.profile_title = input.profile_title
        profile.profile_type=input.profile_type.value
        profile.profile_photo = input.profile_photo
        profile.profile_gender = input.profile_gender.value if input.profile_gender else None
        profile.save()

        profile.profile_user.first_name = input.user_first_name
        profile.profile_user.last_name = input.user_last_name
        profile.profile_user.email = input.user_email
        profile.profile_user.save()

        UsersWithRoles.objects.filter(user_with_role_user=profile.profile_user).update(
            user_with_role_role = UserRoles.objects.filter(role_unique_id=input.role_unique_id).first(),
        )

        
        response_body = UserAccountBuilder.get_user_profile_and_role_data(id=profile.profile_unique_id)

        return self(response=ResponseObject.get_response(id="1"), data=response_body)
    
class DeleteUsersMutation(graphene.Mutation):
    class Arguments:
        profile_unique_id = graphene.String(required=True)

    response = graphene.Field(ResponseObject)

    @classmethod
    # @has_mutation_access(permissions=['can_manage_settings'])
    def mutate(self, root, info,  profile_unique_id):

        admin_profile = UsersProfiles.objects.filter(profile_unique_id=profile_unique_id).first()
        admin_profile.profile_type = ""
        admin_profile.profile_is_active = False
        admin_profile.save()
        admin_profile.profile_user.is_active = False
        admin_profile.profile_user.save()

        return self(response=ResponseObject.get_response(id="1"))

class UpdateMyProfileMutation(graphene.Mutation):
    class Arguments:
        input = UserInputObject()

    response = graphene.Field(ResponseObject)
    data = graphene.Field(UserProfileObject)

    @classmethod
    def mutate(self, root, info,  input):

        profile_unique_id = UserResolverUtils.__profile__(info)

        profile = UsersProfiles.objects.filter(profile_unique_id=profile_unique_id, profile_is_active=True).first()

        if profile is None:
            return self(response=ResponseObject.get_response(id="6"), data=None)
        

        if "255"  not in str(input.profile_phone):          
            return self(response=ResponseObject.get_response(id="1"))

        profile.profile_phone = input.profile_phone
        profile.profile_title = input.profile_title
        profile.profile_photo = input.profile_photo
        profile.profile_gender = input.profile_gender.value if input.profile_gender else None
        profile.save()

        profile.profile_user.first_name = input.user_first_name
        profile.profile_user.last_name = input.user_last_name
        profile.profile_user.email = input.user_email
        profile.profile_user.save()

        response_body = UserAccountBuilder.get_user_profile_data(id=profile.profile_unique_id)

        return self(response=ResponseObject.get_response(id="1"), data=response_body)


class ChangePasswordMutation(graphene.Mutation):
    class Arguments:
        input = ChangePasswordInputObject()

    response = graphene.Field(ResponseObject)

    @classmethod
    # @has_mutation_access(permissions=['can_manage_settings'])
    def mutate(self, root, info,  input):
        profile_unique_id = UserResolverUtils.__profile__(info)

        if not profile_unique_id:
            self(response=ResponseObject.get_response(id="6"))

        profile = UsersProfiles.objects.filter(profile_unique_id=profile_unique_id).first()

        if input.password_1 != input.password_2:
            self(response=ResponseObject.get_response(id="17"))

        profile.profile_user.set_password(input.password_1)
        profile.profile_user.save()
        profile.profile_has_been_verified = True
        profile.save()

        return self(response=ResponseObject.get_response(id="1"))
    

class ResetPasswordMutation(graphene.Mutation):
    class Arguments:
        input = ForgotPasswordInputObject()

    response = graphene.Field(ResponseObject)

    @classmethod
    # @has_mutation_access(permissions=['can_manage_settings'])
    def mutate(self, root, info,  input):

        user_password_request = ForgotPasswordRequestUsers.objects.filter(
                request_token = input.token
            ).first()
        
        
        if  user_password_request is None:
            return self(response=ResponseObject.get_response(id="8"))


        if input.password_1 != input.password_2:
            return self(response=ResponseObject.get_response(id="17"))

        user = user_password_request.request_user

        user.set_password( input.password_1)
        user.save()

        return self(response=ResponseObject.get_response(id="1"))
    


class Mutation(graphene.ObjectType):
    register_user_mutation = RegisterUsersMutation.Field()
    create_users_mutation = CreateUsersMutation.Field()
    update_users_mutation = UpdateUsersMutation.Field()
    delete_users_mutation = DeleteUsersMutation.Field()
    
    update_my_user_profile_mutation = UpdateMyProfileMutation.Field()

    reset_password_mutation  = ResetPasswordMutation.Field()
    
    change_password_mutation = ChangePasswordMutation.Field()


schema = build_schema(Mutation, types=[])

