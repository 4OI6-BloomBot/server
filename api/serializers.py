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
      'hwID',
      'name'
    )

    # Do not provide a name through the API
    read_only_fields = ['name']

    # Hardware ID should only be provided for writes
    extra_kwargs = {
      'hwID' : {
        'write_only' : True
      }
    }

  

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
    
  device = DeviceSerializer()
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

  # ==========================================
  # Validate the passed data
  # ==========================================
  def validate(self, validated_data):
    if (self.context['request'].method == 'POST'):
      validated_data['device'] = self.context

  # ==========================================
  # Create a new object with the passed data
  # ==========================================
  def create(self, validated_data):
    return Measurement.objects.create(**validated_data)