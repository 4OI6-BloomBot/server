from django.views     import generic

# Add model import
from .models import Measurement

# ==========================================
# Root of app. Fetch a list of all devices
# ==========================================
class IndexView(generic.ListView):
    template_name       = "sensor_data/index.html"
    context_object_name = "measurement_list"

    def get_queryset(self):
        return Measurement.objects.order_by('datetime')[:5]
