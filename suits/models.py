from django.db import models

from django.utils import timezone


class Customer(models.Model):
    GENDERS = (
        ('Male',   'Male'),
        ('Female', 'Female'),
    )
    username = models.CharField(max_length=20)
    password = models.TextField()
    phone    = models.CharField(max_length=20)
    email    = models.CharField(max_length=50)
    gender   = models.CharField(max_length=10, choices=GENDERS, default='Male')
    age      = models.IntegerField(default=0)
    weight   = models.DecimalField(max_digits=5, decimal_places=2)
    height   = models.DecimalField(max_digits=5, decimal_places=2)

    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.username

class Order(models.Model):
    ORDER_STATUS = (
        ('Pending Editing','Pending Editing'),
        ('Pending Payment','Pending Payment'),
        ('Ready to Work',  'Ready to Work'),
        ('Working',        'Working'),
        ('Delivering',     'Delivering'),
        ('Complete',       'Complete'),
    )

    customer = models.ForeignKey(Customer)
    price    = models.DecimalField(max_digits=8, decimal_places=2)
    status   = models.CharField(max_length=20, choices=ORDER_STATUS, default='Pending Editing')

    remark   = models.TextField(default='none')

    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
#       return self.customer.username + self.create_date.strftime(' | %d-%b-%Y %H-%M')
        return self.customer.username + ' | Order# ' + str(self.id)

class Body(models.Model):
    SHOULDER_TYPE = (
        ('Normal',   'Normal'),
        ('Square',   'Square'),
        ('Slopping', 'Sloping'),
    )
    order             = models.OneToOneField(Order)
    neck              = models.DecimalField(max_digits=5, decimal_places=2)
    shoulder          = models.DecimalField(max_digits=5, decimal_places=2)
    suit_shirt_length = models.DecimalField(max_digits=5, decimal_places=2)
    chest_1           = models.DecimalField(max_digits=5, decimal_places=2)
    chest_2           = models.DecimalField(max_digits=5, decimal_places=2)
    chest_3           = models.DecimalField(max_digits=5, decimal_places=2)
    chest_4           = models.DecimalField(max_digits=5, decimal_places=2)
    waist_1           = models.DecimalField(max_digits=5, decimal_places=2)
    waist_2           = models.DecimalField(max_digits=5, decimal_places=2)
    sleeve_length     = models.DecimalField(max_digits=5, decimal_places=2)
    bicep             = models.DecimalField(max_digits=5, decimal_places=2)
    wrist             = models.DecimalField(max_digits=5, decimal_places=2)
    crotch            = models.DecimalField(max_digits=5, decimal_places=2)
    hip               = models.DecimalField(max_digits=5, decimal_places=2)
    pants_length      = models.DecimalField(max_digits=5, decimal_places=2)
    high_thigh        = models.DecimalField(max_digits=5, decimal_places=2)
    mid_thigh         = models.DecimalField(max_digits=5, decimal_places=2)
    calf              = models.DecimalField(max_digits=5, decimal_places=2)
    shoulder_type     = models.CharField(max_length=10, choices=SHOULDER_TYPE, default='Normal')

    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.order.id) + ' | Body# ' + str(self.id)

class CustSuit(models.Model):
    order             = models.OneToOneField(Order)

    shoulder          = models.DecimalField(max_digits=5, decimal_places=2)
    back_length       = models.DecimalField(max_digits=5, decimal_places=2)
    back_width        = models.DecimalField(max_digits=5, decimal_places=2)
    back_waist_width  = models.DecimalField(max_digits=5, decimal_places=2)
    back_hip_width    = models.DecimalField(max_digits=5, decimal_places=2)
    chest_width       = models.DecimalField(max_digits=5, decimal_places=2)
    waist_1           = models.DecimalField(max_digits=5, decimal_places=2)
    waist_2           = models.DecimalField(max_digits=5, decimal_places=2)
    front_hip_width   = models.DecimalField(max_digits=5, decimal_places=2)
    sleeve_outseam    = models.DecimalField(max_digits=5, decimal_places=2)
    sleeve_width_1    = models.DecimalField(max_digits=5, decimal_places=2)
    sleeve_width_2    = models.DecimalField(max_digits=5, decimal_places=2)
    bicep_girth       = models.DecimalField(max_digits=5, decimal_places=2)
    cuff_girth        = models.DecimalField(max_digits=5, decimal_places=2)


    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.order.id) + ' | Customized Suit# ' + str(self.id)

