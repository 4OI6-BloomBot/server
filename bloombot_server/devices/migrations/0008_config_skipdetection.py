# Generated by Django 4.2.7 on 2024-04-07 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0007_config_deltafluorothresh'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='skipDetection',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
