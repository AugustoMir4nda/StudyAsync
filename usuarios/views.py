from django.shortcuts import render, redirect #prepara um html para ser exibido por um cliente - renderiza
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth


def cadastro(request):
    # lógica para utilização dos métodos para extrair os dados digitados pelo cliente - extração e validação
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get("confirmar_senha")
        
        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR,'Senha não coincide com Confirmação de Senha')
            return redirect('/usuarios/cadastro')

        #este método retorna username para ser utilizado como parâmetro na condição após a sua criação
        user = User.objects.filter(username = username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Usuário já existe com mesmo nome')
            return redirect('/usuarios/cadastro')

        #Como o acesso ao BD pode dar erros normalmente, utilizamos o try/except para podermos redirecionar o erro para as páginas do site
        try:
        # importamos o método User do django.contrib para poder processar os dados digitados pelos usuários e insri-los nas tabelas do sqlite
            User.objects.create_user(
                # Criamos os usuários a partir do nome e da senha digitada, logo atribui-se os valores ao que foi inputado.
                username = username,
                password = senha
            )
            return redirect('/usuarios/logar')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do servidor')
            return redirect('/usuarios/cadastro')

def logar(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        #Realizando autenticação - Verificando se existe o usuario digitado
        user = auth.authenticate(request, username = username, password = senha)

        if user:
            auth.login(request, user)
            messages.add_message(request, constants.SUCCESS, 'Logado!')
            return redirect('/flashcard/novo_flashcard/')
        else:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos')
            return redirect('/usuarios/logar/')

def logout(request):
    auth.logout(request)
    return redirect('/usuarios/logar')