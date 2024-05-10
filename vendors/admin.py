from django.contrib import admin
from .models import *

models = [Vendor, UserVendorMap]

MySpecialAdmin = lambda model: type('SubClass'+model.__name__, (admin.ModelAdmin,), {
    'list_display': [x.name for x in model._meta.fields],
})

for model in models:
   try:
       admin.site.register(model, MySpecialAdmin(model))
   except admin.sites.AlreadyRegistered:
       pass
