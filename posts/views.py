from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import Category, Post

def published_posts():
    return Post.objects.filter(is_published=True, published_at__lte=timezone.now()).select_related("category")

def post_list(request):
    posts = published_posts()
    query = request.GET.get("q", "").strip()
    category = request.GET.get("mavzu", "")
    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(body__icontains=query) | Q(excerpt__icontains=query))
    if category:
        posts = posts.filter(category__slug=category)
    categories = Category.objects.annotate(total=Count("posts", filter=Q(posts__is_published=True, posts__published_at__lte=timezone.now()))).filter(total__gt=0)
    return render(request, "posts/list.html", {"page_obj": Paginator(posts, 6).get_page(request.GET.get("page")), "categories": categories, "query": query, "selected_category": category, "post_count": published_posts().count()})

def post_detail(request, slug):
    post = get_object_or_404(published_posts(), slug=slug)
    related = published_posts().filter(category=post.category).exclude(pk=post.pk)[:2]
    return render(request, "posts/detail.html", {"post": post, "related": related})
