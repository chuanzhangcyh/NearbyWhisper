# Generated by Django 2.2.3 on 2020-05-12 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Infos',
        ),
    ]