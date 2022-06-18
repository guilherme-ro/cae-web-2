from django.urls import path

from . import views

app_name = 'escolas'
urlpatterns = [
    path('', views.index, name='escolas'),
    path('<int:escola_id>', views.escola, name='escola'),
    # path('search', views.search, name='search')
]