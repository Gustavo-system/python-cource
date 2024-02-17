from rest_framework.routers import DefaultRouter
from categorias.services.services import CategoriaApiViewSet


router_categorias = DefaultRouter()

router_categorias.register(prefix="categorias", basename="categorias", viewset=CategoriaApiViewSet)