from django.shortcuts import render, get_object_or_404

from .models import Post


def index(request):
    author = request.POST['author']
    title = request.POST['title']
    content = request.POST['content']
    saved_post = Post(author=author, title=title, content=content)
    saved_post.save()
    post_list = Post.objects.all().order_by('-created_at')
    context = {'post_list': post_list}
    return render(request, 'boards/index.html', context)


def write(request):
    return render(request, 'boards/write.html')


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comment_set.all()
    context = {'post': post,
               'comments': comments}
    return render(request, 'boards/detail.html', context)


def edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'boards/edit.html', context)


def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
