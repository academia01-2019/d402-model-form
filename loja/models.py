from django.db import models

# Create your models here.


class Produto(models.Model):
    nome = models.CharField(max_length=120)
    preco = models.DecimalField(decimal_places=2, max_digits=10000, default=0)
    descricao = models.TextField(blank=True, null=True)
    # cor = models.CharField(max_length=50)
    # data_de_fabricacao = models.DateField(auto_now=True)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    # CLIENTE_NOVO = 'CN'
    # CLIENTE_RECORRENTE = 'CR'
    # CLIENTE_ESTADO = [
    #     (CLIENTE_NOVO, 'Cliente Novo'),
    #     (CLIENTE_RECORRENTE, 'Cliente Recorrente')
    # ]

    PAGAMENTO_A_VISTA = 'AV'
    PAGAMENTO_PARCELADO_2 = 'P2'
    PAGAMENTO_PARCELADO_3 = 'P3'
    PAGAMENTO_PARCELADO_4 = 'P4'
    METODO_PAGAMENTO = [
        (PAGAMENTO_A_VISTA, 'Pagamento à Vista'),
        (PAGAMENTO_PARCELADO_2, 'Parcelado em 2x'),
        (PAGAMENTO_PARCELADO_3, 'Parcelado em 3x'),
        (PAGAMENTO_PARCELADO_4, 'Parcelado em 4x'),
    ]

    nome = models.CharField(max_length=120)
    email = models.EmailField()
    endereco = models.CharField(max_length=240)
    observacao = models.TextField(blank=True, null=True)
    cartao = models.IntegerField()
    # cliente = models.CharField(max_length=2, choices=CLIENTE_ESTADO, default=CLIENTE_NOVO)
    pagamento = models.CharField(max_length=2, choices=METODO_PAGAMENTO, default=PAGAMENTO_A_VISTA)
