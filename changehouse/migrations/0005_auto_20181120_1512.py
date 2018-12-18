# Generated by Django 2.0 on 2018-11-20 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('changehouse', '0004_auto_20181120_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Cli_Estado',
            field=models.CharField(choices=[('0', 'Activo'), ('1', 'Desactivo')], default='0', max_length=1),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Cli_TipoID',
            field=models.CharField(choices=[('TI', 'TI'), ('CC', 'CC')], default='TI', max_length=2),
        ),
    ]