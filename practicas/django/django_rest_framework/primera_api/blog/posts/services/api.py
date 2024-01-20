# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from posts.models import Post
# from ..serializers.serializers import PostSerializer
# from utils.BaseResponse import BaseResponse

# class PostApiView(APIView):

# 	# se sobre escribe el metodo get
# 	def get(self, request):
# 		# post = Post.objects.all()
# 		# post = [post.title for post in Post.objects.all()]
# 		post_serializer = PostSerializer(Post.objects.all(), many=True)
# 		# base_response = BaseResponse(200, "Datos Obtenidos", post_serializer.data)
# 		# response = base_response.general_response()
# 		response = BaseResponse(200, "Datos Obtenidos", post_serializer.data).general_response()
# 		return Response(status=status.HTTP_200_OK, data=response)
	

# 	def post(self, request):
# 		# Post.objects.create(
# 		# 	title=request.POST['title'],
# 		# 	description=request.POST['description']
# 		# )

# 		# return self.get(request=request)

# 		# utilizando serializer
# 		serializer = PostSerializer(data=request.POST)
# 		serializer.is_valid(raise_exception=True)
# 		serializer.save()
# 		response = BaseResponse(201, "Registro creado exitosamente").general_response()
# 		return Response(status=status.HTTP_201_CREATED, data=response)
	

"""
Otra forma de realizar los endpoints con ViewSet
"""
# from rest_framework import status
# from rest_framework.viewsets import ViewSet
# from rest_framework.response import Response
# from utils.BaseResponse import BaseResponse
# from posts.models import Post
# from ..serializers.serializers import PostSerializer

# class PostViewSet(ViewSet):

# 	# se sobre escribe el metodo get
# 	def list(self, request):
# 		post_serializer = PostSerializer(Post.objects.all(), many=True)
# 		response = BaseResponse(200, "Datos Obtenidos", post_serializer.data).general_response()
# 		return Response(status=status.HTTP_200_OK, data=response)
	
# 	def retrieve(self, request, pk:int):
# 		post_serializer = PostSerializer(Post.objects.get(pk=pk))
# 		response = BaseResponse(200, "Datos Obtenidos", post_serializer.data).general_response()
# 		return Response(status=status.HTTP_200_OK, data=response)
	

# 	def create(self, request):
# 		serializer = PostSerializer(data=request.POST)
# 		serializer.is_valid(raise_exception=True)
# 		serializer.save()
# 		response = BaseResponse(201, "Registro creado exitosamente").general_response()
# 		return Response(status=status.HTTP_201_CREATED, data=response)

"""
Otra forma de realizar los endpoints con ModelViewSet
"""
from rest_framework.viewsets import ModelViewSet
from ..serializers.serializers import PostSerializer
from posts.models import Post
from ..permissions.permissions import IsAdminOrReadOnly


class PostModelViewSet(ModelViewSet):
	"""Se genera un crud de forma rapida"""
	permission_classes = [IsAdminOrReadOnly] # se pueden agregar mas permisos separados por una (,)
	serializer_class = PostSerializer
	queryset = Post.objects.all()
	http_method_names = ['get', 'post', 'put', 'delete'] # indica que metodos se generaran