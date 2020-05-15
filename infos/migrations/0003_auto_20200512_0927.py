# Generated by Django 2.2.3 on 2020-05-12 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0002_auto_20200512_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='infos',
            name='latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='infos',
            name='longitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='infos',
            name='info',
            field=models.TextField(default=None),
        ),
    ]