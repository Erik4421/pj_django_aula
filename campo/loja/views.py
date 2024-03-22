from django.shortcuts import render

# Create your views here.

def pesquisar(request):
    return render(request, 'loja/pesquisar.html')