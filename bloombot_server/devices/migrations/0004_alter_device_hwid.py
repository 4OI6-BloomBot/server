# Generated by Django 4.2.7 on 2024-01-11 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0003_alter_device_lastseen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='hwID',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
