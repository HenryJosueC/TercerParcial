import graphene
import libro.schema

class Query(libro.schema.Query, graphene.ObjectType):
    pass

class Mutation(libro.schema.Mutation, graphene.ObjectType):
    pass
schema = graphene.Schema(query=Query, mutation=Mutation)