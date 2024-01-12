from django.shortcuts import render, HttpResponse
from django.views.generic.base import View

# este es el codigo en una variable para poder responder con un html
# html_base = """
# <h1>Mi web personal</h1>
# <ul>
# 	<li> <a href="/"> Portada </a> </li>
# 	<li> <a href="/about-me"> Acerca de </a> </li>
# 	<li> <a href="/portfolio"> Portafolio </a> </li>
# 	<li> <a href="/contact"> Contacto </a> </li>
# </ul>
# """

# Create your views here.
def home(request):
	# retornamos algo de nuestra funcion
	# return HttpResponse(f"{html_base}<h2>Portada</h2>")
	return render(request=request, template_name="core/home.html") # importamos ahora una vista html


def about(request):
	return render(request=request, template_name="core/about.html")


def portfolio(request):
	return render(request=request, template_name="core/portfolio.html")


def contact(request):
	return render(request=request, template_name="core/contact.html")


# otra forma de generar las vistas es la siguente por medio de clases
# class HelloWorld(View):
# 	def get(self, request):
# 		return HttpResponse(content="<h2>Hola mundo</h2>")
# 		return render(request=request, template_name="core/home.html")