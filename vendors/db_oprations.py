from vendors.models import UserVendorMap
from django.contrib.auth.models import User


def fetch_vendor_details_by_user(user: User):
    return UserVendorMap.objects.get(user=user)
