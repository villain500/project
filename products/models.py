from django.db import models

# Create your models here.
class Football(models.Model):
    Product_Description=models.TextField()
    Price=models.FloatField(default=0)
    Product_Image=models.ImageField(upload_to='products/' ,max_length=250,default=None)

class Jersey(models.Model):
    Product_Description=models.TextField()
    Price=models.FloatField(default=0)
    Product_Image=models.ImageField(upload_to='products/' ,max_length=250,default=None)

class Shoe(models.Model):
    Product_Description=models.TextField()
    Price=models.FloatField(default=0)
    Product_Image=models.ImageField(upload_to='products/' ,max_length=250,default=None)

class GP_Glub(models.Model):
    Product_Description=models.TextField()
    Price=models.FloatField(default=0)
    Product_Image=models.ImageField(upload_to='products/' ,max_length=250,default=None)

class Other(models.Model):
    Product_Name=models.CharField(max_length=30,default=None)
    Product_Description=models.TextField()
    Price=models.FloatField(default=0)
    Product_Image=models.ImageField(upload_to='products/' ,max_length=250,default=None)

