# Generated by Django 2.0 on 2018-04-11 08:20

from django.db import migrations, models
import sprintercarsapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to=sprintercarsapp.models.upload_product_image)),
                ('description', models.CharField(max_length=300)),
                ('specification', models.CharField(max_length=200)),
                ('is_latest', models.BooleanField(default=False)),
                ('is_sold', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
    ]