from django.db import models
from django.contrib.auth.models import User

class DistanceBasePrice(models.Model):
    price = models.FloatField()
    km_value = models.FloatField()
    day = models.CharField(max_length=10, null=True, blank=True)
    created_time = models.DateTimeField(auto_now=True)
    updated_time = models.DateTimeField(auto_now=False, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_by_distance_base_price')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_by_distance_base_price')
    is_enabled = models.BooleanField(default=False)

class DistanceAdditionalPrice(models.Model):
    price = models.FloatField()
    km_value = models.FloatField()
    created_time = models.DateTimeField(auto_now=True)
    updated_time = models.DateTimeField(auto_now=False, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_by_distance_additional_price')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_by_distance_additional_price')
    is_enabled = models.BooleanField(default=False)
    

class TimeMultiplierFactor(models.Model):
    price = models.FloatField()
    hours = models.FloatField()
    created_time = models.DateTimeField(auto_now=True)
    updated_time = models.DateTimeField(auto_now=False, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_by_tmf')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_by_tmf')
    is_enabled = models.BooleanField(default=False)

class WaitingCharge(models.Model):
    price = models.FloatField()
    per_min = models.FloatField()
    created_time = models.DateTimeField(auto_now=True)
    updated_time = models.DateTimeField(auto_now=False, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_by_wc')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_by_wc')
    is_enabled = models.BooleanField(default=False)

