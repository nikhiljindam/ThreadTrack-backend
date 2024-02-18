from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    phone_number = models.IntegerField(max_length=11)
    gst_number = models.CharField(max_length=20)
    pan_number = models.CharField(max_length=15)
    logo = models.URLField(blank=True)
    enable = models.BooleanField(default=True)


class UserVendorMap(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    customer = models.ForeignKey(Vendor, on_delete=models.PROTECT)
