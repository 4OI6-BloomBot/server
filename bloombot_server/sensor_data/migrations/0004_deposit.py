# Generated by Django 4.2.7 on 2024-03-24 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sensor_data', '0003_measurement_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('measurement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sensor_data.measurement')),
            ],
            bases=('sensor_data.measurement',),
        ),
    ]
