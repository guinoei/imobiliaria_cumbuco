# Generated by Django 5.0.1 on 2024-05-03 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imobapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='propriedade',
            name='codigo',
            field=models.CharField(blank=True, max_length=6, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='propriedade',
            name='finalidade',
            field=models.CharField(choices=[('Venda', 'Venda'), ('Aluguel', 'Aluguel')], max_length=30),
        ),
    ]
