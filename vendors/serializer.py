from rest_framework import serializers
from vendors.models import UserVendorMap


class ReadUserVendor(serializers.ModelSerializer):
    class Meta:
        table = UserVendorMap
        fields = '__all__'
        depth = 1
