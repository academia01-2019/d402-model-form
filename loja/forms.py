from django import forms
from loja.models import Pedido

class PedidoCriarForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            'nome',
            'email',
            'endereco',
            'observacao',
            'cartao',
            'pagamento'
        ]
