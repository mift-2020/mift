# Generated by Django 3.0.7 on 2020-10-11 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0013_job_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='phone_number',
            field=models.PositiveIntegerField(blank=True, max_length=10),
        ),
    ]