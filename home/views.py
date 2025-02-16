from django.shortcuts import render

def home(request):
    print('home')

    context = {
            'text' : 'Estamos na HOME'
        }
    
    return render(
        request,
        'home/index.html',
        context
    )
