from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import AccountUpdateForm, RegistrationForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from blog.models import BlogPost

# Create your views here.
def registration_view(request):
    """Handles the registration of new accounts"""
    context = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            context['success_message'] = 'Account Creation Successful'
            return redirect('login')
        else:
            context['form'] = form
    else:
        context['form'] = RegistrationForm()
    return render(request, 'account/register.html', context)

@login_required
def logout_view(request):
    """Handles the logging out of users"""
    logout(request)
    return redirect('home_page')
    # return HttpResponse('logged out')


def login_view(request):
    """Handles the logging in of users"""
    context = {}
    if request.user.is_authenticated:
        return redirect('home_page')
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = request.POST.get('email').lower()
            password = request.POST.get('password')

            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('home_page')
    else:
        login_form = LoginForm()
    context['login_form'] = login_form
    return render(request, 'account/login.html', context)
    

@login_required
def update_view(request):
    """Handles the updating of user details"""
    context = {}

    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        update_form = AccountUpdateForm(request.POST, instance=request.user)
        if update_form.is_valid():
            update_form.save()
            context['success_message']='Details successfully updated.'
    else:
        update_form = AccountUpdateForm(instance=request.user)
    
    blog_posts = BlogPost.objects.filter(author=request.user)
    context['blog_posts'] = blog_posts
    context['update_form'] = update_form
    return render(request, 'account/account.html', context)


def must_authenticate_view(request):
    return render(request, 'account/must_authenticate.html')