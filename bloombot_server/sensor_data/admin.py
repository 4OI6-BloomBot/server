from django.contrib import admin
from.models         import Sensor, Measurement, Deposit

# =========================================
# Register the app models with the project
# =========================================
admin.site.register(Sensor)
admin.site.register(Measurement)
admin.site.register(Deposit)