from django.db import models


# Create your models here.

# slider
class Slider(models.Model):
    Slider_Title=models.CharField(max_length=100)
    Slider_Description=models.TextField()
    Slider_Image=models.ImageField(upload_to='sliders/' ,max_length=250,default=None)

    def __str__(self) -> str:
        return self.Slider_Title

    

