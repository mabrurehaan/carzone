from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.car_photo.url))

    thumbnail.short_description = 'Car Image'
    list_display = ('id','thumbnail','registration_No', 'driver_Name', 'color', 'Brand_Name', 'manufacture_Year', 'type_of_Vehicle', 'fuel_Type', 'is_requisition')
    list_display_links = ('id', 'thumbnail', 'registration_No')
    list_editable = ('is_requisition',)
    search_fields = ('id', 'registration_No', 'driver_Name', 'seating_Capacity','fuel_Type')
    list_filter = ('Brand_Name', 'transmission_Type', 'type_of_Vehicle', 'fuel_Type')
admin.site.register(Car, CarAdmin)