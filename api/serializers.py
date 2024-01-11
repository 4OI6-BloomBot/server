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
  

# ==========================================
# Sensor type serializer
# ==========================================      
class SensorSerializer(serializers.ModelSerializer):
  
  id = serializers.IntegerField()

  class Meta:
    model = Sensor
    fields = (
      'id', 
      'name',
      'unit'
    )

    # Do not allow writes to the sensor data
    read_only_fields = ('name', 'unit')


  # ==========================================
  # Check if the sensor ID exists and update
  # the data with the obj if so
  # ==========================================
  def validate(self, validated_data):
    
    if (self.context['request'].method == 'POST'):
      # Check if sensor with the passed ID exists
      # Throw an error if it DNE
      try:
        validated_data = Sensor.objects.get(id = validated_data['id'])
      except:
        raise serializers.ValidationError(detail = "Sensor with ID " + str(validated_data['id']) + " does not exist", code = 200)

    return validated_data


# ==========================================
# Sensor data serializer
# ==========================================
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