# Generated by Django 4.2 on 2023-04-28 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
                ('cpf', models.TextField(max_length=16)),
                ('email', models.TextField(max_length=100)),
                ('endereco', models.TextField(max_length=255)),
                ('fone', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id_produto', models.AutoField(primary_key=True, serialize=False)),
                ('cod_produto', models.TextField(max_length=255)),
                ('nome', models.TextField(max_length=255)),
                ('descricao', models.TextField(max_length=255)),
                ('preco', models.TextField(max_length=255)),
                ('categoria', models.TextField(max_length=255)),
                ('quantidade', models.TextField(max_length=255)),
                ('fornecedor', models.TextField(max_length=255)),
                ('validade', models.DateTimeField()),
            ],
        ),
    ]
