# Generated by Django 2.0.2 on 2018-08-21 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0004_auto_20180409_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='time_begin',
        ),
        migrations.RemoveField(
            model_name='events',
            name='time_end',
        ),
    ]
