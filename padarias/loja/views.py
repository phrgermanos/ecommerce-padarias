from django.shortcuts import render

def loja(request):
     context = {}
     return render(request, 'loja/loja.html', context)

def carrinho(request):
     context = {}
     return render(request, 'loja/carrinho.html', context)

def escapar(request):
     context = {}
     return render(request, 'loja/escapar.html', context)
