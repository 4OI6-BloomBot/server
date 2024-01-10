# ==========================================
# Serializer for models for use in the API
# ==========================================

# ========================
# Imports
# ========================
from rest_framework import serializers
from .models        import Measurement, Sensor
 

# ==========================================
# Sensor type serializer
# ==========================================      
class SensorSerializer(serializers.ModelSerializer):
   
  class Meta:
    model = Sensor
    fields = (
      'id', 
      'name'
    )
    

# ==========================================
# Sensor data serializer
# ==========================================
class MeasurementSerializer(serializers.ModelSerializer):
    
  device = SensorSerializer(read_only = True)

  class Meta:
    model  = Measurement
    fields = (
      'id',
      'device',
      'sensor',
      'value',
      'datetime'
    )