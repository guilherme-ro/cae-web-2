from django.shortcuts import get_object_or_404, render
from escolas.models import Escola

def index(request):
    escolas = Escola.objects.all()
    context = {
        'escolas': escolas
    }

    return render(request, 'escolas/escolas.html', context)

def escola(request, escola_id):
    escola = get_object_or_404(Escola, pk=escola_id)
    context = {
        'escola': escola,
    }

    return render(request, 'escolas/escola.html', context)

# def search(request):
#     return render(request, 'escolas/search.html')