# Generated by Django 3.0.7 on 2020-10-11 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20201011_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='account_no',
        ),
    ]