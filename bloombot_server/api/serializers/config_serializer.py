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
      'temp_thresh'
    )

    # Do not allow writes through the API
    read_only_fields = ['name', 'temp_thresh']