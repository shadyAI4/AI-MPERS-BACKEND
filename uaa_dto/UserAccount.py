import graphene

from uaa.models import UsersProfiles
from uaa_dto.account_object import UserRoleObjects
from uaa_dto.Response import ResponseObject
from .Enums import GenderEnum, UserEnum
from graphene_federation import key,external,extend
from .Referenced import PageObject


class UserInputObject(graphene.InputObjectType):
    profile_unique_id = graphene.String()
    user_first_name = graphene.String()
    user_last_name = graphene.String()
    user_email = graphene.String()
    profile_phone = graphene.String()
    profile_title = graphene.String()
    profile_photo = graphene.String()
    user_nickname = graphene.String()
    profile_type = UserEnum()
    role_unique_id = graphene.String()

class UserRegistrationInputObject(graphene.InputObjectType):
    user_first_name = graphene.String()
    user_last_name = graphene.String()
    user_nickname = graphene.String()
    # password = graphene.String()
    profile_title = graphene.String()
    profile_type = graphene.String()
    # profile_type = UserEnum()
    # role_unique_id = graphene.String()
    # confirm_password = graphene.String()
    
class UserObject(graphene.ObjectType):
    user_first_name = graphene.String()
    user_last_name = graphene.String()
    user_email = graphene.String()
    profile_phone = graphene.String()
    profile_is_active = graphene.Boolean()
    profile_username=graphene.String()

class UserObjectProfile(graphene.ObjectType):
    id = graphene.String()
    profile_title = graphene.String()
    profile_photo = graphene.String()
    profile_gender = graphene.String()
    profile_type = graphene.String()
    profile_has_been_verified = graphene.Boolean()
    user_nickname = graphene.String()
    profile_user=graphene.Field(UserObject)

class UserProfileObject(graphene.ObjectType):
    id = graphene.String()
    profile_unique_id = graphene.String()
    user_first_name = graphene.String()
    user_last_name = graphene.String()
    user_email = graphene.String()
    profile_phone = graphene.String()
    profile_title = graphene.String()
    profile_photo = graphene.String()
    profile_gender = graphene.String()
    profile_is_active = graphene.Boolean()
    profile_type = graphene.String()
    profile_has_been_verified = graphene.Boolean()
    profile_username=graphene.String()
    user_nickname = graphene.String()

class ProfileResponseObject(graphene.ObjectType):
    response = graphene.Field(ResponseObject)
    data = graphene.List(UserProfileObject)
    page = graphene.Field(PageObject)



class UserFilteringInputObject(graphene.InputObjectType):
    profile_type = UserEnum()
    page_number = graphene.Int(required=True)
    profile_unique_id = graphene.String()


class UserProfileAndRoleObjects(graphene.ObjectType):
    id = graphene.String()
    user_profile = graphene.Field(UserProfileObject)
    user_roles = graphene.Field(UserRoleObjects)
    # designation = graphene.Field(DesignationObjects)

class UserProfileAndRoleResponseObject(graphene.ObjectType):
    response = graphene.Field(ResponseObject)
    data = graphene.Field(UserProfileAndRoleObjects)

class UsersResponseObject(graphene.ObjectType):
    response = graphene.Field(ResponseObject)
    data = graphene.List(UserProfileAndRoleObjects)
    page = graphene.Field(PageObject)

class ChangePasswordInputObject(graphene.InputObjectType):
    current_password = graphene.String()
    password_1 = graphene.String()
    password_2 = graphene.String()

class ForgotPasswordInputObject(graphene.InputObjectType):
    token = graphene.String(required=True)
    password_1 = graphene.String()
    password_2 = graphene.String()



