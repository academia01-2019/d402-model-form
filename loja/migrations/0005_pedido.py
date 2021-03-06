# Generated by Django 2.1.7 on 2019-02-26 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0004_produto_disponivel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('endereco', models.CharField(max_length=240)),
                ('observacao', models.TextField(blank=True, null=True)),
                ('cartao', models.IntegerField()),
            ],
        ),
    ]
