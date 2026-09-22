from django.db import models
from django.contrib.auth.models import User
from app1.models import Car


# from car_dealer_portal.models import Car
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_name = models.ForeignKey(Car, on_delete=models.CASCADE)
    plocation = models.CharField(max_length=100)
    dlocation = models.CharField(max_length=100)
    pdate = models.DateField()
    ddate = models.DateField()
    time = models.TimeField()
    is_status = models.CharField(max_length=20, default='pending')
    is_booked = models.BooleanField(default=False)
# Create your models here.
