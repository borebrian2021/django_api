# Generated by Django 4.2 on 2023-04-19 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('description', models.TextField()),
                ('phone_number', models.PositiveBigIntegerField()),
                ('is_live', models.BooleanField()),
                ('amount', models.FloatField()),
            ],
        ),
    ]
