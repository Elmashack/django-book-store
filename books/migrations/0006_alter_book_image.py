# Generated by Django 4.0.1 on 2022-01-20 08:45

import config.storage_backends
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_book_id_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(null=True, storage=config.storage_backends.PublicMediaStorage, upload_to='covers/%Y/%m/'),
        ),
    ]