# Generated by Django 3.2.13 on 2022-07-05 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_delete_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noun', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='imgs')),
                ('desc', models.TextField()),
            ],
        ),
    ]
