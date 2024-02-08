from django.db import models


# ===============================
# Device configuration tracking
# ===============================
class Config(models.Model):

  # Name for config
  name = models.CharField(
          max_length = 100, 
          unique     = True
        )
  
  # Temperature threshold
  temp_thresh = models.FloatField()

  @classmethod
  def getDefault(cls):
     config, created = cls.objects.get_or_create(
        name     = "Default",
        defaults = {
          "temp_thresh" : 25.0
        }
     )

     return config.pk



# =============================
# Device tracking model
# =============================
class Device(models.Model):
    name        = models.CharField(max_length = 100)

    hwID        = models.CharField(
                    max_length = 50,
                    unique     = True
                  )
    
    timeCreated = models.DateTimeField(
                    auto_now_add = True
                  )

    # Reference to the applied config
    # Do not allow the config to be deleted if it is
    # still configured on a device.
    config      = models.ForeignKey(
                    Config, 
                    on_delete = models.PROTECT,
                    default   = Config.getDefault
                  )
    
    # fleet  = models.ForeignKey(Fleet,  on_delete=models.SET_NULL)


    # ====================================================
    # Find the last time the device was referenced in the 
    # relevant models.
    # ====================================================
    @property
    def lastSeen(self):
        time_list = []
        
        # Get the most recent times from the sets
        location_t    = self.location_set.latest('datetime').datetime
        measurement_t = self.measurement_set.latest('datetime').datetime

        # Only add the times if they are not none values
        if (location_t): 
          time_list.append(location_t)

        if (measurement_t): 
          time_list.append(measurement_t)
        
        # Add created time as default
        time_list.append(self.timeCreated)

        # Sort the list and return the most recent entry
        time_list.sort(reverse = True)

        return time_list[0]

    # ====================================================
    # Override to string method to return the given name
    # Return the hwID if no name is given
    # ====================================================
    def __str__(self):
        if (len(self.name) == 0):
            return self.hwID
        
        return self.name
      

# =============================
# Grouping system for devices
# =============================
# class Fleet():
    # name = models.CharField(max_length = 100) 