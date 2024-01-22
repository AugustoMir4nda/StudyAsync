from django.urls import path
from . import views
#Criei este arquivo para cadastrar as novas urls, além do file padrão adm que vem no arquivo, são as Urls que vão rodar no servidor
urlpatterns = [
    path('cadastro/', views.cadastro, name ="cadastro"), #rota e função com nome que é chamada
    path('logar/', views.logar, name ='login'),
    path('logout', views.logout, name = 'logout')
]