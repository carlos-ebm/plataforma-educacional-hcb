# Generated by Django 3.1.7 on 2021-04-10 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_activity_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='namelink',
            field=models.CharField(default=1, max_length=50, verbose_name='Nombre de enlace'),
            preserve_default=False,
        ),
    ]
