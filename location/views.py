from django.views import generic

# Add model import
from .models import Location

# ==========================================
# Root of app
# ==========================================
class IndexView(generic.ListView):
    template_name       = "location/index.html"
    context_object_name = "location_list"

    def get_queryset(self):
        return Location.objects.order_by('datetime')[:5]


# ==========================================
# Device location history
# ==========================================
class DeviceView(generic.ListView):
    template_name       = "location/index.html"
    context_object_name = "location_list"

    def get_queryset(self):
        return Location.objects.filter(pk = self.kwargs.get('pk')).order_by('datetime')[:5]