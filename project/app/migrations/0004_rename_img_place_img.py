# Generated by Django 3.2.13 on 2022-06-29 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_img_place_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='Img',
            new_name='img',
        ),
    ]
