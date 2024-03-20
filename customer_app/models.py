from django.db import models

# Create your models here.

## email/phone/address/city/state/zipcode



class Customer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    address = models.TextField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=54)
    zipcode = models.IntegerField()
    def __str__(self):
        return (f"{self.first_name} {self.last_name}")
    
    
    #   return (f"{self.first_name} {self.last_name}")
    