from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet, blog_posts, blog_post_detail

# Use a router for automatic URL configuration
router = DefaultRouter()
router.register(r'posts', BlogPostViewSet, basename='blogpost')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/', blog_posts, name='blog_posts'),
    path('posts/<int:post_id>/', blog_post_detail, name='blog_post_detail'),
]
