# Generated by Django 4.2.7 on 2023-12-03 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_device_lastseen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='lastSeen',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
