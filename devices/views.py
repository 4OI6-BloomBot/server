from django.shortcuts import loader
from django.http      import HttpResponse

# Add model import
from .models import Device


def index(request):
    device_list = Device.objects.order_by("name")[:5]
    
    # Create template and pass data to it
    template = loader.get_template("devices/index.html")
    context  = {
        "device_list" : device_list
    }

    return HttpResponse(template.render(context, request))