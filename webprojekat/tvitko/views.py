from django.shortcuts import render
from .models import Tweet
from .models import Hashtag
from .tc import podaci

# Create your views here.
# views u djangu je isto sto i controller u MVC-u

def index(request):
    return render(request, 'index.html')


def tabela(request):

    rez = Tweet.objects.all()  # u sql select * form Tweet
    ctx = {'n': len(rez), 'tabela': rez}
    return render(request, 'tabela.html', ctx)

def search(request):
    tagovi = request.POST['tagovi']
    brojtvitova = request.POST['brojtvitova']
    tvitovi = podaci(tagovi, brojtvitova)
    ctx = {'tabela': tvitovi}
    return render(request, 'tabela.html', ctx)