from rest_framework import serializers
from .models import Customer


class CustomerCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ("first_name", "last_name", "dob")
