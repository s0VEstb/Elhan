from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from user.forms import RegisterForm, LoginForm
from .models import User, Profile

# Create your views here.


def register_view(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, 'user/register.html',context={'form': form})
    elif request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'user/register.html',context={'form': form})

        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
        )
        Profile.objects.create(
            user=user,
            avatar=form.cleaned_data['avatar'],
            bio=form.cleaned_data['bio'],
            age=form.cleaned_data['age']
        )
        login(request, user)

    return redirect('/post/post_list/')


def login_view(request):
    if request.method == "GET":
        form = LoginForm(request.POST)
        return render(request, 'user/login.html', context={'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST, request.FILES)

        if not form.is_valid():
            return render(request, 'user/login.html', context={'form': form})

        user = authenticate(**form.cleaned_data)  # User object or None
        print(user)

        if not user:
            form.add_error(None, 'Invalid username or password')
            return render(request, 'user/login.html', context={'form': form})

        login(request, user)
        return redirect('/post/post_list/')


@login_required(login_url='/login/')
def profile_view(request):
    posts = request.user.posts.all()
    return render(request, 'user/profile.html', context={'posts': posts})



def logout_view(request):
    logout(request)
    return redirect('/post/post_list/')
