from graphql import GraphQLError

from ai_mpers_role_and_permission.models import UsersWithRoles


class AccessControl:
    def user_has_access(permissions=[], user_id=None):
        if user_id is None or len(permissions) < 1:
            return False

        all_user_roles = UsersWithRoles.objects.filter(user_with_role_user_id=user_id).first()
        has_give_permissions=False

        if all_user_roles is not None:
            has_give_permissions = all_user_roles.user_with_role_role.get_role_permissions().filter(role_with_permission_permission__permission_code__in=permissions).exists()
        
        return has_give_permissions

               
