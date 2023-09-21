from django.urls import re_path, path
from .views import (
    create_blog_view, blog_details_view,
    update_blog_post_view, delete_blog_post
    )

app_name = 'blog'

urlpatterns = [
    re_path(r'^create_post/$', create_blog_view, name="create_blog_post"),
    path('<slug>/', blog_details_view, name="blog_details"),
    path('<slug>/edit', update_blog_post_view, name="update_blog_post"),
    path('<slug>/delete', delete_blog_post, name="delete_blog_post"),
]