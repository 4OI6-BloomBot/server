from django.views     import generic

# Add model import
from .models import Measurement

# ==========================================
# Root of app. Fetch a list of all devices
# ==========================================
class IndexView(generic.ListView):
    template_name       = "sensor_data/index.html"
    context_object_name = "measurement_list"

    # Add the page type for nav
    def get_context_data(self, *args, **kwargs):
        context = super(generic.ListView, self).get_context_data(*args, **kwargs)

        context['page_category'] = "sensor_data"
        context['page_title']    = "sensor data"

        return context


    def get_queryset(self):
        return Measurement.objects.order_by('datetime')[:5]
