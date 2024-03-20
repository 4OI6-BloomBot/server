# 
# URL mapping for the sensor data app
# 

from django.urls    import path
from .              import views

app_name    = 'sensor_data' # Register namespace
urlpatterns = [
    path("", views.IndexView.as_view(), name = "index")
]