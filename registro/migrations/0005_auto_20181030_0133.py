# Generated by Django 2.1.2 on 2018-10-30 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0004_auto_20181030_0130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='fechaNac',
            new_name='fechanac',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='tipoViv',
            new_name='tipoviv',
        ),
    ]
