from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Comment


def main_page(request):
    if request.method == 'GET':
        return render(request, 'post/index.html')


def post_view_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        context = {
            'posts': posts
        }
        return render(request, 'post/list.html', context)


def post_detail_view(request, post_id):
    if request.method == 'GET':
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return render(
                request,
                'errors/404.html'
            )

        comments = Comment.objects.all()




        context = {
            'post': post
        }
        return render(request, 'post/detail.html', context)

