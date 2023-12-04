from django.db import models

# =============================
# Location model
# =============================
class Location(models.Model):
    latitude  = models.DecimalField(
                  max_digits     = 9,
                  decimal_places = 6
                )
    
    longitude = models.DecimalField(
                  max_digits     = 9,
                  decimal_places = 6
                )
    
    datetime  = models.DateTimeField(
                  auto_now     = False,
                  auto_now_add = True,
                  null         = True
                )
    
    device    = models.ForeignKey(
                  "devices.Device",
                  on_delete = models.CASCADE
                )

    
    # Override to string method to return the given name
    def __str__(self):
        return self.device.name + "_" + self.datetime