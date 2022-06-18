from django.shortcuts import render
from django.http import HttpResponse

from relatorios.models import Relatorio
from escolas.models import Escola

def index(request):
    relatorios = Relatorio.objects.all().filter(is_published=True)[:3]
    escolas = Escola.objects.all()

    context = {
        'relatorios': relatorios,
        'escolas': escolas
    }
    return render(request, 'paginas/index.html', context)

def search(request):
    queryset_list = Relatorio.objects.all().order_by('-data_relatorio').filter(is_published=True)
    escolas = Escola.objects.all()

    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(titulo__icontains=keywords)[:3]

    # escola
    if 'escola' in request.GET:
        escola = request.GET['escola']
        if escola:
            queryset_list = queryset_list.filter(escola__exact=escola)[:3]

    context = {
        'relatorios': queryset_list,
        'escolas': escolas
    }
    return render(request, 'paginas/search.html', context)

def about(request):
    return render(request, 'paginas/about.html')