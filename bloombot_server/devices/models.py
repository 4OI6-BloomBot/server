from django.db import models

# =============================
# Device tracking model
# =============================
class Device(models.Model):
    name     = models.CharField(max_length = 100)
    hwID     = models.CharField(
                max_length = 50,
                unique     = True
               )
    lastSeen = models.DateTimeField(
                auto_now     = False,
                auto_now_add = True,
                null         = True
               )
    # config = models.ForeignKey(Config, on_delete=models.SET_NULL)
    # fleet  = models.ForeignKey(Fleet,  on_delete=models.SET_NULL)

    # Override to string method to return the given name
    # Return the hwID if no name is given
    def __str__(self):
        if (len(self.name) == 0):
            return self.hwID
        
        return self.name

# ===============================
# Device configuration tracking
# ===============================
# class Config():


# =============================
# Grouping system for devices
# =============================
# class Fleet():
    # name = models.CharField(max_length = 100) 