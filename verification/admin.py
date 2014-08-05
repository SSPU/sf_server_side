from django.contrib import admin

from suits.models import Suit
from suits.models import Pant
from suits.models import Shirt
from suits.models import Vest

from verification.models import VeriSuit
from verification.models import VeriPant
from verification.models import VeriShirt
from verification.models import VeriVest

class VeriSuitInline(admin.StackedInline):
    model = VeriSuit

class VeriPantInline(admin.StackedInline):
    model = VeriPant

class VeriShirtInline(admin.StackedInline):
    model = VeriShirt

class VeriVestInline(admin.StackedInline):
    model = Vest

def product_username(obj):
    return obj.order.customer.username
product_username.short_description = 'User Name'

def product_order_id(obj):
    return obj.order.id
product_order_id.short_description = 'Order Id'

class SuitAdmin(admin.ModelAdmin):
    inlines = [VeriSuitInline]
    list_display  = ['id', product_username, product_order_id, 'price', 'create_date', 'last_update']
    search_fields = ['order__customer__username', 'order__customer__phone', 'order__customer__email']

class PantAdmin(admin.ModelAdmin):
    inlines = [VeriPantInline]
    list_display  = ['id', product_username, product_order_id, 'price', 'create_date', 'last_update']
    search_fields = ['order__customer__username', 'order__customer__phone', 'order__customer__email']

class ShirtAdmin(admin.ModelAdmin):
    inlines = [VeriShirtInline]
    list_display  = ['id', product_username, product_order_id, 'price', 'create_date', 'last_update']
    search_fields = ['order__customer__username', 'order__customer__phone', 'order__customer__email']

class VestAdmin(admin.ModelAdmin):
    inlines = [VeriVestInline]
    list_display  = ['id', product_username, product_order_id, 'price', 'create_date', 'last_update']
    search_fields = ['order__customer__username', 'order__customer__phone', 'order__customer__email']

admin.site.register(Suit, SuitAdmin)
admin.site.register(Pant, PantAdmin)
admin.site.register(Shirt, ShirtAdmin)
admin.site.register(Vest, VestAdmin)
