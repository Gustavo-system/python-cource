from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from usuarios.serializers.serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerializer
from usuarios.models import User


class RegisterView(APIView):
	
	def post(self, request):

		user_serializer = UserRegisterSerializer(data=request.data)

		if user_serializer.is_valid(raise_exception=True):
			user_serializer.save()
			return Response(user_serializer.data, status=status.HTTP_201_CREATED)

		return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	

class UserView(APIView):
	permission_classes = [IsAuthenticated]

	def get(self, request):
		user_serializer = UserSerializer(request.user)
		return Response(status=status.HTTP_200_OK, data=user_serializer.data)

	def put(self, request):
		user = User.objects.get(id=request.user.id)
		user_serializer = UserUpdateSerializer(user, data=request.data)
		if user_serializer.is_valid(raise_exception=True):
			user_serializer.save()
			return Response(status=status.HTTP_200_OK, data=user_serializer.data)

		return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
