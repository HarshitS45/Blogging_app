from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from .forms import (CreateBlogPostForm,
                    UpdateBlogPostForm
                    )
from account.models import Account
from .models import BlogPost

from blog.models import (
    BlogPost
)
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from random import shuffle
# Create your views here.

def create_blog_view(request):
    """The view to create a blog post"""
    if not request.user.is_authenticated:
        return redirect ('must_auth')
    context = {}

    user = request.user
    create_blog_form = CreateBlogPostForm(request.POST or None, request.FILES or None)
    if create_blog_form.is_valid():
        obj = create_blog_form.save(commit=False)
        author = Account.objects.filter(email=user.email).first() # Return a queryset '.first' gets the first item there
        obj.author = author
        obj.save()
        context['success_message'] = f"'{obj.title}' has been posted."
        create_blog_form = CreateBlogPostForm()
        return redirect('home_page')
    else:
        create_blog_form = CreateBlogPostForm()
    context['create_blog_form'] = create_blog_form
    return render(request, 'blog/create_blog.html', context)


def blog_details_view(request, slug):
    """The view to get the details of a blog"""
    context = {}
    blog_details = get_object_or_404(BlogPost, slug=slug)
    # blog_posts = BlogPost.objects.all()[:3]
    # blog_posts = sorted(BlogPost, key=attrgetter('date_updated'), reverse=True)[:5]
    blog_posts = BlogPost.objects.filter(date_published__lte=timezone.now()).order_by('?')[:3]
    context['blog_post'] = blog_posts
    context['blog_details'] = blog_details
    return render(request, 'blog/blog_details.html', context)


def update_blog_post_view(request, slug):
    """The view to update a blog post"""
    context = {}
    user = request.user
    if not user.is_authenticated:
        redirect('must_auth')

    blog_post = get_object_or_404(BlogPost, slug=slug)

    if user != blog_post.author:
        return HttpResponse("<h3>You are not the author of this post!</h3>")

    if request.method == 'POST':
        update_form = UpdateBlogPostForm(request.POST or None, request.FILES or None, instance=blog_post)
        if update_form.is_valid():
            update_form.save()
            context['success_message'] = f"'{blog_post.title}' has been updated."
            return redirect('home_page')

    # else:
    update_form = UpdateBlogPostForm(instance=request.user, initial = {
                "title": blog_post.title,
                "body": blog_post.body,
                "image": blog_post.image,
        })

    context['blog_post'] = blog_post
    context['update_form'] = update_form
    return render(request, 'blog/edit_blog_post.html', context)

def get_blog_queryset(query=None):
    """The view that performs the search functionality"""
    queryset = []
    queries = query.split(" ") # To remove the whitespaces between queries
    for query in queries:
        posts = BlogPost.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        ).distinct()

        for post in posts:
            queryset.append(post)

    return list(set(queryset))

def delete_blog_post(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)
    # perform some validation, 
    # like can this user delete this post or not, etc.
    # if validation is successful, delete the article
    blog_post.delete()
    return HttpResponseRedirect('/')

# def timezones_view(request):

#     tzname = pytz.timezone("Europe/Berlin")
#     timezone.activate(pytz.timezone(tzname))

#     render(request, 'blog')