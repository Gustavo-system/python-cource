from django.shortcuts import render, HttpResponse
from django.views.generic.base import View

# Create your views here.
class HelloWorld(View):
	def get(self, request):
		data = {
			"name" : "El pollo loco",
			"years" : 20,
		}
		return render(content="<h2>Hola mundo</h2>", context=data)