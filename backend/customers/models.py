from django.db import models


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    dob = models.DateField(blank=False, null=False)

