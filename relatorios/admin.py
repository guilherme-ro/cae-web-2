from django.contrib import admin
from .models import Relatorio, QSection, Question, Choice, ImpressaoRelatorio, RelQuestion
from escolas.models import Escola


admin.site.site_header = "Sistema Visitas - Administração"
admin.site.site_title = "Área do Administrador"
admin.site.index_title = "Bem vindo à Área do Admin"



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['qsection', 'question_text']}),]
    inlines = [ChoiceInline]

class RelatorioAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['escola', 'cae_rep', 'escola_rep', 'escola_direcao', 'titulo', 'is_published', 'data_relatorio', 'hora_inicio', 'hora_fim', 'foto_principal' ]}),]

class RelQuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['rel_id', 'question_id', 'choice', 'orientacoes', 'vencimento', 'comentario' ]}),]
    

# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Relatorio, RelatorioAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Escola)
admin.site.register(QSection)
admin.site.register(ImpressaoRelatorio)
admin.site.register(RelQuestion)

