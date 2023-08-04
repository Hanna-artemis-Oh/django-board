import json
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment


def index(request):
    post_list = Post.objects.all().order_by('-created_at')
    context = {'post_list': post_list}
    return render(request, 'boards/index.html', context)


def write(request):
    return render(request, 'boards/write.html')


def write_success(request):
    author = request.POST['author']
    title = request.POST['title']
    content = request.POST['content']
    saved_post = Post(author=author, title=title, content=content)
    saved_post.save()
    return redirect('boards:index')


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
    try:
        json_object = json.loads(request.body)
        like = json_object.get('like')
        post = get_object_or_404(Post, pk=post_id)
        if like == 1:
            post.like += 1
            post.save()
    except:
        print('broken like button')

    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'boards/detail.html', context)


def edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    try:
        context = {'post': post}
        author = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        post.author = author
        post.title = title
        post.content = content
        post.save()
        return redirect('boards:index')
    except:
        print('수정 실패')
    return render(request, 'boards/edit.html', context)


def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('boards:index')
