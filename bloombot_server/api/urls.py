# 
# URL mapping for the API
# 

from django.urls    import path, include
from .              import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'measurements', views.MeasurementViewset)
router.register(r'location',     views.LocationViewset)

app_name    = 'api' # Register namespace
urlpatterns = [
    path("",                  include(router.urls)),
    path("api-auth/",         include("rest_framework.urls")),
    path("config/<int:pk>",   views.ConfigGet.as_view())
]