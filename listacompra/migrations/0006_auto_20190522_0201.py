# Generated by Django 2.2.1 on 2019-05-22 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listacompra', '0005_auto_20190521_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productosm',
            name='descripcion',
            field=models.CharField(max_length=500),
        ),
    ]
