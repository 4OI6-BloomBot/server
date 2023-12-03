# 
# URL mapping for the sensor data app
# 

from django.urls import path

from . import views

app_name    = 'sensor_data' # Register namespace
urlpatterns = [
    path("",               views.index,  name="index"),
    # path("<int:pk>/",      views.DetailView.as_view(), name="detail"),
    # path("<int:id>/edit/", views.edit,                 name="edit"),
]