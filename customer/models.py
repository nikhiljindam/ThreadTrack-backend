from django.db import models
from vendors.models import Vendor


# Create your models here.
class Customer(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT)
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    phone_number = models.IntegerField(max_length=11)
    gst_number = models.CharField(max_length=20, null=True)
    pan_number = models.CharField(max_length=15, null=True)
