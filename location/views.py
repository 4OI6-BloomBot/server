from django.views import generic

# Add model import
from .models import Location


# ==========================================
# Show location history of all devices
# ==========================================
class IndexView(generic.ListView):
    template_name       = "location/index.html"
    context_object_name = "device_location_list"

    def get_queryset(self):
        data = Location.objects.order_by('device', 'datetime')

        data_sorted = {}
        for location in data.all():
            if location.device.id not in data_sorted:
                data_sorted[location.device.id] = []
            data_sorted[location.device.id].append(location)

        return data_sorted
    

# ======================================================
# Query to pull the most recent location of each device
# If an ID is provided then the most recent locations 
# of the device are returned instead.
# ======================================================
def getDeviceLocations(pk = None):
    if pk is None:
      return Location.objects.order_by('device', '-datetime').distinct('device')

    return Location.objects.filter(device = pk).order_by('datetime') 