from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from usuarios.models import User
from usuarios.serializers.serializers import UserRegisterSerializer


class UserService(APIView):
	
	def post(self, request):

		user_serializer = UserRegisterSerializer(data=request.data)

		if user_serializer.is_valid(raise_exception=True):
			user_serializer.save()
			return Response(user_serializer.data, status=status.HTTP_201_CREATED)

		return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)