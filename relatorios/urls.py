from django.urls import path
from . import views

app_name = 'relatorios'
urlpatterns = [
    path('', views.index, name='relatorios'),
    path('<int:relatorio_id>', views.relatorio, name='relatorio'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('search', views.search, name='search'),
    path('<int:relatorio_id>/relatorio_pdf', views.relatorio_pdf, name='relatorio_pdf')
]