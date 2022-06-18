from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from escolas.models import Escola
from .models import Relatorio, Question, Choice, QSection, RelQuestion

from django.shortcuts import render
import os
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa

def index(request):
    relatorios = Relatorio.objects.all()
    questions = Question.objects.all()
    choices = Choice.objects.all()
    context = {
        'relatorios': relatorios,
        'questions': questions,
        'choices': choices
    }
    
    return render(request, 'relatorios/relatorios.html', context)

def relatorio(request, relatorio_id):
    relatorio = get_object_or_404(Relatorio, pk=relatorio_id)
    qsections = QSection.objects.all()
    questions = Question.objects.all()
    choices = Choice.objects.all()
    rel_questions = RelQuestion.objects.all()

    context = {
        'relatorio': relatorio,
        'relatorio_id': relatorio_id,
        'qsections': qsections,
        'questions': questions,
        'choices': choices,
        'rel_questions': rel_questions
    }

    return render(request, 'relatorios/relatorio.html', context)

def relatorio_pdf(request, relatorio_id):
    relatorio = get_object_or_404(Relatorio, pk=relatorio_id)
    qsections = QSection.objects.all()
    questions = Question.objects.all()
    choices = Choice.objects.all()
    rel_questions = RelQuestion.objects.all()

    rel_name = relatorio.titulo
    template_path = 'relatorios/template_pdf.html'
    context = {
        'relatorio': relatorio,
        'relatorio_id': relatorio_id,
        'qsections': qsections,
        'questions': questions,
        'choices': choices,
        'rel_questions': rel_questions
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename= "' + rel_name + '.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
        html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('erro')
    return response

def cadastro(request):

    rel = Escola.objects.all()
    qsections = QSection.objects.all()
    questions = Question.objects.all()
    choices = Choice.objects.all()


    context = {
        'escolas': rel,
        'qsections': qsections,
        'questions': questions,
        'choices': choices
    }

    if request.method == 'POST':
        escola_id = request.POST['lista_escolas']
        cae_rep = request.POST['cae_rep']
        escola_rep = request.POST['escola_rep']
        escola_direcao = request.POST['escola_direcao']
        titulo = request.POST['titulo']
        data_relatorio = request.POST['data_relatorio']
        hora_inicio = request.POST['hora_inicio']
        hora_fim = request.POST['hora_fim']
        user_id = request.POST['user_id']

        # criar variaveis para cadastrar as respostas das perguntas

        #  Check if user has made inquiry already
        if request.user.is_authenticated:

            has_registered = Relatorio.objects.all().filter(titulo=titulo, data_relatorio=data_relatorio, is_published=True)
            if has_registered:
                messages.error(request, 'Esse relatório já foi cadastrado')
                return redirect('relatorios')

        relatorio = Relatorio(user_id=user_id, escola_id=escola_id, cae_rep=cae_rep, escola_rep=escola_rep, escola_direcao=escola_direcao, titulo=titulo, is_published=True, 
        data_relatorio=data_relatorio, hora_inicio=hora_inicio, hora_fim=hora_fim)

        relatorio.save()

        rel_id = Relatorio.objects.latest('id')

        for question in questions: 
            choice = None
            orientacoes = None
            vencimento = None
            comentario = None
            question_id = None
            report_questions = None

            if (question.qsection.section_name.lower() == 'Documentação'.lower()):

                question_id = question.id
                choice = request.POST['choice-'+str(question.id)]
                orientacoes = request.POST['orientacoes-'+str(question.id)]
                vencimento = request.POST['vencimento-'+str(question.id)]
                comentario = request.POST['comentario-'+str(question.id)]
         
                report_questions = RelQuestion(rel_id=rel_id.id, question_id=question_id, choice=choice, orientacoes=orientacoes, vencimento=vencimento, comentario=comentario)
                report_questions.save()

            if (question.qsection.section_name.lower() == 'Cozinha'.lower()):
                
                question_id = question.id
                choice = request.POST['choice-'+str(question.id)]
                orientacoes = request.POST['orientacoes-'+str(question.id)]
                vencimento = request.POST['vencimento-'+str(question.id)]
                comentario = request.POST['comentario-'+str(question.id)]
         
                report_questions = RelQuestion(rel_id=rel_id.id, question_id=question_id, choice=choice, orientacoes=orientacoes, vencimento=vencimento, comentario=comentario)
                report_questions.save()

            if (question.qsection.section_name.lower() == 'Despensa'.lower()):
                question_id = question.id
                for choice in choices:

                    if (choice.question == question):
                        choice = request.POST['choice-'+str(question.id)]
                        orientacoes = request.POST['orientacoes-'+str(question.id)]
                        vencimento = request.POST['vencimento-'+str(question.id)]
                        comentario = request.POST['comentario-'+str(question.id)]
            
         
                report_questions = RelQuestion(rel_id=rel_id.id, question_id=question_id, choice=choice, orientacoes=orientacoes, vencimento=vencimento, comentario=comentario)
                report_questions.save()
    
            if (question.qsection.section_name.lower() == 'Alimentação'.lower()):
                question_id = question.id
                for choice in choices:

                    if (choice.question == question):
                        choice = request.POST['choice-'+str(choice.question.id)]
                        orientacoes = request.POST['orientacoes-'+str(question.id)]
                        vencimento = request.POST['vencimento-'+str(question.id)]
                        comentario = request.POST['comentario-'+str(question.id)]
            
         
                report_questions = RelQuestion(rel_id=rel_id.id, question_id=question_id, choice=choice, orientacoes=orientacoes, vencimento=vencimento, comentario=comentario)
                report_questions.save()

            if (question.qsection.section_name.lower() == 'Armazenamento'.lower()):
                question_id = question.id
                for choice in choices:

                    if (choice.question == question):
                        choice = request.POST['choice-'+str(choice.question.id)]
                        orientacoes = request.POST['orientacoes-'+str(question.id)]
                        vencimento = request.POST['vencimento-'+str(question.id)]
                        comentario = request.POST['comentario-'+str(question.id)]
            
         
                report_questions = RelQuestion(rel_id=rel_id.id, question_id=question_id, choice=choice, orientacoes=orientacoes, vencimento=vencimento, comentario=comentario)
                report_questions.save()

            if (question.qsection.section_name.lower() == 'Sobre os Atendentes'.lower()):
                question_id = question.id
                for choice in choices:

                    if (choice.question == question):
                        choice = request.POST['choice-'+str(choice.question.id)]
                        orientacoes = request.POST['orientacoes-'+str(question.id)]
                        vencimento = request.POST['vencimento-'+str(question.id)]
                        comentario = request.POST['comentario-'+str(question.id)]
            
         
                report_questions = RelQuestion(rel_id=rel_id.id, question_id=question_id, choice=choice, orientacoes=orientacoes, vencimento=vencimento, comentario=comentario)
                report_questions.save()

            if (question.qsection.section_name.lower() == 'Informações dos Atendentes'.lower()):
                question_id = question.id
                for choice in choices:

                    if (choice.question == question):
                        choice = request.POST['choice-'+str(choice.question.id)]
                        orientacoes = request.POST['orientacoes-'+str(question.id)]
                        vencimento = request.POST['vencimento-'+str(question.id)]
                        comentario = request.POST['comentario-'+str(question.id)]
            
         
                report_questions = RelQuestion(rel_id=rel_id.id, question_id=question_id, choice=choice, orientacoes=orientacoes, vencimento=vencimento, comentario=comentario)
                report_questions.save()
   
        messages.success(request, 'Seu cadastro foi realizado com sucesso')
        return redirect('/relatorios/', context)
    else:
        return render(request, 'relatorios/cadastro.html', context)

def search(request):
    queryset_list = Relatorio.objects.all().order_by('-data_relatorio').filter(is_published=True)

    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(titulo__icontains=keywords)

    # escola
    if 'escola' in request.GET:
        escola = request.GET['escola']
        if escola:
            queryset_list = queryset_list.filter(escola__nome__exact=escola)

    context = {
        'relatorios': queryset_list
    }
    return render(request, 'relatorios/search.html', context)