class CustPant(models.Model):
    order             = models.OneToOneField(Order)

    waist_girth       = models.DecimalField(max_digits=5, decimal_places=2)
    hip_girth         = models.DecimalField(max_digits=5, decimal_places=2)
    thigh             = models.DecimalField(max_digits=5, decimal_places=2)
    knee_girth        = models.DecimalField(max_digits=5, decimal_places=2)
    ankel_girth       = models.DecimalField(max_digits=5, decimal_places=2)
    pant_outseam      = models.DecimalField(max_digits=5, decimal_places=2)
    front_crotch      = models.DecimalField(max_digits=5, decimal_places=2)
    back_crotch       = models.DecimalField(max_digits=5, decimal_places=2)

    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.order.id) + ' | Customized Pant# ' + str(self.id)

class CustShirt(models.Model):
    order             = models.OneToOneField(Order)

    collar            = models.DecimalField(max_digits=5, decimal_places=2)
    half_chest_1      = models.DecimalField(max_digits=5, decimal_places=2)
    half_chest_2      = models.DecimalField(max_digits=5, decimal_places=2)
    half_check_3      = models.DecimalField(max_digits=5, decimal_places=2)
    hip_girth         = models.DecimalField(max_digits=5, decimal_places=2)
    front_length      = models.DecimalField(max_digits=5, decimal_places=2)
    shoulder          = models.DecimalField(max_digits=5, decimal_places=2)
    back_length       = models.DecimalField(max_digits=5, decimal_places=2)
    sleeve_outseam    = models.DecimalField(max_digits=5, decimal_places=2)
    sleeve_girth_1    = models.DecimalField(max_digits=5, decimal_places=2)
    sleeve_girth_2    = models.DecimalField(max_digits=5, decimal_places=2)
    bicep_girth       = models.DecimalField(max_digits=5, decimal_places=2)
    cuff_girth        = models.DecimalField(max_digits=5, decimal_places=2)

    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.order.id) + ' | Customized Shirt# ' + str(self.id)

class CustVest(models.Model):
    order             = models.OneToOneField(Order)

    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.order.id) + ' | Customized Vest# ' + str(self.id)


class Material(models.Model):
    MATERIAL_TYPE = (
        ('Outer Fabric',  'Outer Fabric'),
        ('Lining Fabric', 'Lining Fabric'),
        ('Shirt Fabric',  'Shirt Fabric')
    )
    name            = models.CharField(max_length=100)
    material_type   = models.CharField(max_length=20, choices=MATERIAL_TYPE, default='Outer Fabric')
    material_status = models.BooleanField(default=True)
    remark          = models.TextField(default='none')

    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

class Suit(models.Model):
    FIT_STYLE = (
        ('Regular', 'Regular'),
        ('Loose',   'Loose'),
        ('Slim',    'Slim'),
    )
    LAPEL_STYLE = (
        ('Notched',    'Notched'),
        ('Peak',       'Peak'),
        ('Fish Mouse', 'Fish Mouse'),
        ('Shawl',      'Shawl'),
    )
    LAPEL_WIDTH = (
        ('Normal', 'Normal'),
        ('Wide',   'Wide'),
    )
    COLLAR_SATIN_WIDTH = (
        ('Full', 'Full'),
        ('Edge', 'Edge'),
        ('None', 'None'),
    )
    LAPEL_SATIN_WIDTH = (
        ('Full',       'Full'),
        ('Edge(wide)', 'Edge(wide)'),
        ('Edge(slim)', 'Edge(slim)'),
        ('none',       'none'),
    )
    SATIN_COLOUR = (
        ('Black', 'Black'),
        ('Navy',  'Navy'),
        ('White', 'White'),
    )
    COLLAR_BACK_FELT_COLOUR = (
        ('Match Fabric', 'Match Fabric'),
        ('Blue',         'Blue'),
        ('Pink',         'Pink'),
        ('Purple',       'Purple'),
        ('Red',          'Red'),
    )
    BREAST_STYLE = (
        ('Single', 'Single'),
        ('Double', 'Double'),
    )
    BREAST_BUTTON_NUM = (
        ('1 Button',            '1 Button'),
        ('2 Button (1 fasten)', '2 Button (1 fasten)'),
        ('2 Button (2 fasten)', '2 Button (2 fasten)'),
        ('3 Button (2 fasten)', '3 Button (2 fasten)'),
    )
    FRONT_POCKET_NUM = (
        ('2 Pockets', '2 Pockets'),
        ('3 Pockets', '3 Pockets'),
    )
    VENT_STYLE = (
        ('Single - center', 'Single - center'),
        ('Double - side',   'Double - side'),
    )
    STITCH_STYLE = (
        ('None',      'None'),
        ('White',     'White'),
        ('Stitching', 'Stitching'),
    )
    MONOGRAM_STYLE = (
        ('None',        'None'),
        ('Right Chest', 'Right Chest'),
        ('Left Chest',  'Left Chest'),
    )

    order                   = models.ForeignKey(Order)
