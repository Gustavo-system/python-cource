from django.urls import path
from usuarios.services.services import UserService


urlpatterns = [
	path(route='auth/register', view=UserService.as_view(), name="Registra un usuario")
]