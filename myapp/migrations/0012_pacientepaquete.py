# Generated by Django 4.2.11 on 2024-04-15 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_detalleservicio_rename_descripcion_servicio_umbral_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PacientePaquete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField()),
                ('precio', models.FloatField()),
                ('estado', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.estado')),
                ('idDispositivo', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.dispositivo')),
                ('idPaciente', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.paciente')),
                ('idPaquete', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.paquete')),
            ],
        ),
    ]
