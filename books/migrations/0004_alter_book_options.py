# Generated by Django 4.0.1 on 2022-01-14 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('status_special', 'Can read all books')]},
        ),
    ]
