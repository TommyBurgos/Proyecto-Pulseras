# Generated by Django 4.2.11 on 2024-04-01 06:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_remove_user_ciudad_remove_user_direccion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ciudad',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='direccion',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='user',
            name='estadoCivil',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='user.estadocivil'),
        ),
        migrations.AddField(
            model_name='user',
            name='genero',
            field=models.ForeignKey(blank=True, default=3, on_delete=django.db.models.deletion.CASCADE, to='user.genero'),
        ),
        migrations.AddField(
            model_name='user',
            name='nacimiento',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='user',
            name='rol',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.rol'),
        ),
    ]