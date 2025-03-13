from rest_framework import viewsets
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    """
    API endpoint for CRUD operations on BlogPost
    """
    queryset = BlogPost.objects.all().order_by('-created_at')  # Show newest first
    serializer_class = BlogPostSerializer
