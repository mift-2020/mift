# Generated by Django 3.0.7 on 2020-10-11 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_remove_user_account_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='account_no',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
