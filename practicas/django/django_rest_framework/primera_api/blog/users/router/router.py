from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path

urlpatterns = [
    path('auth/login', TokenObtainPairView.as_view(), name='login'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='token refresh'),
]