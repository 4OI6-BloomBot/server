from django.db import models

# =============================
# Device tracking model
# =============================
class Device(models.Model):
    name     = models.CharField(max_length = 100)
    hwID     = models.CharField(max_length = 50)
    lastSeen = models.DateTimeField(
                auto_now     = False,
                auto_now_add = True,
                null         = True
              )
    # config = models.ForeignKey(Config, on_delete=models.SET_NULL)
    # fleet  = models.ForeignKey(Fleet,  on_delete=models.SET_NULL)

    # Override to string method to return the given name
    def __str__(self):
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