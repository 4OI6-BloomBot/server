from django.db    import models

# =============================
# Sensor type model
# =============================
class Sensor(models.Model):
  name      = models.CharField(max_length = 200)
  unit      = models.CharField(max_length = 50)
  precision = models.FloatField()

  # Override string method to return the given name
  def __str__(self):
    return self.name


# =============================
# Measurement log model
# =============================
class Measurement(models.Model):
  datetime      = models.DateTimeField(
                    auto_now     = False,
                    auto_now_add = False
                  )
  
  # Reference to the sensor type
  # Do not allow sensor types to be deleted if they are being used
  sensor        = models.ForeignKey(
                    Sensor,
                    on_delete = models.PROTECT 
                  )
  
  # Reference to the device that created the data
  # When the device is deleted, delete the sensor data
  device        = models.ForeignKey(
                    "devices.Device",
                    on_delete = models.CASCADE
                  )
  
  value         = models.FloatField()

  # Log the time that the measurement was received by the
  # server to allow for real-time updates in the UI 
  time_received = models.DateTimeField(
                    auto_now_add = True
                  )

  # Override string method to return the given name
  def __str__(self):
    return str(self.device) + "_" + self.sensor.name
  