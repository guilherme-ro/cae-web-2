from django.db import models

class Escola(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    diretor = models.CharField(max_length=200)
    alunos_atendidos_dia = models.CharField(max_length=200)
    total_alunos_matric = models.CharField(max_length=200)  
    p_manha = models.BooleanField('Período: Manhã', default=False)
    p_tarde = models.BooleanField('Período: Tarde', default=False)
    p_noite = models.BooleanField('Período: Noite', default=False)
    p_integral = models.BooleanField('Período: Integral', default=False)
    def __str__(self):
        return self.nome

