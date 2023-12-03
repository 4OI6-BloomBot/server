from django.contrib import admin
from.models         import Sensor, Measurement

# =========================================
# Register the app models with the project
# =========================================
admin.site.register(Sensor)
admin.site.register(Measurement)