# ==========================================
# Location data serializer
# ==========================================
from rest_framework     import serializers
from ..models           import Location
from .device_serializer import DeviceSerializer

class LocationSerializer(serializers.ModelSerializer):
    
  device = DeviceSerializer()

  class Meta:
    model  = Location
    fields = (
      'id',
      'device',
      'latitude',
      'longitude',
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