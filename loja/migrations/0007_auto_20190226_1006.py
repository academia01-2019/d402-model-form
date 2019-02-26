# Generated by Django 2.1.7 on 2019-02-26 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0006_auto_20190226_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='cliente',
            field=models.CharField(choices=[('CN', 'Cliente Novo'), ('CR', 'Cliente Recorrente')], default='CN', max_length=2),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='cartao',
            field=models.IntegerField(),
        ),
    ]
