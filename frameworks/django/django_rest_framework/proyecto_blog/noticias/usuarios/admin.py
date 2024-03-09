from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from usuarios.models import User


@admin.register(User)
class User(UserAdmin):
	list_display = ['id', 'username', 'email', 'is_staff']