from django.contrib import admin
from .models        import Device

# =========================================
# Register the app models with the project
# =========================================
admin.site.register(Device)