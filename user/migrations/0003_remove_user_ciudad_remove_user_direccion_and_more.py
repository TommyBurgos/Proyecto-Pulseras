# Generated by Django 4.2.11 on 2024-04-01 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_estadocivil_genero_rol_user_ciudad_user_direccion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='ciudad',
        ),
        migrations.RemoveField(
            model_name='user',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='user',
            name='estadoCivil',
        ),
        migrations.RemoveField(
            model_name='user',
            name='genero',
        ),
        migrations.RemoveField(
            model_name='user',
            name='nacimiento',
        ),
        migrations.RemoveField(
            model_name='user',
            name='rol',
        ),
    ]
