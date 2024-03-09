from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User

# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
	list_display = ['id', 'username', 'email', 'is_staff']
	
	"""Agregamos las modificaciones para la vista el usuario en el admin web"""
	fieldsets = (
		(None, {'fields': ('username', 'password')}),
		('Datos personales', {'fields': ('first_name', 'last_name', 'email')}),
		('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
		('Redes Solciales', {'fields': ('pagina_web', 'facebook')})
	)