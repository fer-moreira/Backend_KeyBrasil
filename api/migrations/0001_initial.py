# Generated by Django 3.0.6 on 2020-05-16 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImageModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500, verbose_name='Name')),
                ('url', models.CharField(max_length=500, verbose_name='Url')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Product Image',
                'verbose_name_plural': 'Product Images',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, verbose_name='Product Name')),
                ('model_name', models.CharField(max_length=150, verbose_name='Product Model')),
                ('slug', models.SlugField(max_length=150)),
                ('price', models.FloatField(max_length=150, verbose_name='Price')),
                ('stock_count', models.IntegerField(verbose_name='In Stock')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('images', models.ManyToManyField(to='api.ProductImageModel')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='SwitchTypesModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('model_name', models.CharField(max_length=150, verbose_name='Model')),
                ('slug', models.SlugField(max_length=150)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('images', models.ManyToManyField(to='api.ProductImageModel')),
            ],
            options={
                'verbose_name': 'Switch Type',
                'verbose_name_plural': 'Switch Types',
            },
        ),
        migrations.CreateModel(
            name='ProductReviewModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('author_name', models.CharField(max_length=450, verbose_name='Author Name')),
                ('author_email', models.CharField(max_length=450, verbose_name='Author Email')),
                ('review_text', models.CharField(max_length=450, verbose_name='Description')),
                ('review_rating', models.IntegerField(verbose_name='Rating')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('product_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ProductModel')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
        migrations.AddField(
            model_name='productmodel',
            name='switch_type',
            field=models.ManyToManyField(to='api.SwitchTypesModel'),
        ),
    ]
