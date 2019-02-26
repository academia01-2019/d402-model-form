from django.shortcuts import render
from loja.forms import PedidoCriarForm

# Create your views here.

def criar_pedido_view(request):
    formulario = PedidoCriarForm(request.POST or None)
    
    if formulario.is_valid():
        formulario.save()
        formulario = PedidoCriarForm()

    contexto = {
        'form': formulario
    }

    return render(request, 'formulario-pedido.html', contexto)
