# Generated by Django 4.0.4 on 2022-05-06 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='shortcuts',
            new_name='shortcut',
        ),
        migrations.RenameField(
            model_name='shortcut',
            old_name='shortcut_keys',
            new_name='shortcut_key',
        ),
    ]