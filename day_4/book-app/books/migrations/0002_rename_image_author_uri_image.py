# Generated by Django 3.2.14 on 2022-07-14 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='image',
            new_name='uri_image',
        ),
    ]
