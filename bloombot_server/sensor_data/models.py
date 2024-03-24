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

  # Reference to a location object that is assosiated
  # with the measurement.
  # Do not delete locations on measurement delete.
  # Does not have to be specified.
  location      = models.ForeignKey(
                    "location.Location",
                    on_delete = models.PROTECT,
                    blank     = True,
                    null      = True
                  )

  # Measurement value.
  value         = models.FloatField()

  # Log the time that the measurement was received by the
  # server to allow for real-time updates in the UI 
  time_received = models.DateTimeField(
                    auto_now_add = True
                  )

  # Override string method to return the given name
  def __str__(self):
    return str(self.device) + "_" + self.sensor.name
  

# =============================
# Deposit log model
# =============================
class Deposit(Measurement):
  
  # =====================================================
  # Get the pump from the database or create it if
  # it does not already exist.
  # =====================================================
  @classmethod
  def getPump(cls):
    sensor, created = Sensor.objects.get_or_create(
      name     = "Pump",
      defaults = {
        "unit"      : "mL",
        "precision" : 0.5
      }
    )

    return sensor