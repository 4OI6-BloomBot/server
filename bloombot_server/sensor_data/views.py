from django.views   import generic
from .models        import Sensor

# ==========================================
# Root of app. Fetch a list of all sensors
# ==========================================
class IndexView(generic.ListView):
    template_name       = "sensor_data/index.html"
    context_object_name = "sensor_list"

    # Add the page type for nav
    def get_context_data(self, *args, **kwargs):
        context = super(generic.ListView, self).get_context_data(*args, **kwargs)

        context['page_category'] = "sensor_data"
        context['page_title']    = "sensor data"

        return context


    # Add the list of sensors to the view
    def get_queryset(self):
        return Sensor.objects.order_by('name')