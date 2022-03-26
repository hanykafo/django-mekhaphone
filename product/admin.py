from re import search
from django.contrib import admin
from .models import *

# Add Panel your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'item_full_name',
        'camp_id',
        'class_d_no',
        'saling_price',
    ]
    list_editable = [
        'camp_id',
        'class_d_no',
        'saling_price',
    ]
    search_fields = [
        'item_full_name'
    ]
    list_filter = [
        'camp_id'
    ]
# Register your models here.
admin.site.register(ComStClassMaster)
admin.site.register(ComStClassDetails)
admin.site.register(ComStCampProduced)
admin.site.register(ComStUnits)
admin.site.register(ComStItemColors)
admin.site.register(ComStProducts,ProductAdmin)
admin.site.register(ComStItemImage)
admin.site.register(ComStAlternative_Pro)
admin.site.register(ComStAccessories_pro)

admin.site.site_header = 'Mekha Phone'
admin.site.site_title = 'Mekha Phone'
