# Generated by Django 3.2.7 on 2022-08-23 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment_app', '0002_alter_appointment_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]