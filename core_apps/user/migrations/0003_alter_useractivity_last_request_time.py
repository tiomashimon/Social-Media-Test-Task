# Generated by Django 4.2.5 on 2023-12-21 12:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_userprofile_useractivity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivity',
            name='last_request_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
