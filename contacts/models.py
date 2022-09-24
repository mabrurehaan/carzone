from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    car_id = models.IntegerField()
    customer_need = models.CharField(max_length=100)
    car_title = models.CharField(max_length=100)
    start_date = models.DateField(max_length=150)
    end_date = models.DateField(max_length=150)
    destination = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    requisition_form = models.ImageField(upload_to='requisition/')
    message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    create_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.phone
