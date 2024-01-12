# ==========================================
# Sensor data serializer
# ==========================================
from rest_framework     import serializers
from ..models           import Measurement
from .device_serializer import DeviceSerializer
from .sensor_serializer import SensorSerializer

class MeasurementSerializer(serializers.ModelSerializer):
    
  device = DeviceSerializer()
  sensor = SensorSerializer()

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
  # TODO: Need to check if value/date needs
  #       validation.
  # ==========================================
  def validate(self, validated_data):

    # New measurement validation
    if (self.context['request'].method == 'POST'):
      return validated_data