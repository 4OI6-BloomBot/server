from typing import Any
from django.shortcuts import get_object_or_404
from django.http      import HttpResponseRedirect
from django.views     import generic
from django.urls      import reverse

# Add model import
from .models        import Device, Config
from location.views import getDeviceLocations


# ==========================================
# Root of app. Fetch a list of all devices
# ==========================================
class IndexView(generic.ListView):
    template_name       = "devices/index.html"
    context_object_name = "device_list"

    # Add the device locations to the passed arguments
    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['location_json'] = getDeviceLocations()

        # Add the page type for nav
        context['page_category'] = "device"
        context['page_title']    = "devices"

        return context

    def get_queryset(self):
        return Device.objects.order_by('name')[:5]


# ==========================================
# Get the details of a device givin its ID
# ==========================================
class DetailView(generic.DetailView):
    template_name = "devices/details.html"
    model         = Device

    # Add the device locations to the passed arguments
    def get_context_data(self, *args, **kwargs):
        context = super(DetailView, self).get_context_data(*args, **kwargs)
        context['location_json'] = getDeviceLocations(self.kwargs['pk'])

        # Add the config options
        context['configs']  = getConfigs()

        # Add the page data for base template
        context['page_category'] = "device"
        context['page_title']    = str(self.object)

        return context


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

    

# ==========================================
# Get the details of a config givin its ID
# ==========================================
class ConfDetailView(generic.DetailView):
    template_name = "devices/configDetails.html"
    model         = Config

    # Add the device locations to the passed arguments
    def get_context_data(self, *args, **kwargs):
        context = super(ConfDetailView, self).get_context_data(*args, **kwargs)
        # context['location_json'] = getDeviceLocations(self.kwargs['pk'])

        # Add the config options
        # context['configs']  = getConfigs()

        # Add the page data for base template
        context['page_category'] = "device"
        context['page_title']    = "Edit " + str(self.object)
        print(context)

        return context


# ======================================================
# Grab the configurations from the database
# ======================================================
def getConfigs(pk = None):
    # Determine the query to run
    if pk is None:
      configs = Config.objects.order_by('name')
    else:
      configs = Config.objects.filter(pk = pk)
        
    # Parse as JSON and return
    return configs


# ==========================================
# Edit a config given its ID
# ==========================================
def editConfig(request, pk):

    # Get device from ID
    config = get_object_or_404(Config, pk = pk)

    # Get form data
    config.name            = request.POST['configName']
    config.tempThresh      = request.POST['tempThresh']
    config.deltaTempThresh = request.POST['deltaTempThresh']
    config.deltaTurbThresh = request.POST['deltaTurbThresh']
    config.fluoroThresh    = request.POST['fluoroThresh']

    # Update object in DB
    config.save()

    return HttpResponseRedirect(reverse("devices:index"))

# ==========================================
# Apply a new config to a specific device
# ==========================================
def setConfig(request, id):

    # Get device from ID
    device = get_object_or_404(Device, pk = id)

    # Get form data
    namePrefix = request.POST['prefix']
    confID     = request.POST[namePrefix + 'configName']
    
    # Get config item from ID
    config = get_object_or_404(Config, pk = confID)

    # Update object in DB
    device.config = config
    device.save()

    # Redirect back to the device list (TODO: Update redirect)
    return HttpResponseRedirect(reverse("devices:index"))