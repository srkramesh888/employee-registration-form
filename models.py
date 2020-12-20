from django.db import models

# Create your models here.
class Ram(models.Model):
    Name=models.CharField(max_length=200)
    Password=models.CharField(max_length=200)
    Email_ID=models.EmailField()
    Gender=models.CharField(max_length=200)
    Date_of_Birth=models.CharField(max_length=200)
    Address=models.CharField(max_length=200)
    Phone_Number=models.CharField(max_length=200)
    Photo=models.ImageField(upload_to="media",null=True,blank=True)
class Meta:
    db_table="try_ram"





