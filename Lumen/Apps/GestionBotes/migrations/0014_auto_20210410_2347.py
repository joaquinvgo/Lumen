# Generated by Django 3.0.5 on 2021-04-10 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionBotes', '0013_auto_20201004_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paises',
            name='Nombre',
            field=models.CharField(max_length=50),
        ),
    ]
