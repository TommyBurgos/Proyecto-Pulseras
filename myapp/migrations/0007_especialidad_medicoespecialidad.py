# Generated by Django 4.2.11 on 2024-04-15 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_enfermedades_tipoalerta_alerta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MedicoEspecialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('idEspecialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.especialidad')),
                ('idMedico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.medico')),
            ],
        ),
    ]
