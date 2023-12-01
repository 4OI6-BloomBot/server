from django.shortcuts import loader, render, get_object_or_404
from django.http      import HttpResponse, Http404

# Add model import
from .models import Device

# ==========================================
# Root of app. Fetch a list of all devices
# ==========================================
def index(request):
    device_list = Device.objects.order_by("name")[:5]
    
    # Create template and pass data to it
    template = loader.get_template("devices/index.html")
    context  = {
        "device_list" : device_list
    }

    return HttpResponse(template.render(context, request))


# ==========================================
# Get the details of a device givin its ID
# ==========================================
def fetchDevice(request, id):
    device = get_object_or_404(Device, pk=id)

    return render(request, "devices/details.html", { "device" : device })