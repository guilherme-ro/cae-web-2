# Generated by Django 3.2.7 on 2021-11-05 21:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relatorios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImpressaoRelatorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mRelatorioTitulo', models.CharField(max_length=50)),
                ('mRelatorioSubTitulo', models.CharField(max_length=50)),
                ('mRelatorioEndereco', models.CharField(max_length=50)),
                ('mRelatorioBairro', models.CharField(max_length=50)),
                ('mRelatorioCEP', models.CharField(max_length=8)),
                ('mRelatorioTelefone', models.CharField(max_length=10)),
                ('mRelatorioRamal', models.CharField(max_length=6)),
                ('mRelatorioCidade', models.CharField(max_length=30)),
                ('mRelatorioEmail', models.CharField(max_length=50)),
                ('mRelatorioFoto', models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d/')),
                ('mRelatorioCopia', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='comentario',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='question',
            name='vencimento',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='question',
            name='orientacoes',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.CreateModel(
            name='QSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=30)),
                ('relatorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relatorios.relatorio')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='qsection',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='relatorios.qsection'),
            preserve_default=False,
        ),
    ]
