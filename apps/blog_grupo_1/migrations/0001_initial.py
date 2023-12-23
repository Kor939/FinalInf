# Generated by Django 4.2.7 on 2023-12-23 00:06

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, unique=True)),
                ('imagen', models.ImageField(default='static/categoria/post_default.jpg', upload_to='media')),
            ],
            options={
                'ordering': ('titulo',),
            },
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=50)),
                ('asunto', models.CharField(max_length=100)),
                ('mensaje', models.TextField()),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, unique=True)),
                ('url', models.SlugField(max_length=255, unique=True)),
                ('resumen', ckeditor.fields.RichTextField()),
                ('contenido', ckeditor.fields.RichTextField()),
                ('vistas', models.PositiveIntegerField(default=0)),
                ('destacado', models.BooleanField(default=False)),
                ('visible', models.BooleanField(default=True)),
                ('imagen', models.ImageField(default='static/post/post_default.jpg', upload_to='media')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog_grupo_1.categoria')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.perfil')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('creado',),
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=5000)),
                ('visible', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.perfil')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog_grupo_1.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]