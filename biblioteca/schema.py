import graphene
import libro.schema

class Query(libro.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)