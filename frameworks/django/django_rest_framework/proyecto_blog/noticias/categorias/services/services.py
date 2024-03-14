from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from categorias.models import Categoria
from categorias.serializers.serializers import CategoriaSerializer
from categorias.permissions.permissions import IsAdminOrReadOnly

class CategoriaApiViewSet(ModelViewSet):
	permission_classes = [IsAdminOrReadOnly]
	serializer_class = CategoriaSerializer
	queryset = Categoria.objects.all() # retornar toda la informacion
	# queryset = Categoria.objects.filter(publicado=True) # agregamos un foltrado estatico

	lookup_field = 'slug' # una forma de cambiar el parametro para filtrar

	# utilizando filtrados personalizados intalando django_filter
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['title', 'slug', 'publicado']
