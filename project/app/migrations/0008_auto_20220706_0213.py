# Generated by Django 3.2.13 on 2022-07-05 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='desc',
            new_name='dsc',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='img',
            new_name='imge',
        ),
    ]
