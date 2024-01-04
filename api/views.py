from rest_framework import generics, viewsets
from .models        import Measurement
from .serializers   import MeasurementSerializer


# ======================================================
# Sensor data view set.
# Handles API access to the sensor data model. 
# TODO: Auth needs to be added for writes
# ======================================================
class MeasurementViewset(viewsets.ModelViewSet):
    # Define queryset & serializer
    queryset         = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    # ============================================
    # Update the queryset with filters applied
    # ============================================
    def get_queryset(self):
        queryset = Measurement.objects.all()

        # Grab the parameters from the HTTP request
        sensor_id = self.request.query_params.get('sensor')
        
        # Apply the filters only if the params exist
        if (sensor_id is not None):
            queryset = queryset.filter(sensor = sensor_id)

        return queryset