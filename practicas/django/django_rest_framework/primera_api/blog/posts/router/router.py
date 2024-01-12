from rest_framework.routers import DefaultRouter
# from ..services.api import PostViewSet
from ..services.api import PostModelViewSet

router_post = DefaultRouter()

# router_post.register(prefix="posts", basename="posts", viewset=PostViewSet)
router_post.register(prefix="posts", basename="posts", viewset=PostModelViewSet)