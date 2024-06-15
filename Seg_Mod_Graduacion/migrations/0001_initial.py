# Generated by Django 5.0.6 on 2024-06-12 02:23

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=100)),
                ('plan', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Modalidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TutorExterno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Complementario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio_egreso', models.IntegerField()),
                ('periodo_egreso', models.CharField(max_length=50)),
                ('numero_acta', models.CharField(max_length=50)),
                ('nota', models.FloatField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InvCientifica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('resumen', models.TextField(max_length=500)),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('pdf_inv_c', models.FileField(upload_to='documentos/investigacion/')),
                ('estado', models.CharField(choices=[('Aprobado', 'Aprobado'), ('Pendiente', 'Pendiente'), ('Rechazado', 'Rechazado')], default='Pendiente', max_length=10)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('pdf_perfil', models.FileField(upload_to='documentos/perfil/')),
                ('estado', models.CharField(choices=[('Aprobado', 'Aprobado'), ('Pendiente', 'Pendiente'), ('Rechazado', 'Rechazado')], default='Pendiente', max_length=10)),
                ('modalidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Seg_Mod_Graduacion.modalidad')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProyectoFinal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('resumen', models.TextField(max_length=500)),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('pdf_proyecto_final', models.FileField(upload_to='documentos/proyecto_final/')),
                ('estado', models.CharField(choices=[('Aprobado', 'Aprobado'), ('Pendiente', 'Pendiente'), ('Rechazado', 'Rechazado')], default='Pendiente', max_length=10)),
                ('modalidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Seg_Mod_Graduacion.modalidad')),
                ('tribunales', models.ManyToManyField(blank=True, limit_choices_to={'groups__name': 'Docentes'}, related_name='tribunales', to=settings.AUTH_USER_MODEL)),
                ('tutor', models.ForeignKey(limit_choices_to={'groups__name': 'Docentes'}, on_delete=django.db.models.deletion.CASCADE, related_name='tutor_final', to=settings.AUTH_USER_MODEL)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tutor_externo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Seg_Mod_Graduacion.tutorexterno')),
            ],
        ),
    ]