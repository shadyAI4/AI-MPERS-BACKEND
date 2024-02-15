import graphene
from graphene import ObjectType

from .models import UsersProfiles
# from peyha_backend.decorators.Permission import has_query_access
from uaa_dto.Referenced import PageObject
from uaa_dto_builder.account_builder import UserAccountBuilder
from uaa_dto.Response import ResponseObject
from uaa_dto.UserAccount import UserProfileAndRoleResponseObject, UsersResponseObject, UserFilteringInputObject, ProfileResponseObject
from django.db.models import Q
from django.core.paginator import Paginator
from uaa_utils.UserUtils import UserUtils


class Query(ObjectType): 
    print("it reach heere")
    get_users = graphene.Field(ProfileResponseObject,filtering=UserFilteringInputObject())
    get_user_profile_and_role = graphene.Field(UserProfileAndRoleResponseObject)


    # @has_query_access(permissions=['can_view_users'])
    def resolve_get_users(self, info,filtering=None,**kwargs):
        filters=Q(profile_is_active=True)
        
        if filtering.profile_type is not None:
            filters &= Q(profile_type = filtering.profile_type)
            
        if filtering.profile_unique_id is not None:
            filters &= Q(profile_unique_id = filtering.profile_unique_id)

        else:
            filters &= Q(profile_type__ne = "PLAYER")
            
        all_users =UsersProfiles.objects.filter(filters).values('profile_unique_id')         
        
        paginated_users=Paginator(all_users,50)
        all_users=paginated_users.page(filtering.page_number)
        page_object=PageObject.get_page(all_users)
            
        all_users_list = list(map(lambda x: UserAccountBuilder.get_user_profile_data(str(x['profile_unique_id'])), all_users))
        
        return UsersResponseObject(response=ResponseObject.get_response(id="6"),data=all_users_list , page = page_object)

    def resolve_get_user_profile_and_role(self, info,**kwargs):
        print("Here it work")
        profile_unique_id = UserUtils.__profile__(info.context.user)
        print("But here it not work")
        print("I think this is the profileuniqueId ", profile_unique_id)
        profile=UsersProfiles.objects.filter(profile_unique_id=profile_unique_id).first()
        print("And this is my profile", profile)
        if profile is None:
            return info.return_type.graphene_type(response=ResponseObject.get_response(id="34"))

        user_object=UserAccountBuilder.get_user_profile_and_role_data(profile.profile_unique_id)
        
        return info.return_type.graphene_type(response=ResponseObject.get_response(id="6"),data=user_object)



schema = graphene.Schema(query=Query)