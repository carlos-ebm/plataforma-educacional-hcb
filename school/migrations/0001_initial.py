# Generated by Django 3.1.7 on 2021-03-18 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('instruction', models.TextField(verbose_name='Instrucciones')),
                ('document', models.FileField(upload_to='Documentos', verbose_name='Documento')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
            ],
            options={
                'verbose_name': 'Actividad',
                'verbose_name_plural': 'Actividades',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Activity_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.activity')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.profile')),
            ],
            options={
                'verbose_name': 'Actividad de perfil',
                'verbose_name_plural': 'Actividades de perfiles',
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='activity',
            name='activityToProfile',
            field=models.ManyToManyField(through='school.Activity_profile', to='registration.Profile', verbose_name='Actividades de perfiles'),
        ),
    ]
