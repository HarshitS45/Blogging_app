from django.shortcuts import render
from operator import attrgetter
from blog.models import BlogPost
from blog.views import get_blog_queryset
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def home_page(request):
    context = {}
    
    query = ""
    if request.GET:
        query = request.GET.get('query', '')
        context['query'] = str(query)

    blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True) # Sorts the blog post by their dates, here the latest/newest blog posts will comr first in the list.

    # Pagination
    page_number = request.GET.get('page', 1)
    blog_posts_paginator = Paginator(blog_posts, 5) # Shows 5 blog posts per page
    # try:
    blog_posts = blog_posts_paginator.get_page(page_number)
    # except PageNotAnInteger:
    #     blog_posts = blog_posts_paginator.page(BLOG_POST_PER_PAGE)
    # except EmptyPage:
    #     blog_posts = blog_posts_paginator.get_page(blog_posts_paginator.num_pages)
    blog_posts2 = BlogPost.objects.all().order_by('?')[:3]
    context['blog_posts'] = blog_posts
    context['blog_posts2'] = blog_posts2
    return render(request, 'blog_app/home.html', context)