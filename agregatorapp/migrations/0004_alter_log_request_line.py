# Generated by Django 3.2.12 on 2022-02-21 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agregatorapp', '0003_alter_log_header_user_agent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='request_line',
            field=models.TextField(default='-'),
        ),
    ]
