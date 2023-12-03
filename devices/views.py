from django.shortcuts import get_object_or_404
from django.http      import HttpResponseRedirect
from django.views     import generic
from django.urls      import reverse

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


# ==========================================
# Edit a device given its ID
# ==========================================
def edit(request, id):

    # Get device from ID
    device = get_object_or_404(Device, pk = id)

    # Get form data
    new_name = request.POST['name']

    # Update object in DB
    device.name = new_name
    device.save()

    # Redirect back to the device list (TODO: Update redirect)
    return HttpResponseRedirect(reverse("devices:index"))

    