from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm, CategoryForm, TagForm, CommentForm


# Create your views here.
def http_responce(request):
    return HttpResponse('Hello, World!')


def first_render(request):
    return render(request, 'first_render.html')


def post_list_api_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'posts/post_list.html', {'posts': posts})


def post_detail_api_view(request, post_id):
    if request.method == 'GET':
        post = get_object_or_404(Post, id=post_id)
        return render(request, 'posts/post_detail.html', {'post': post})


@login_required(login_url='/user/login/')
def create_post_view(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'posts/create_post.html', {'form': form})
    elif request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'posts/create_post.html', {'form': form})
        post = form.save()
        post.user = request.user
        post.save()
        return redirect('/post/post_list/')


@login_required(login_url='/user/login/')
def create_category_view(request):
    if request.method == 'GET':
        form = CategoryForm()
        return render(request, 'posts/create_category.html', {'form': form})
    elif request.method == 'POST':
        form = CategoryForm(request.POST)
        if not form.is_valid():
            return render(request, 'posts/create_category.html', {'form': form})
        form.save()
        return redirect('/post/post_list/')


@login_required(login_url='/user/login/')
def create_tag_view(request):
    if request.method == 'GET':
        form = TagForm()
        return render(request, 'posts/create_tag.html', {'form': form})
    elif request.method == 'POST':
        form = TagForm(request.POST)
        if not form.is_valid():
            return render(request, 'posts/create_tag.html', {'form': form})
        form.save()
        return redirect('/post/post_list/')


@login_required(login_url='/user/login/')
def create_comment_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Fetch the post
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post  # Link the comment to the post object
            comment.user = request.user  # Optionally associate with the logged-in user
            comment.save()
            return redirect('create_review', post_id=post_id)
    else:
        form = CommentForm()

    return render(request, 'posts/post_detail.html', {'post': post, 'form': form})


