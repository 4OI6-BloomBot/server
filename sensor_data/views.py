from django.views     import generic

# Add model import
from .models import Measurement, Sensor

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

        context['sensor_list'] = getSensors()

        return context


    def get_queryset(self):
        return Measurement.objects.order_by('datetime')[:5]


# ==========================================
# Display sensor specific data
# ==========================================
class SensorView(generic.ListView):
    template_name       = "sensor_data/index.html"
    context_object_name = "measurement_list"

    # Add the page type for nav
    def get_context_data(self, *args, **kwargs):
        context = super(generic.ListView, self).get_context_data(*args, **kwargs)

        context['page_category'] = "sensor_data"
        context['page_title']    = Sensor.objects.get(pk = self.kwargs['pk']).name + " data"

        context['sensor_list'] = getSensors()

        return context


    def get_queryset(self):
        return Measurement.objects.filter(sensor = self.kwargs['pk']).order_by('datetime')




def getSensors():
    return Sensor.objects.order_by('name')