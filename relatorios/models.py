from django.db import models
from datetime import datetime
from escolas.models import Escola
from django.contrib.auth.models import User

class ImpressaoRelatorio(models.Model):
    mRelatorioTitulo = models.CharField(max_length=50)
    mRelatorioSubTitulo = models.CharField(max_length=50)
    mRelatorioEndereco = models.CharField(max_length=50)
    mRelatorioBairro = models.CharField(max_length=50)
    mRelatorioCEP = models.CharField(max_length=8)
    mRelatorioTelefone = models.CharField(max_length=10)
    mRelatorioRamal = models.CharField(max_length=6)
    mRelatorioCidade = models.CharField(max_length=30)
    mRelatorioEmail = models.CharField(max_length=50)
    mRelatorioFoto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    mRelatorioCopia = models.BooleanField()
    def __str__(self):
        return self.mRelatorioTitulo

class Relatorio(models.Model):
    escola = models.ForeignKey(Escola, on_delete=models.DO_NOTHING)
    cae_rep = models.CharField(max_length=200)
    escola_rep = models.CharField(max_length=200)
    escola_direcao = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    data_relatorio = models.DateField(default=datetime.now)
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    user_id = models.IntegerField()
    foto_principal = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    foto_1 = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    foto_2 = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    foto_3 = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    foto_4 = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    foto_5 = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    foto_6 = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    def __str__(self):
        return self.titulo

class QSection(models.Model):
    section_name = models.CharField(max_length=30)
    def __str__(self):
        return self.section_name

class Question(models.Model):
    qsection = models.ForeignKey(QSection, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    orientacoes = models.CharField(max_length=200, blank=True)
    vencimento = models.DateField(default=datetime.now, blank=True)
    comentario = models.CharField(max_length=30, blank=True)
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=30)
    def __str__(self):
        return self.choice_text

class RelQuestion(models.Model):
    rel_id = models.IntegerField()
    question_id = models.IntegerField()
    choice = models.CharField(max_length=30)
    orientacoes = models.CharField(max_length=200)
    vencimento = models.DateField(default=datetime.now, blank=True)
    comentario = models.CharField(max_length=200)

