# ==========================================
# Serializer for models for use in the API
# ==========================================

# ========================
# Imports
# ========================
from rest_framework import serializers
from .models        import Measurement
 

# ==========================================
# Sensor data serializer
# ==========================================
class MeasurementSerializer(serializers.ModelSerializer):
    
  class Meta:
      model  = Measurement
      fields = (
          'id',
          'device',
          'sensor',
          'value',
          'datetime'
      )

