from django.contrib.auth.models import User
from django.db import models
class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    per_day_price = models.IntegerField()
    per_hour_price = models.IntegerField()
    company_name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='cars/image')
    is_published = models.BooleanField(default=False)
# Create your models here.
