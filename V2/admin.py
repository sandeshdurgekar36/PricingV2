from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

@admin.register(DistanceBasePrice)
class DistanceBasePrice(ImportExportModelAdmin):
    list_display = ['id', 'price', 'km_value', 'day', 'created_time', 'updated_time', 'created_by', 'updated_by', 'is_enabled']

@admin.register(DistanceAdditionalPrice)
class DistanceAdditionalPrice(ImportExportModelAdmin):
    list_display = ['id', 'price', 'km_value', 'created_time', 'updated_time', 'created_by', 'updated_by', 'is_enabled']

@admin.register(TimeMultiplierFactor)
class TimeMultiplierFactor(ImportExportModelAdmin):
    list_display = ['id', 'price', 'hours', 'created_time', 'updated_time', 'created_by', 'updated_by', 'is_enabled']

@admin.register(WaitingCharge)
class WaitingCharge(ImportExportModelAdmin):
    list_display = ['id', 'price', 'per_min', 'created_time', 'updated_time', 'created_by', 'updated_by', 'is_enabled']