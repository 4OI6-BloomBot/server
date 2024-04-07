# ==========================================
# Config type serializer
# ==========================================      
from rest_framework import serializers
from ..models       import Config

class ConfigSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Config
    fields = (
      'id', 
      'name',
      'tempThresh',
      'deltaTempThresh', 
      'turbThresh',
      'deltaTurbThresh',
      'fluoroThresh',
      'deltaFluoroThresh',
      'skipDetection'
    )

    # Do not allow writes through the API
    read_only_fields = ['name', 
                        'tempThresh',
                        'deltaTempThresh',
                        'turbThresh',
                        'deltaTurbThresh',  
                        'fluoroThresh',
                        'deltaFluoroThresh',
                        'skipDetection']
