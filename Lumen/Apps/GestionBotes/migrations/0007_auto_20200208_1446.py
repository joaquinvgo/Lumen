# Generated by Django 3.0.2 on 2020-02-08 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GestionBotes', '0006_auto_20200127_2034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fotos',
            name='UbicacionLocal',
        ),
        migrations.RemoveField(
            model_name='fotos',
            name='Url',
        ),
    ]
