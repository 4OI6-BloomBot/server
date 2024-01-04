from rest_framework import viewsets
from django.views   import generic
from .models        import Measurement
from .serializers   import MeasurementSerializer


class MeasurementViewset(viewsets.ModelViewSet):
    # define queryset
    queryset = Measurement.objects.all()
 
    # specify serializer to be used
    serializer_class = MeasurementSerializer