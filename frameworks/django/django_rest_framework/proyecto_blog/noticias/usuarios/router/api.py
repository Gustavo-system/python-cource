from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from usuarios.services.services import RegisterView, UserView


urlpatterns = [
	path(route='auth/register', view=RegisterView.as_view(), name="Registra un usuario"),
	path(route='auth/token/login', view=TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(route='auth/token/refresh', view=TokenRefreshView.as_view(), name='token_refresh'),
    path(route='user', view=UserView.as_view(), name='Usuarios'),
]