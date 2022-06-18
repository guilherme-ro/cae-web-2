
from django.contrib import admin
from django.urls import include, path

app_name = 'sistema_visitas'
urlpatterns = [
    path('', include('paginas.urls')),
    path('relatorios/', include('relatorios.urls')),
    path('escolas/', include('escolas.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
