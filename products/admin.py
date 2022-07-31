from django.contrib import admin
from products.models import Football
from products.models import Jersey
from products.models import Shoe
from products.models import GP_Glub
from products.models import Other
# Register your models here.
class FootBallAdmin(admin.ModelAdmin):
    list_display=('Product_Description','Price','Product_Image')
admin.site.register(Football,FootBallAdmin)

class JerseyAdmin(admin.ModelAdmin):
    list_display=('Product_Description','Price','Product_Image')
admin.site.register(Jersey,JerseyAdmin)

class ShoesAdmin(admin.ModelAdmin):
    list_display=('Product_Description','Price','Product_Image')
admin.site.register(Shoe,ShoesAdmin)

class GP_GlubsAdmin(admin.ModelAdmin):
    list_display=('Product_Description','Price','Product_Image')
admin.site.register(GP_Glub,GP_GlubsAdmin)

class OthersAdmin(admin.ModelAdmin):
    list_display=('Product_Name','Product_Description','Price','Product_Image')
admin.site.register(Other,OthersAdmin)

