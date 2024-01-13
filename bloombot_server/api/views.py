from rest_framework                      import viewsets, mixins
from .models                             import Measurement, Location
from .serializers.measurement_serializer import MeasurementSerializer
from .serializers.location_serializer    import LocationSerializer
from django.utils                        import timezone, dateparse
from datetime                            import timedelta


# ======================================================
# Base viewset.
# Configured to only allow listing and creating data.
# TODO: Auth needs to be added
# ======================================================
class BaseViewset(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    
    pass


# ======================================================
# Sensor data view set.
# Handles API access to the sensor data model. 
# ======================================================
class MeasurementViewset(BaseViewset):
    # Define queryset & serializer
    queryset         = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    # ============================================
    # Update the queryset with filters applied
    # ============================================
    def get_queryset(self):
        queryset = Measurement.objects.all()

        # Grab the parameters from the HTTP request
        sensor_id        = self.request.query_params.get('sensor')
        device_id        = self.request.query_params.get('device')
        last_recieved_id = self.request.query_params.get('last_received')
        
        # Apply the filters only if the params exist and are not all
        if (sensor_id and sensor_id != 'all'):
            queryset = queryset.filter(sensor = sensor_id)

        if (device_id and device_id != 'all'):
            queryset = queryset.filter(device = device_id)


        # Only return values that were added since the last_recieve_time
        # Set the start time to be slightly past the given recieve time to avoid duplication
        if (last_recieved_id):
            
            # Get the object from the passed ID
            last_recieved_obj = Measurement.objects.get(id = last_recieved_id)

            # If the obj exists, filter the data based off of its creation time
            if (last_recieved_obj):
                start_time = last_recieved_obj.time_received + timedelta(seconds = 1)
                queryset   = queryset.filter(time_received__range = [start_time, timezone.now()])


        return queryset.order_by("time_received")
    

  
# ======================================================
# Location data view set.
# Handles API access to the location data model. 
# ======================================================
class LocationViewset(BaseViewset):
    # Define queryset & serializer
    queryset         = Location.objects.all()
    serializer_class = LocationSerializer

    # ============================================
    # Update the queryset with filters applied
    # ============================================
    def get_queryset(self):
        queryset = Location.objects.all()

        # Grab the parameters from the HTTP request
        device_id = self.request.query_params.get('device')
        
        # Apply the filters only if the params exist and are not all
        if (device_id and device_id != 'all'):
            queryset = queryset.filter(device = device_id)

        return queryset.order_by("datetime")