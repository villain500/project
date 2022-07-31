from django.contrib import admin
from adminsite.models import Slider
# from adminsite.models import Site_User
# Register your models here.

# Slider
class SliderAdmin(admin.ModelAdmin):
    list_display=('Slider_Title','Slider_Description','Slider_Image')

admin.site.register(Slider,SliderAdmin)

