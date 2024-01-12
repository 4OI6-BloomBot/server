# ==========================================
# Device type serializer
# ==========================================      
from rest_framework import serializers
from ..models       import Device

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
        'write_only' : True,
        'validators' : []
      },
    }
  

  # ==========================================
  # Update the data with the device obj
  # ==========================================
  def validate(self, validated_data):
    # If the device does not exist, create it.
    # Otherwise, return the device
    try:
      validated_data = Device.objects.get(hwID = validated_data['hwID'])
    except:
      validated_data = self.save(validated_data['hwID'])

    return validated_data


  # ==========================================
  # Create a new device with the given hwID
  # ==========================================
  def save(self, hwID):
    device = Device(hwID = hwID)
    device.save()

    return device