from django.db import models

# Create your models here.
class Team(models.Model):
    full_Name = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    Wing_Name = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    mobile_No = models.PositiveIntegerField()
    facebook_Link = models.URLField(max_length=200)
    email_Address = models.EmailField(max_length=254)
    created_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_Name