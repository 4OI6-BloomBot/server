from django.views import generic

# Add model import
from .models import Location


# ==========================================
# Show location history of all devices
# ==========================================
class IndexView(generic.ListView):
    template_name       = "location/index.html"
    context_object_name = "location_list"

    def get_queryset(self):
        return Location.objects.order_by('device', '-datetime').distinct('device')
    

# ======================================================
# Query to pull the most recent location of each device
# If an ID is provided then the most recent locations 
# of the device are returned instead.
# ======================================================
def getDeviceLocations(pk = None):
    if pk is None:
      return Location.objects.order_by('device', '-datetime').distinct('device')

    return Location.objects.filter(device = pk).order_by('datetime') 