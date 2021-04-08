# Generated by Django 3.1.7 on 2021-04-08 09:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import groomeet_backend.models
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Banda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Instrumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('familia', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Musico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaNacimiento', models.DateField(null=True, verbose_name='Fecha de nacimiento')),
                ('isGold', models.BooleanField(default=False)),
                ('isSilver', models.BooleanField(default=False)),
                ('generos', models.ManyToManyField(to='groomeet_backend.Genero')),
                ('instrumentos', models.ManyToManyField(to='groomeet_backend.Instrumento')),
                ('likesRecibidos', models.ManyToManyField(blank=True, related_name='likesDados', to=settings.AUTH_USER_MODEL)),
                ('likesRecibidosBanda', models.ManyToManyField(blank=True, related_name='likesDadosMusico', to='groomeet_backend.Banda')),
                ('noLikesRecibidos', models.ManyToManyField(blank=True, related_name='noLikesDados', to=settings.AUTH_USER_MODEL)),
                ('noLikesRecibidosBanda', models.ManyToManyField(blank=True, related_name='noLikesDadosMusico', to='groomeet_backend.Banda')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MiembroNoRegistrado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
                ('descripcion', models.CharField(max_length=500)),
                ('banda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='miembrosNoRegistrados', to='groomeet_backend.banda')),
                ('instrumentos', models.ManyToManyField(blank=True, to='groomeet_backend.Instrumento')),
            ],
        ),
        migrations.CreateModel(
            name='MiembroDe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaUnion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de unión')),
                ('banda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groomeet_backend.banda')),
                ('musico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groomeet_backend.musico')),
            ],
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('cuerpo', models.TextField(verbose_name='Cuerpo del mensaje')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajes', to='groomeet_backend.musico', verbose_name='Autor')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajes', to='groomeet_backend.chat', verbose_name='Chat')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Invitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('estado', models.CharField(choices=[(groomeet_backend.models.EstadoInvitacion['Rechazada'], 'Rechazada'), (groomeet_backend.models.EstadoInvitacion['Pendiente'], 'Pendiente'), (groomeet_backend.models.EstadoInvitacion['Aceptada'], 'Aceptada')], max_length=40)),
                ('banda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groomeet_backend.banda')),
                ('emisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitacionesEnviadas', to='groomeet_backend.musico')),
                ('receptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitacionesRecibidas', to='groomeet_backend.musico')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=100)),
                ('codigo_estado', models.CharField(max_length=100)),
                ('total_de_la_compra', models.DecimalField(decimal_places=2, max_digits=5)),
                ('nombre_cliente', models.CharField(max_length=100)),
                ('apellido_cliente', models.CharField(max_length=100)),
                ('correo_cliente', models.EmailField(max_length=100)),
                ('direccion_cliente', models.CharField(max_length=100)),
                ('fecha_compra', models.DateField(default=datetime.date.today)),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='groomeet_backend.producto')),
                ('usuario', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='chat',
            name='participante1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats1', to='groomeet_backend.musico', verbose_name='Participante 1'),
        ),
        migrations.AddField(
            model_name='chat',
            name='participante2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats2', to='groomeet_backend.musico', verbose_name='Participante 2'),
        ),
        migrations.AddField(
            model_name='banda',
            name='administrador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='bandasAdministradas', to='groomeet_backend.musico'),
        ),
        migrations.AddField(
            model_name='banda',
            name='generos',
            field=models.ManyToManyField(blank=True, to='groomeet_backend.Genero'),
        ),
        migrations.AddField(
            model_name='banda',
            name='instrumentos',
            field=models.ManyToManyField(blank=True, to='groomeet_backend.Instrumento'),
        ),
        migrations.AddField(
            model_name='banda',
            name='likesRecibidosBanda',
            field=models.ManyToManyField(blank=True, related_name='likesDadosBanda', to='groomeet_backend.Banda'),
        ),
        migrations.AddField(
            model_name='banda',
            name='likesRecibidosMusico',
            field=models.ManyToManyField(blank=True, related_name='likesDadosBanda', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='banda',
            name='miembros',
            field=models.ManyToManyField(blank=True, through='groomeet_backend.MiembroDe', to='groomeet_backend.Musico'),
        ),
        migrations.AddField(
            model_name='banda',
            name='noLikesRecibidosBanda',
            field=models.ManyToManyField(blank=True, related_name='noLikesDadosBanda', to='groomeet_backend.Banda'),
        ),
        migrations.AddField(
            model_name='banda',
            name='noLikesRecibidosMusico',
            field=models.ManyToManyField(blank=True, related_name='noLikesDadosBanda', to=settings.AUTH_USER_MODEL),
        ),
    ]
