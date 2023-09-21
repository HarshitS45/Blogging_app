"""blog_project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.contrib import admin
from django.urls import path, re_path, include
from blog_app import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from account.views import (
    registration_view, logout_view, 
    login_view, update_view  ,
    must_authenticate_view,
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.home_page, name='home_page'),
    re_path(r'^blog/', include('blog.urls', 'blog')),
    re_path(r'^must_auth/$', must_authenticate_view, name="must_auth"),
    re_path(r'^register/$', registration_view, name='register'),
    re_path(r'^logout/$', logout_view, name='logout'),
    re_path(r'^login/$', login_view, name='login'),
    re_path(r'^login/update_profile/$', update_view, name='update'),


    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_form.html'), name='password_reset_confirm'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)