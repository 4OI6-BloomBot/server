from django.db import models

# Import the models that are referenced in the API
from sensor_data.models import Measurement, Sensor
from devices.models     import Device
from location.models    import Location
