from django.db import models
from django.db.models import SET_NULL
from usuarios.models import User
from categorias.models import Categoria

class Post(models.Model):
	titulo = models.CharField(max_length=255)
	contenido = models.TextField()
	slug = models.SlugField(max_length=255, unique=True)
	publicado = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	usuario = models.ForeignKey(User, on_delete=SET_NULL, null=True)
	categoria = models.ForeignKey(Categoria, on_delete=SET_NULL, null=True)


	def __str__(self):
		return self.titulo