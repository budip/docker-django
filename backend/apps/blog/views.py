from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .models import BlogPost
from .serializers import BlogPostSerializer
import json

class BlogPostViewSet(viewsets.ModelViewSet):
    """
    API endpoint for CRUD operations on BlogPost
    """
    queryset = BlogPost.objects.all().order_by('-created_at')  # Show newest first
    serializer_class = BlogPostSerializer

def blog_posts(request):
    posts = BlogPost.objects.all().values('id', 'title', 'content', 'published_date')
    return JsonResponse(list(posts), safe=False)

def blog_post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return JsonResponse({
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "published_date": post.published_date,
    })

@csrf_exempt  # Disable CSRF for simplicity (Use proper CSRF handling in production)
def create_blog_post(request):
    try:
        data = json.loads(request.body)
        new_post = BlogPost.objects.create(title=data['title'], content=data['content'])
        return JsonResponse({"message": "Blog post created!", "id": new_post.id}, status=201)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
    
@csrf_exempt
def update_blog_post(request, post):
    try:
        data = json.loads(request.body)
        post.title = data.get("title", post.title)
        post.content = data.get("content", post.content)
        post.save()
        return JsonResponse({"message": "Blog post updated!"}, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)    