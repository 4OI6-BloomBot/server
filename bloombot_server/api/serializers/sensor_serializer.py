# ==========================================
# Sensor type serializer
# ==========================================      
from rest_framework import serializers
from ..models       import Sensor

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
