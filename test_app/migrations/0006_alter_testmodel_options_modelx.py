# Generated by Django 4.2 on 2023-04-19 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0005_alter_testmodel_options_testmodel_extra_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testmodel',
            options={'ordering': ('-amount',), 'verbose_name': 'Users'},
        ),
        migrations.CreateModel(
            name='ModelX',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('milage', models.FloatField()),
                ('test_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_content', to='test_app.testmodel')),
            ],
        ),
    ]
