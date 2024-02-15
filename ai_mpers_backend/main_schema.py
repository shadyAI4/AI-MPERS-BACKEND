import graphene
from graphene_django import DjangoObjectType
# from graphql_auth import mutations
# import graphql_jwt
from graphene_federation import build_schema




# # from graphql_auth.schema import UserQuery, MeQuery
from uaa.schema import Query as uaa_query
from uaa.views import Mutation as uaa_mutation
from patients.views import Mutation as patients_mutation
from patients.schema import Query as patients_query

class Query(uaa_query,patients_query,graphene.ObjectType):
    print("here we go")
    pass
class Mutation(uaa_mutation,patients_mutation,graphene.ObjectType):
    pass

schema = build_schema(query=Query, mutation=Mutation)