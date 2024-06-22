from django import forms 
from django.shortcuts import render
from django.http import HttpResponse
from .forms import FormLinks
from .models import Links
from django.shortcuts import redirect

def home(request):
    form = FormLinks()
    status = request.GET.get('status')
    return render(request, 'home.html', {'form': form, 'status': status})

def valida_link(request):
    form = FormLinks(request.POST)
    #Permite não criar o mesmo link, cada link é unico
    link_encurtado = form.data['link_encurtado']
    links = Links.objects.filter(link_encurtado = link_encurtado)
    if len(links) > 0:
        return redirect("/?status=1")
    
    if form.is_valid(): #Verifica se os dados são validos e permite não manipular outros tipos de dados sem ser o link
        try:
            form.save()
            return HttpResponse(f"Seu link foi criado com sucesso e é: http://127.0.0.1:8000/{form.data['link_encurtado']}")
        except:
            return HttpResponse("erro interno do sistema")

def redirecionar(request, link):
    links = Links.objects.filter(link_encurtado = link)
    if len(links) == 0: #Significa que se o link não foi criado, o usuario será redirecionado para uma página com o seu link pronto
        return redirect('/')
    
    
    return redirect(links[0].link_redirecionado)