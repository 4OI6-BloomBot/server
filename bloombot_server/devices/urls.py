# 
# URL mapping for the devices app
# 

from django.urls import path

from . import views

app_name    = 'devices' # Register namespace
urlpatterns = [
    path("",               views.IndexView.as_view(),  name="index"),
    path("<int:pk>/",      views.DetailView.as_view(), name="detail"),
    path("<int:id>/edit/", views.edit,                 name="edit"),
]