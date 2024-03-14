from rest_framework import serializers
from post.models import Post
from usuarios.serializers.serializers import UserSerializer
from categorias.serializers.serializers import CategoriaSerializer


class PostSerializer(serializers.ModelSerializer):

	# se agregan las relaciones de las llaves foraneas declaradas
	usuario = UserSerializer()
	categoria = CategoriaSerializer()

	class Meta:
		model = Post
		fields= "__all__"
