# Generated by Django 4.2 on 2023-04-19 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testmodel',
            old_name='is_live',
            new_name='is_alive',
        ),
    ]
