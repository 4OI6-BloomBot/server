# 
# URL mapping for the sensor data app
# 

from django.urls import path

from . import views

app_name    = 'sensor_data' # Register namespace
urlpatterns = [
    path("",               views.IndexView.as_view(),  name="index"),
    path("<int:pk>/",      views.SensorView.as_view(), name="sensor"),
    # path("<int:id>/edit/", views.edit,                 name="edit"),
]