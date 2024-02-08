from rest_framework                      import viewsets, mixins, generics
from .models                             import Measurement, Location, Device
from .serializers.measurement_serializer import MeasurementSerializer
from .serializers.location_serializer    import LocationSerializer
from .serializers.config_serializer      import ConfigSerializer
from django.utils                        import timezone
from django.shortcuts                    import get_object_or_404
from datetime                            import timedelta


# ======================================================
# Base viewset.
# Configured to only allow listing and creating data.
# TODO: Auth needs to be added
# ======================================================
class BaseViewset(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    
    # ============================================
    # Filter the queryset by the device ID
    # ============================================
    def filterDevice(self, queryset):
        device_id = self.request.query_params.get('device')

        # Only filter if we were passed an ID
        if (device_id and device_id != 'all'):
            queryset = queryset.filter(device = device_id)

        return queryset
    

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
        last_recieved_id = self.request.query_params.get('last_received')

        # Apply the filters only if the params exist and are not all
        if (sensor_id and sensor_id != 'all'):
            queryset = queryset.filter(sensor = sensor_id)

        queryset = self.filterDevice(queryset)


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

        queryset = self.filterDevice(queryset)

        return queryset.order_by("datetime")
    


# ======================================================
# Config data view set.
# Handles API access to the config data model. 
# ======================================================
class ConfigGet(generics.RetrieveAPIView):
    # Define queryset & serializer
    queryset         = Device.objects.all()
    serializer_class = ConfigSerializer

    # ===============================================
    # Return the config object instead of the device
    # Note: This is unchanged from the definition, 
    #       had to override method to return the 
    #       config from the device object.
    # ===============================================
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = get_object_or_404(queryset, **filter_kwargs)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj.config