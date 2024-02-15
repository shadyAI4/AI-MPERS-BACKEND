import graphene
from graphene import ObjectType
# from ai_mpers_backed.decorators.Permission import has_query_access

from uaa_dto.account_object import UserRoleResponseObject, UserRolesFilteringInputObjects, GroupedPermissionsResponseObject, PermisionFilteringInputObjects
from uaa_dto.Response import ResponseObject
from ai_mpers_role_and_permission.models import UserRoles, UserPermissionsGroup
from uaa_dto_builder.UAABuilder import UAABuilder

class Query(ObjectType): 
    get_roles = graphene.Field(UserRoleResponseObject,filtering=UserRolesFilteringInputObjects(required=True))
    get_system_permissions = graphene.Field(GroupedPermissionsResponseObject,filtering=PermisionFilteringInputObjects(required=True))

    # @has_query_access(permissions=['can_manage_settings'])
    def resolve_get_roles(self, info,filtering=None,**kwargs):
        try:

            roles=UserRoles.objects.filter(role_is_active=True).all()

            if filtering.role_unique_id is not None:
                roles=roles.filter(role_unique_id=filtering.role_unique_id).all()

            roles_list=[]
            for role in roles:
                roles_list.append(UAABuilder.get_role_data(role.role_unique_id))
            
            return UserRoleResponseObject(response=ResponseObject.get_response(id="1"),data=roles_list)
        except Exception as e:
            print(e)
            return UserRoleResponseObject(response=ResponseObject.get_response(id="4"))
    
    # @has_query_access(permissions=['can_manage_settings'])
    def resolve_get_system_permissions(self, info,filtering=None,**kwargs):
        try:
            permission_groups=UserPermissionsGroup.objects.filter(permission_group_is_global=False).all()
            
            if filtering.group_is_global is not None:
                permission_groups=permission_groups.filter(permission_group_is_global=filtering.group_is_global).all()
            
            if filtering.permission_group_unique_id is not None :
                permission_groups=permission_groups.filter(permission_group_unique_id=filtering.permission_group_unique_id).all()    
            
            permission_group_list=[]
            for permission_group in permission_groups:
                permission_group_list.append(UAABuilder.get_group_permissions_data(permission_group.permission_group_unique_id))
            
            return GroupedPermissionsResponseObject(response=ResponseObject.get_response(id="1"),data=permission_group_list)
        except:
            return GroupedPermissionsResponseObject(response=ResponseObject.get_response(id="4"))
