# Generated by Django 3.0.4 on 2020-04-17 02:45

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('imagem', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/home/guilherme/Documentos/fuxiqueira-webapp/api/upload'), upload_to='')),
                ('descricao', models.TextField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('projeto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questoes.Projeto')),
            ],
        ),
        migrations.CreateModel(
            name='Alternativa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(max_length=100)),
                ('questao_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alternativas', to='questoes.Questao')),
            ],
        ),
    ]
