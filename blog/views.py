from django.shortcuts import render
from blog.data import posts

def blog(request):

    context = {
            'posts' : posts
        }

    return render(
        request,
        'blog/index.html',
        context
    )

def post(request, post_id):
    found_post = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break


    context = {
            'post' : found_post,
            'title' : found_post['title'] + ' - '
        }

    return render(
        request,
        'blog/post.html',
        context
    )

def exemplo(request):
    print('exemplo')

    context = {
            'text' : 'Olá exemplo',
            'title' : 'Exemplo - '
        }

    return render(
        request,
        'blog/exemplo.html',
        context
    )
