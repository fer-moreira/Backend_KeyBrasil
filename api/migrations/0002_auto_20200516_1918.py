# Generated by Django 3.0.6 on 2020-05-16 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandsModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(max_length=150)),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('text', models.CharField(max_length=450, verbose_name='Description')),
                ('image', models.CharField(max_length=450, verbose_name='Image')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
        ),
        migrations.AlterModelOptions(
            name='productimagemodel',
            options={'verbose_name': 'Image', 'verbose_name_plural': 'Images'},
        ),
        migrations.AlterModelOptions(
            name='productmodel',
            options={'verbose_name': 'Keyboard', 'verbose_name_plural': 'Keyboards'},
        ),
        migrations.AlterModelOptions(
            name='switchtypesmodel',
            options={'verbose_name': 'Switch', 'verbose_name_plural': 'Switches'},
        ),
    ]
