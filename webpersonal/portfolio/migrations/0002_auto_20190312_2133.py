# Generated by Django 2.1.7 on 2019-03-13 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proyect',
            options={'ordering': ['-created'], 'verbose_name': 'proyecto', 'verbose_name_plural': 'proyectos'},
        ),
        migrations.AlterField(
            model_name='proyect',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='proyect',
            name='description',
            field=models.TextField(verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='proyect',
            name='image',
            field=models.ImageField(upload_to='projects', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='proyect',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='proyect',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición'),
        ),
    ]
