# Generated by Django 3.0.6 on 2020-05-16 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200516_1918'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brandsmodel',
            options={'verbose_name': 'Brand', 'verbose_name_plural': 'Brands'},
        ),
        migrations.AlterField(
            model_name='brandsmodel',
            name='text',
            field=models.TextField(max_length=500, verbose_name='Description'),
        ),
    ]