#   customer                = models.ForeignKey(Customer)

    outer_fabric            = models.ForeignKey(Material, related_name='outer_fabric')
    lining_fabric           = models.ForeignKey(Material, related_name='lining_fabric')
    fit                     = models.CharField(max_length=10, choices=FIT_STYLE, default='Regular')

    lapel_style             = models.CharField(max_length=10, choices=LAPEL_STYLE, default='Notched')
    lapel_width             = models.CharField(max_length=10, choices=LAPEL_WIDTH, default='Normal')
    collar_satin_width      = models.CharField(max_length=10, choices=COLLAR_SATIN_WIDTH, default='Full')
    lapel_satin_width       = models.CharField(max_length=20, choices=LAPEL_SATIN_WIDTH, default='Full')
    satin_colour            = models.CharField(max_length=20, choices=SATIN_COLOUR, default='Black')
    collar_back_felt_colour = models.CharField(max_length=20, choices=COLLAR_BACK_FELT_COLOUR, default='Match Fabric')

    breast_style            = models.CharField(max_length=10, choices=BREAST_STYLE, default='Single')
    breast_button_number    = models.CharField(max_length=20, choices=BREAST_BUTTON_NUM, default='2 Button (1 fasten)')
#   breast_button_style
    front_pocket_number     = models.CharField(max_length=10, choices=FRONT_POCKET_NUM, default='2 Pockets')

    vent                    = models.CharField(max_length=20, choices=VENT_STYLE, default='Single - center')
    outer_pick_stitch       = models.CharField(max_length=20, choices=STITCH_STYLE, default='None')
    monogram_style          = models.CharField(max_length=20, choices=MONOGRAM_STYLE, default='None')
    monogram_text           = models.TextField(default='none')

    remark      = models.TextField(default='none')
    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return 'Suit#' + str(self.id)

class Pant(models.Model):
    BELT_LOOPS_STYLE = (
        ('With Belt Loops','With Belt Loops'),
        ('No Belt Loops',  'No Belt Loops'),
    )
    POCKET_STYLE = (
        ('Vertical',  'Vertical'),
        ('Horizontal','Horizontal'),
        ('Slanted',   'Slanted'),
    )
    PLEATS_STYLE = (
        ('Single','Single'),
        ('Double','Double'),
        ('None',  'None'),
    )
    BACK_POCKET_STYLE = (
        ('Left', 'Left'),
        ('Right','Right'),
        ('Both', 'Both'),
        ('None', 'None'),
    )
    LINING_STYLE = (
        ('None','None'),
        ('Half','Half'),
        ('Full','Full'),
    )

    order            = models.ForeignKey(Order)

    belt_loops       = models.CharField(max_length=20, choices=BELT_LOOPS_STYLE, default='With Belt Loops')
    pocket_opening   = models.CharField(max_length=20, choices=POCKET_STYLE, default='Vertical')
    pleats           = models.CharField(max_length=10, choices=PLEATS_STYLE, default='Single')
    back_pocket      = models.CharField(max_length=10, choices=BACK_POCKET_STYLE, default='Right')
    lining_style     = models.CharField(max_length=10, choices=LINING_STYLE, default='None')

    remark      = models.TextField(default='none')
    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return 'Pant#' + str(self.id)

