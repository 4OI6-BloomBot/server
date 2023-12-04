# 
# URL mapping for the sensor data app
# 

from django.urls import path

from . import views

app_name    = 'location' # Register namespace
urlpatterns = [
    path("",                 views.IndexView.as_view(),  name="index"),
    path("device/<int:pk>/", views.DeviceView.as_view(), name="device"),
    # path("<int:id>/edit/", views.edit,                 name="edit"),
]