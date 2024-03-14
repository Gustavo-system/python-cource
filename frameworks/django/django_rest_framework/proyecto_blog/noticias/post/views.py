from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from post.models import Post
from post.serializers import PostSerializer


class PostApiViewSet(ModelViewSet):
	serializer_class = PostSerializer
	queryset = Post.objects.filter(publicado=True)
	filter_backends = [DjangoFilterBackend]
	# se puede realizar el filtrado de las dos maneras que se muestran abajo y junto # filterset_fields = ['categoria', 'categoria__slug']
	filterset_fields = ['categoria']
	# filterset_fields = ['categoria__slug'] # aqui le estamos indicando por cual key sera el filtrado