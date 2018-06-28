from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from .models import Washer, Product, WasherQueue

class WasherAdmin(OrderedModelAdmin):
    list_display = ('washerName', 'move_up_down_links')

class ProductAdmin(OrderedModelAdmin):
    list_display = ('product', 'productType','move_up_down_links')

class WasherQueueAdmin(OrderedModelAdmin):
    list_display = ('washer', 'product', 'volume')

# Register your models here.
admin.site.register(Washer, WasherAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(WasherQueue, WasherQueueAdmin)
