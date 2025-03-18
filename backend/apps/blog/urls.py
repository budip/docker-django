from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet

# Use a router for automatic URL configuration
router = DefaultRouter()
router.register(r'posts', BlogPostViewSet, basename='blogpost')

urlpatterns = [
    path('', include(router.urls)),
]
