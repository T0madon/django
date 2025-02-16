from django.shortcuts import render

def blog(request):
    print('blog')

    context = {
            'text' : 'Olá blog',
            'title' : 'Blog - '
        }

    return render(
        request,
        'blog/index.html',
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
