# Generated by Django 3.2.7 on 2022-08-23 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment_app', '0003_auto_20220823_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='end_time',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='start_time',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
