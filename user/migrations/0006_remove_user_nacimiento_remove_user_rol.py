# Generated by Django 4.2.11 on 2024-04-01 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_user_nacimiento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='nacimiento',
        ),
        migrations.RemoveField(
            model_name='user',
            name='rol',
        ),
    ]
