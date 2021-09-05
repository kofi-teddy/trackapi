import graphene
import graphql_jwt

from apps.tracks import schema as track_schaema
from apps.users import schema as user_schema


class Query(user_schema.Query, track_schaema.Query, graphene.ObjectType):
    pass


class Mutation(user_schema.Mutation, track_schaema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
