# Generated by Django 2.2.1 on 2019-05-22 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listacompra', '0002_auto_20190521_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productosm',
            name='descripcion',
            field=models.URLField(max_length=500),
        ),
    ]
