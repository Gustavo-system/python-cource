from rest_framework.viewsets import ModelViewSet
from categorias.models import Categoria
from categorias.serializers.serializers import CategoriaSerializer


class CategoriaApiViewSet(ModelViewSet):
	serializer_class = CategoriaSerializer
	queryset = Categoria.objects.all()