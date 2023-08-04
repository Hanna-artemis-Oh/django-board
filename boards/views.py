import json

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post, Comment


def index(request):
    # author = request.POST['author']
    # title = request.POST['title']
    # content = request.POST['content']
    # saved_post = Post(author=author, title=title, content=content)
    # saved_post.save()
    post_list = Post.objects.all().order_by('-created_at')
    context = {'post_list': post_list}
    return render(request, 'boards/index.html', context)


def write(request):
    return render(request, 'boards/write.html')


def detail(request, post_id):
    try:
        json_object = json.loads(request.body)
        author = json_object.get('comment-author')
        content = json_object.get('comment-content')
        comment = Comment(author=author, content=content, post_id=post_id)
        comment.save()
        post = get_object_or_404(Post, pk=post_id)
        post.num_comments += 1
        post.save()
    except:
        print('No comment posted')

    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'boards/detail.html', context)


def edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'boards/edit.html', context)


def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('boards:index')
