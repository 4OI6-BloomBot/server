# 
# URL mapping for the sensor data app
# 

from django.urls    import path, include
from .              import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'measurements', views.MeasurementViewset)

app_name    = 'sensor_data' # Register namespace
urlpatterns = [
    path("",               views.IndexView.as_view(),  name = "index"),
    path("<int:pk>/",      views.SensorView.as_view(), name = "sensor"),
    path("api/",           include(router.urls)),
    path("api-auth/",      include("rest_framework.urls")),
    # path("<int:id>/edit/", views.edit,                 name="edit"),
]