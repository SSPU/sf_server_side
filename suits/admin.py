from django.contrib import admin

from suits.models import Customer
from suits.models import Order
from suits.models import Body
from suits.models import CustSuit
from suits.models import CustPant
from suits.models import CustShirt
from suits.models import CustVest

from suits.models import Suit
from suits.models import Pant
from suits.models import Shirt
from suits.models import Vest
from suits.models import Material

class OrderInline(admin.StackedInline):
    model = Order
    extra = 1
    radio_fields = {'status'       : admin.HORIZONTAL}

class BodyInline(admin.StackedInline):
    model = Body
    radio_fields = {'shoulder_type': admin.HORIZONTAL}

class CustSuitInline(admin.StackedInline):
    model = CustSuit
    extra = 0

class CustPantInline(admin.StackedInline):
    model = CustPant
    extra = 0

class CustShirtInline(admin.StackedInline):
    model = CustShirt
    extra = 0

class CustVestInline(admin.StackedInline):
    model = CustVest
    extra = 0

class SuitInline(admin.StackedInline):
    model = Suit
    extra = 0
    radio_fields = {
        'fit'                     : admin.HORIZONTAL,
        'lapel_style'             : admin.HORIZONTAL,
        'lapel_width'             : admin.HORIZONTAL,
        'collar_satin_width'      : admin.HORIZONTAL,
        'lapel_satin_width'       : admin.HORIZONTAL,
        'satin_colour'            : admin.HORIZONTAL,
        'collar_back_felt_colour' : admin.HORIZONTAL,
        'breast_style'            : admin.HORIZONTAL,
        'breast_button_number'    : admin.HORIZONTAL,
        'front_pocket_number'     : admin.HORIZONTAL,
        'vent'                    : admin.HORIZONTAL,
        'outer_pick_stitch'       : admin.HORIZONTAL,
        'monogram_style'          : admin.HORIZONTAL,
    }

class PantInline(admin.StackedInline):
    model = Pant
    extra = 0
    radio_fields = {
        'belt_loops'              : admin.HORIZONTAL,
        'pocket_opening'          : admin.HORIZONTAL,
        'pleats'                  : admin.HORIZONTAL,
        'back_pocket'             : admin.HORIZONTAL,
        'lining_style'            : admin.HORIZONTAL,
    }

class ShirtInline(admin.StackedInline):
    model = Shirt
    extra = 0
    radio_fields = {
        'fit'                     : admin.HORIZONTAL,
        'collar_style'            : admin.HORIZONTAL,
        'collar_point'            : admin.HORIZONTAL,
        'collar_colour_contrast'  : admin.HORIZONTAL,
        'pleats'                  : admin.HORIZONTAL,
        'pick_stitching'          : admin.HORIZONTAL,
        'cuff_button_number'      : admin.HORIZONTAL,
        'cuff_collour_contrast'   : admin.HORIZONTAL,
        'cuff_style'              : admin.HORIZONTAL,
        'front_button'            : admin.HORIZONTAL,
        'front_button_colour'     : admin.HORIZONTAL,
        'pocket'                  : admin.HORIZONTAL,
        'sleeve_style'            : admin.HORIZONTAL,
    }

class VestInline(admin.StackedInline):
    model = Vest
    extra = 0
    radio_fields = {
        'front_button_number'    : admin.HORIZONTAL,
        'front_button_style'     : admin.HORIZONTAL,
        'pocket'                 : admin.HORIZONTAL,
        'pockets_satin_colour'   : admin.HORIZONTAL,
        'back_material'          : admin.HORIZONTAL,
        'strap'                  : admin.HORIZONTAL,
    }

class CustomerAdmin(admin.ModelAdmin):
    inlines = [OrderInline,
               ]
    list_display  = ['username', 'phone', 'email', 'gender', 'age']
    search_fields = ['username', 'phone', 'email']
    radio_fields  = {'gender'    : admin.HORIZONTAL}


class OrderAdmin(admin.ModelAdmin):
    inlines = [BodyInline,
               CustSuitInline,
               CustPantInline,
               CustShirtInline,
               CustVestInline,
               SuitInline,
               PantInline,
               ShirtInline,
               VestInline,
               ]
    list_display  = ['__unicode__', 'price', 'create_date', 'last_update']
    search_fields = ['customer__username', 'customer__phone', 'customer__email']
    radio_fields  = {'status'    : admin.HORIZONTAL}
    raw_id_fields = ['customer']

class MaterialAdmin(admin.ModelAdmin):
    list_display  = ['material_type', 'name', 'material_status', 'remark']
    radio_fields  = {'material_type': admin.HORIZONTAL}


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Material, MaterialAdmin)

admin.site.register(Suit)
admin.site.register(Pant)
admin.site.register(Shirt)
admin.site.register(Vest)
