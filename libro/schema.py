import graphene 
from graphene_django.types import DjangoObjectType
from libro.models import Categoria, Libro

class TipoCategoria(DjangoObjectType):
    class Meta:
        model = Categoria

class TipoLibro(DjangoObjectType):
    class Meta:
        model = Libro

class Query(object):
    all_Categorias = graphene.List(TipoCategoria)
    allLibros = graphene.List(TipoLibro)

    def resolve_all_Categorias(self, info, **kwargs):
        return Categoria.objects.all()
    
    def resolve_allLibros (self, info, **kwargs):
        return Libro.objects.select_related('Categoria').all()

    def resolve_hello(self, info, **kwargs):
        return "world"

class NuevoLibro(graphene.Mutation):
    id = graphene.Int()
    titulo = graphene.String()
    sinopsis = graphene.String()
    autor = graphene.String()
    Categoria_id = graphene.Int(name="Categoria")

    class Arguments:
        titulo = graphene.String()
        sinopsis = graphene.String()
        autor = graphene.String()
        Categoria_id = graphene.Int(name="Categoria")

    
    def mutate(self, info, titulo, sinopsis, autor, Categoria_id):
        libro = Libro(titulo=titulo, sinopsis=sinopsis, autor=autor, Categoria_id=Categoria_id)
        libro.save()

        return NuevoLibro(
            id=libro.id,
            titulo=libro.titulo,
        )

class Mutation(graphene.ObjectType):
    crear_libro = NuevoLibro.Field()

