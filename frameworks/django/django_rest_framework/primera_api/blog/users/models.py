from django.db import models
from django.contrib.auth.models import AbstractUser

# se declara el modelo vacio ya que se esta heredando del modelo AbstracUser
# y se tienen campos por default, si quieren agregar otros campos se hace como la parte de abahi
# class User(AbstractUser):
# 	pass


# se agregan nuevos campos adicionales a la herencia que tiene
class User(AbstractUser):
	email = models.EmailField(unique=True)
	pagina_web = models.CharField(max_length=255, blank=True)
	facebook = models.CharField(max_length=255, blank=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []