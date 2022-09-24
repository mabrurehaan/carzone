from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.
class Car(models.Model):

    category_choices = (
        ('Jeep', 'Jeep'),
        ('Pickup', 'Pickup'),
        ('Minibus', 'Minibus'),
        ('Truck', 'Truck'),
        ('Car', 'Car'),
        ('Micro', 'Micro'),
        ('Motor-Cycle', 'Motor-Cycle'),
    )

    year_choices = []
    for r in range(2000, (datetime.now().year+1)):
        year_choices.append((r,r))

    features_choices = (
        ('Air Conditioning', 'Air Conditioning'),
        ('Rear View Monitor', 'Rear View Monitor'),
        ('Audio Interface', 'Audio Interface'),
        ('Color LCD multi information display', 'Color LCD multi information display'),
        ('Non-Air Conditioning', 'Non-Air Conditioning'),
        ('USB port and Charging Outlets', 'USB port and Charging Outlets'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    transmission_choices = (
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic'),
    )

    fuel_choices = (
        ('Diesel', 'Diesel'),
        ('Octane', 'Octane'),
        ('Petrol', 'Petrol'),
        ('CNG', 'CNG'),
        ('Others', 'Others'),
    )

    blood_choices = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),

    )

    registration_No = models.CharField(max_length=255)
    type_of_Vehicle = models.CharField(choices=category_choices, max_length=100)
    origin = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    Brand_Name = models.CharField(max_length=100)
    manufacture_Year = models.IntegerField(('year'), choices=year_choices)
    engine_Displacement_CC = models.IntegerField()
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    features = MultiSelectField(choices=features_choices, max_choices=10, max_length=350)
    transmission_Type = models.CharField(choices=transmission_choices, max_length=100)
    seating_Capacity = models.IntegerField()
    engine_No = models.CharField(max_length=100)
    chassis_No = models.CharField(max_length=100)
    fuel_Type = models.CharField(choices=fuel_choices, max_length=10)
    fuel_Tank_Capacity = models.IntegerField()
    name_of_Owner = models.CharField(max_length=100)
    passenger_Information = RichTextField()
    driver_Name = models.CharField(max_length=200)
    blood_Group = models.CharField(choices=blood_choices, max_length=20)
    driver_Photo = models.ImageField(upload_to='driver/%Y/%m/%d/')
    driver_Mobile_No = models.IntegerField()
    licence_No = models.CharField(max_length=150)
    date_of_Birth = models.DateField(max_length=150)
    is_requisition = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.registration_No