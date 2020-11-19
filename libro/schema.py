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
