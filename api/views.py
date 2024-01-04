from rest_framework import viewsets
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
        device_id = self.request.query_params.get('device');
        
        # Apply the filters only if the params exist and are not all
        if (sensor_id and sensor_id is not 'all'):
            queryset = queryset.filter(sensor = sensor_id)

        if (device_id and device_id is not 'all'):
            queryset = queryset.filter(device = device_id)


        return queryset