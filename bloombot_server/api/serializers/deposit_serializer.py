# ==========================================
# Sensor type serializer
# ==========================================      
from rest_framework          import serializers
from ..models                import Deposit
from .measurement_serializer import MeasurementSerializer

class DepositSerializer(MeasurementSerializer):
  
  class Meta():
    model  = Deposit
    fields = (
      'id',
      'device',
      'location',
      'value',
      'datetime'
    ) 

  # ==============================================
  # Update the sensor object with the static pump
  # ==============================================
  def validate(self, validated_data):
    validated_data['sensor'] = Deposit.getPump()

    return validated_data