class Shirt(models.Model):
    FIT_STYLE = (
        ('Regular', 'Regular'),
        ('Loose',   'Loose'),
        ('Slim',    'Slim'),
    )
    COLLAR_STYLE = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    )
    COLLAR_POINT = (
        ('Fixed Plastic Collar Stay','Fixed Plastic Collar Stay'),
        ('Removable Collar Stay',    'Removable Collar Stay'),
        ('Button Down',              'Button Down'),
    )
    COLOUR_CONTRAST = (
        ('Same as Shirt','Same as Shirt'),
        ('Full',         'Full'),
        ('Inner Only',   'Inner Only'),
    )
    PLEATS_STYLE = (
        ('None',                'None'),
        ('Single Centre Pleats','Single Centre Pleats'),
        ('Double Side Pleats',  'Double Side Pleats'),
    )
    PICK_STITCHING_STYLE = (
        ('None','None'),
        ('Matching Colour','Match Colour'),
    )
    CUFF_BUTTON_NUMBER = (
        ('1','1'),
        ('2','2'),
    )
    CUFF_STYLE = (
        ('Square','Square'),
        ('Angled','Angled'),
        ('Round', 'Round'),
        ('French','French'),
    )
    FRONT_BUTTON_STYLE = (
        ('Plain Front',   'Plain Front'),
        ('Placket Front', 'Placket Front'),
        ('Hidden Buttons','Hidden Buttons'),
    )
    FRONT_BUTTON_COLOUR = (
        ('White','White'),
        ('Black','Black'),
        ('Blue', 'Blue'),
        ('Red',  'Red'),
    )
    FRONT_POCKET_STYLE = (
        ('None',     'None'),
        ('1 Pocket', '1 Pocket'),
        ('2 Pockets','2 Pockets'),
    )
    SLEEVE_STYLE = (
        ('Long Sleeve', 'Long Sleeve'),
        ('Short Sleeve','Short Sleeve'),
    )

    order                  = models.ForeignKey(Order)
    shirt_fabric           = models.ForeignKey(Material, related_name='shirt_fabric')

    fit                    = models.CharField(max_length=10, choices=FIT_STYLE, default='Regular')
    collar_style           = models.CharField(max_length=1,  choices=COLLAR_STYLE, default='1')
    collar_point           = models.CharField(max_length=30, choices=COLLAR_POINT, default='Removable Collar Stay')
    collar_colour_contrast = models.CharField(max_length=20, choices=COLOUR_CONTRAST, default='Same as Shirt')
    collar_colour          = models.CharField(max_length=30, default='none')
    pleats                 = models.CharField(max_length=20, choices=PLEATS_STYLE, default='None')
    pick_stitching         = models.CharField(max_length=20, choices=PICK_STITCHING_STYLE, default='None')
    cuff_button_number     = models.CharField(max_length=1,  choices=CUFF_BUTTON_NUMBER, default='1')
    cuff_collour_contrast  = models.CharField(max_length=20, choices=COLOUR_CONTRAST, default='Same as Shirt')
    cuff_colour            = models.CharField(max_length=30, default='none')
    cuff_style             = models.CharField(max_length=20, choices=CUFF_STYLE, default='Square')
    front_button           = models.CharField(max_length=20, choices=FRONT_BUTTON_STYLE, default='Plain Front')
    front_button_colour    = models.CharField(max_length=20, choices=FRONT_BUTTON_COLOUR, default='White')
    pocket                 = models.CharField(max_length=20, choices=FRONT_POCKET_STYLE, default='None')
    sleeve_style           = models.CharField(max_length=20, choices=SLEEVE_STYLE, default='Long Sleeve')

    remark      = models.TextField(default='none')
    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return 'Shirt#' + str(self.id)

class Vest(models.Model):
    FRONT_BUTTON_NUMBER = (
        ('3 Buttons','3 Buttons'),
        ('4 Buttons','4 Buttons'),
        ('5 Buttons','5 Buttons'),
    )
    FRONT_BUTTON_STYLE = (
        ('Same as Suit','Same as Suit'),
        ('Nut',         'Nut'),
        ('Horn',        'Horn'),
        ('Shell',       'Shell'),
        ('Fabric',      'Fabric'),
        ('Satin',       'Satin'),
        ('Brass',       'Brass'),
        ('Plastic',     'Plastic'),
    )
    POCKET_STYLE = (
        ('Normal (x2)', 'Normal (x2)'),
        ('None',        'None'),
    )
    POCKETS_SATIN_COLOUR = (
        ('No Satin','No Satin'),
        ('Black',   'Black'),
        ('Navy',    'Navy'),
        ('White',   'White'),
    )
    BACK_MATERIAL = (
        ('Lining','Lining'),
        ('Fabric','Fabric'),
    )
    STRAP = (
        ('Strap','Strap'),
        ('None', 'None'),
    )

    order                  = models.ForeignKey(Order)

    front_button_number    = models.CharField(max_length=20, choices=FRONT_BUTTON_NUMBER, default='4 Buttons')
    front_button_style     = models.CharField(max_length=20, choices=FRONT_BUTTON_STYLE, default='Same as Suit')
    pocket                 = models.CharField(max_length=20, choices=POCKET_STYLE, default='Normal (x2)')
    pockets_satin_colour   = models.CharField(max_length=20, choices=POCKETS_SATIN_COLOUR, default='No Satin')
    back_material          = models.CharField(max_length=20, choices=BACK_MATERIAL, default='Lining')
    strap                  = models.CharField(max_length=20, choices=STRAP, default='Strap')

    remark      = models.TextField(default='none')
    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return 'Vest#' + str(self.id)

