from   django.views                 import generic
from   django.core.serializers.json import DjangoJSONEncoder
import json

# Add model import
from .models import Location

# Add serializer for location
# TODO: Probably should have defined the serializers in each of the apps instead of
#       in the API.
from api.serializers.location_serializer import LocationSerializer


# ==========================================
# Show location history of all devices
# ==========================================
class IndexView(generic.ListView):
    template_name       = "location/index.html"
    context_object_name = "location_json"

    # Add the base template data
    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)

        context['page_category'] = "device"
        context['page_title']    = "Location History"

        return context

    def get_queryset(self):
        data = Location.objects.order_by('device', 'datetime')
        ser  = LocationSerializer(data, many = True)

        return json.dumps(ser.data)
    

# ======================================================
# Query to pull the most recent location of each device
# If an ID is provided then the most recent locations 
# of the device are returned instead.
# ======================================================
def getDeviceLocations(pk = None):
    # Determine the query to run
    if pk is None:
      locations = Location.objects.order_by('device', '-datetime').distinct('device')
    else:
      locations = Location.objects.filter(device = pk).order_by('datetime') 
    
    # Serialize the data
    ser = LocationSerializer(locations, many = True)
    
    # Parse as JSON and return
    return json.dumps(ser.data)