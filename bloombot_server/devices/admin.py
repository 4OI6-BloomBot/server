from django.contrib import admin
from .models        import Device, Config

# =========================================
# Register the app models with the project
# =========================================
admin.site.register(Device)
admin.site.register(Config)