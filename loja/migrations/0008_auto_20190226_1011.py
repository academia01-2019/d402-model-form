# Generated by Django 2.1.7 on 2019-02-26 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0007_auto_20190226_1006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='cliente',
        ),
        migrations.AddField(
            model_name='pedido',
            name='pagamento',
            field=models.CharField(choices=[('AV', 'Pagamento à Vista'), ('P2', 'Parcelado em 2x'), ('P3', 'Parcelado em 3x'), ('P4', 'Parcelado em 4x')], default='AV', max_length=2),
        ),
    ]