# 
# URL mapping for the devices app
# 

from django.urls import path

from . import views

app_name    = 'devices' # Register namespace
urlpatterns = [
    path("",          views.index,       name="index"),
    path("<int:id>/", views.fetchDevice, name="detail"),
]