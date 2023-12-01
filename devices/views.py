from django.shortcuts import loader, render, get_object_or_404
from django.http      import HttpResponse, Http404
from django.views     import generic

# Add model import
from .models import Device

# ==========================================
# Root of app. Fetch a list of all devices
# ==========================================
class IndexView(generic.ListView):
    template_name       = "devices/index.html"
    context_object_name = "device_list"

    def get_queryset(self):
        return Device.objects.order_by('name')[:5]


# ==========================================
# Get the details of a device givin its ID
# ==========================================
class DetailView(generic.DetailView):
    template_name = "devices/details.html"
    model         = Device


    