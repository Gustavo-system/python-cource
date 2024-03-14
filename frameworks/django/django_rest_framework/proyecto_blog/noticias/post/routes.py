from rest_framework.routers import DefaultRouter
from post.views import PostApiViewSet

routes_posts = DefaultRouter()

routes_posts.register(prefix="posts", basename="posts", viewset=PostApiViewSet)