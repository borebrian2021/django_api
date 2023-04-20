# Generated by Django 4.2 on 2023-04-19 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0004_alter_testmodel_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testmodel',
            options={'ordering': ('-amount',)},
        ),
        migrations.AddField(
            model_name='testmodel',
            name='extra_name',
            field=models.CharField(default='null', editable=False, max_length=255),
        ),
    ]