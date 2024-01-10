# ==========================================
# Serializer for models for use in the API
# ==========================================

# ========================
# Imports
# ========================
from rest_framework import serializers
from .models        import Measurement, Sensor, Device


# ==========================================
# Sensor type serializer
# ==========================================      
class DeviceSerializer(serializers.ModelSerializer):
   
  class Meta:
    model = Device
    fields = (
      'id', 
      'name'
    )


# ==========================================
# Sensor type serializer
# ==========================================      
class SensorSerializer(serializers.ModelSerializer):
   
  class Meta:
    model = Sensor
    fields = (
      'id', 
      'name',
      'unit'
    )


# ==========================================
# Sensor data serializer
# ==========================================
class MeasurementSerializer(serializers.ModelSerializer):
    
  device = DeviceSerializer(read_only = True)
  sensor = SensorSerializer(read_only = True)

  class Meta:
    model  = Measurement
    fields = (
      'id',
      'device',
      'sensor',
      'value',
      'datetime'
    )