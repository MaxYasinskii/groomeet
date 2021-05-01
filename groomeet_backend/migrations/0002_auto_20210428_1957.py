# Generated by Django 3.1.7 on 2021-04-28 17:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groomeet_backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='musico',
            name='contadorReferidos',
            field=models.IntegerField(default=0, verbose_name='Referidos'),
        ),
        migrations.AddField(
            model_name='musico',
            name='invitadoPor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='referidos', to='groomeet_backend.musico'),
        ),
        migrations.AlterField(
            model_name='banda',
            name='miembros',
            field=models.ManyToManyField(blank=True, through='groomeet_backend.MiembroDe', to='groomeet_backend.Musico', verbose_name='Miembros'),
        ),
        migrations.CreateModel(
            name='Bonificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaBonificacion', models.DateField(default=datetime.date.today)),
                ('musico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bonificaciones', to='groomeet_backend.musico')),
            ],
        ),
    ]
