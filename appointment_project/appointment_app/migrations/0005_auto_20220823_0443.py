# Generated by Django 3.2.7 on 2022-08-23 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment_app', '0004_auto_20220823_0435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='start_time',
        ),
    ]