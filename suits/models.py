from django.db import models

from django.utils import timezone


class Customer(models.Model):
    GENDERS = (
        ('Male',   'Male'),
        ('Female', 'Female'),
    )
    username = models.CharField(max_length=20, unique=True)
    password = models.TextField()
    phone    = models.CharField(max_length=20)
    email    = models.CharField(max_length=50, unique=True)
    gender   = models.CharField(max_length=10, choices=GENDERS, default='Male')

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
    FIT_STYLE = (
        ('Regular', 'Regular'),
        ('Loose',   'Loose'),
        ('Slim',    'Slim'),
    )
    SHOULDER_TYPE = (
        ('Normal',   'Normal'),
        ('Square',   'Square'),
        ('Slopping', 'Sloping'),
    )
    order             = models.OneToOneField(Order)
    neck              = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='B100 / Neck')
    shoulder          = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='B200 / Shoulder')
    front_length      = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='B300 / Front Length (to root of thumb)')
    chest_1           = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='B400 / Chest (under armpit / nipple)')
    chest_2           = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='B500 / Chest (bottom of rib cage)')
    waist_1           = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='B600 / Waist (belly button)')
    waist_2           = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='B700 / Waist (belt)')
    front_width       = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='B800 / Front Width (under armpit / nipple)')
    back_width        = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='B900 / Back Width (under armpit / nipple)')
    crotch            = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='B1000 / Crotch')
    hip               = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='B1100 / Hip')
    bicep             = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='B1300 / Bicep')
    wrist             = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='B1400 / Wrist')
    waist_3           = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='750 / Waist for Pants')
    high_thigh        = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='B1500 / High Thigh')
    mid_thigh         = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='B1600 / Mid Thigh')
    calf              = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='B1700 / Calf')
    shoulder_type     = models.CharField(max_length=10, choices=SHOULDER_TYPE, default='Normal', verbose_name='B2000 / Shoulder Type')
    height            = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='B2001 / Height')
    weight            = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='B2002 / Weight')
    birth_year        = models.IntegerField(default=0, verbose_name='B2003 / Year of Birth')
    fit               = models.CharField(max_length=10, choices=FIT_STYLE, default='Regular', verbose_name='B2005 / Fit Preference')

    remark      = models.TextField(default='none')
    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.order.id) + ' | Body# ' + str(self.id)

class CustSuit(models.Model):
    order             = models.OneToOneField(Order)

    shoulder          = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PJ0010 / Shoulder')
    back_length       = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PJ0020 / Back Length')
    back_width        = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PJ0030 / Back Width (under armpit)')
    back_waist_width  = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PJ0040 / Back Waist Width')
    back_hip_width    = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PJ0050 / Back Hip Width')
    chest_width       = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PJ0110 / Chest Width (under armpit)')
    waist_1           = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PJ0120 / Waist (1st button)')
    waist_2           = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PJ0130 / Waist (last button)')
    front_hip_width   = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PJ0140 / Front Hip Width')
    sleeve_outseam    = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PJ0210 / Sleeve Outseam')
    sleeve_width_1    = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PJ0220 / Sleeve Opening Width')
    sleeve_width_2    = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PJ0230 / Sleeve Opening Width (90d to Sleeve Outseam)')
    bicep_girth       = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PJ0240 / Bicep Girth')
    cuff_girth        = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PJ0250 / Cuff Girth')

    remark      = models.TextField(default='none')
    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.order.id) + ' | Customized Suit# ' + str(self.id)

class CustPant(models.Model):
    order             = models.OneToOneField(Order)

    waist_girth       = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PP0100 / Waist Girth')
    hip_girth         = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PP0110 / Hip Girth')
    thigh             = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PP0120 / Thigh (below crotch)')
    knee_girth        = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PP0130 / Knee Girth')
    ankel_girth       = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PP0140 / Ankel Girth')
    pant_outseam      = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PP0200 / Pant Outseam')
    front_crotch      = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PP0300 / Front Crotch Length')
    back_crotch       = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PP0310 / Back Crotch Length')

    remark      = models.TextField(default='none')
    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.order.id) + ' | Customized Pant# ' + str(self.id)

class CustShirt(models.Model):
    order             = models.OneToOneField(Order)

    collar            = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PH0100 / Collar')
    half_chest_1      = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PH0200 / Half Chest (under armpit)')
    half_chest_2      = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PH0210 / Half Chest (2nd button beneath armpit)')
    half_check_3      = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PH0220 / Half Chest (last button)')
    hip_girth         = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PH0230 / Hip Girth')
    front_length      = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PH0240 / Front Length')
    shoulder          = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PH0300 / Shoulder')
    back_length       = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PH0310 / Back Length')
    sleeve_outseam    = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PH0400 / Sleeve Outseam')
    sleeve_girth_1    = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PH0410 / Sleeve Opening Girth')
    sleeve_girth_2    = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PH0420 / Sleeve Opening Girth (90d to Sleeve Outseam)')
    bicep_girth       = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PH0430 / Bicep Girth')
    cuff_girth        = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='PH0440 / Cuff Girth')

    remark      = models.TextField(default='none')
    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.order.id) + ' | Customized Shirt# ' + str(self.id)

class CustVest(models.Model):
    order             = models.OneToOneField(Order)

    remark      = models.TextField(default='none')
    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.order.id) + ' | Customized Vest# ' + str(self.id)


class Material(models.Model):
    MATERIAL_TYPE = (
        ('Outer Fabric',  'Outer Fabric'),
        ('Lining Fabric', 'Lining Fabric'),
        ('Shirt Fabric',  'Shirt Fabric'),
        ('Suit Buttons',  'Suit Buttons'),
        ('Shirt Buttons', 'Shirt Buttons'),
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
    SHOULDER_PADDING = (
        ('None',         'None'),
        ('With Padding', 'With Padding'),
    )
    ELBOW_PAD = (
        ('None',            'None'),
        ('With elbow pads', 'With Elbow Pads'),
    )
    SLEEVE_BH = (
        ('Non Functional', 'Non Functional'),
        ('Functional',     'Functional'),
    )
    SLEEVE_BS = (
        ('Same as Front Button','Same as Front Button'),
    )
    VENT_STYLE = (
        ('Single - center', 'Single - center'),
        ('Double - side',   'Double - side'),
        ('No Vents',        'No Vents'),
    )
    STITCH_STYLE = (
        ('None',      'None'),
        ('White',     'White'),
    )
    MONOGRAM_STYLE = (
        ('None',        'None'),
        ('Right Chest', 'Right Chest'),
        ('Left Chest',  'Left Chest'),
    )

    order                   = models.ForeignKey(Order)
#   customer                = models.ForeignKey(Customer)

    fit                     = models.CharField(max_length=10, choices=FIT_STYLE, default='Regular', verbose_name='S0001 / Fit Style')
    outer_fabric            = models.ForeignKey(Material, related_name='outer_fabric',
                              limit_choices_to={'material_type' : 'Outer Fabric'}, verbose_name='S0002 / Suit Fabric')
    lining_fabric           = models.ForeignKey(Material, related_name='lining_fabric',
                              limit_choices_to={'material_type' : 'Lining Fabric'}, verbose_name='S0003 / Suit Lining')
    suit_buttons            = models.ForeignKey(Material, related_name='suit_buttons',
                              limit_choices_to={'material_type' : 'Suit Buttons'}, verbose_name='S0004 / Suit Buttons')

    lapel_style             = models.CharField(max_length=10, choices=LAPEL_STYLE, default='Notched', verbose_name='S0100 / Lapel Style')
    lapel_width             = models.CharField(max_length=10, choices=LAPEL_WIDTH, default='Normal', verbose_name='S0101 / Lapel Width')
    collar_satin_width      = models.CharField(max_length=10, choices=COLLAR_SATIN_WIDTH, default='Full', verbose_name='S0110 / Collar Satin Width')
    lapel_satin_width       = models.CharField(max_length=20, choices=LAPEL_SATIN_WIDTH, default='Full', verbose_name='S0111 / Lapel Satin Width')
    satin_colour            = models.CharField(max_length=20, choices=SATIN_COLOUR, default='Black', verbose_name='S0112 / Satin Colour')
    collar_back_felt_colour = models.CharField(max_length=20, choices=COLLAR_BACK_FELT_COLOUR, default='Match Fabric', verbose_name='S0130 / Collar Back Felt Colour')

    breast_style            = models.CharField(max_length=10, choices=BREAST_STYLE, default='Single', verbose_name='S0200 / Breast Style')
    breast_button_number    = models.CharField(max_length=20, choices=BREAST_BUTTON_NUM, default='2 Button (1 fasten)', verbose_name='S0201 / Breast Button Number')
    breast_button_style     = models.TextField(default='none', verbose_name='S0202 / Breast Button Style')
    front_pocket_number     = models.CharField(max_length=10, choices=FRONT_POCKET_NUM, default='2 Pockets', verbose_name='S0250 / Front Pocket Number')
    shoulder_padding        = models.CharField(max_length=20, choices=SHOULDER_PADDING, default='None', verbose_name='S0300 / Shoulder Padding')
    elbow_pad               = models.CharField(max_length=20, choices=ELBOW_PAD, default='None', verbose_name='S0301 / Elbow Pads')
    sleeve_buttonholes      = models.CharField(max_length=20, choices=SLEEVE_BH, default='Non Functional', verbose_name='S0302 / Sleeve Buttonholes')
    sleeve_button_style     = models.CharField(max_length=20, choices=SLEEVE_BS, default='Same as Front Button', verbose_name='S0303 / Sleeve Button Style')

    vent                    = models.CharField(max_length=20, choices=VENT_STYLE, default='Single - center', verbose_name='S0500 / Vents')
    outer_pick_stitch       = models.CharField(max_length=20, choices=STITCH_STYLE, default='None', verbose_name='S0600 / Outer Pick Stitch')
    monogram_style          = models.CharField(max_length=20, choices=MONOGRAM_STYLE, default='None', verbose_name='S1100 / Monogram')
    monogram_text           = models.TextField(default='none')

    price       = models.DecimalField(max_digits=8, decimal_places=2)
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
    LENGTH_STYLE = (
        ('Above Ankel', 'Above Ankel'),
        ('At Ankel',    'At Ankel'),
    )
    LOWER_LEG_STYLE = (
        ('Consistent with Fit Style', 'Consistent with Fit Style'),
        ('Additional Slimming',       'Additional Slimming'),
    )

    order            = models.ForeignKey(Order)

    belt_loops       = models.CharField(max_length=20, choices=BELT_LOOPS_STYLE, default='With Belt Loops', verbose_name='P0100 / Belt Loops')
    pocket_opening   = models.CharField(max_length=20, choices=POCKET_STYLE, default='Vertical', verbose_name='P0200 / Pocket Opening')
    pleats           = models.CharField(max_length=10, choices=PLEATS_STYLE, default='Single', verbose_name='P0300 / Pleats')
    back_pocket      = models.CharField(max_length=10, choices=BACK_POCKET_STYLE, default='Right', verbose_name='P0400 / Back Pocket')
    lining_style     = models.CharField(max_length=10, choices=LINING_STYLE, default='None', verbose_name='P0500 / Lining')
    length_style     = models.CharField(max_length=20, choices=LENGTH_STYLE, default='At Ankel', verbose_name='P0600 / Pants Length')
    lower_leg_style  = models.CharField(max_length=30, choices=LOWER_LEG_STYLE, default='Consistent with Fit Style', verbose_name='P0700 / Additional Slimming in Lower Leg')

    price       = models.DecimalField(max_digits=8, decimal_places=2)
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
        ('Cut Away - medium','Cut Away - medium'),
        ('Cut Away - large', 'Cut Away - large'),
        ('Pointed - short',  'Pointed - short'),
        ('Pointed - medium', 'Pointed - medium'),
        ('Round',            'Round'),
        ('Band',             'Band'),
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
        ('Matching Colour','Matching Colour'),
    )
    CUFF_BUTTON_NUMBER = (
        ('1','1'),
        ('2','2'),
    )
    CUFF_STYLE = (
        ('Normal', 'Normal'),
        ('French', 'French'),
    )
    CUFF_SHAPE_STYLE = (
        ('Square','Square'),
        ('Angled','Angled'),
        ('Round', 'Round'),
    )
    FRONT_BUTTON_STYLE = (
        ('Plain Front',   'Plain Front'),
        ('Placket Front', 'Placket Front'),
        ('Hidden Buttons','Hidden Buttons'),
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
    SHIRT_LENGTH = (
        ('Normal', 'Normal'),
        ('Shorter','Short'),
        ('Longer', 'Longer'),
    )

    order                  = models.ForeignKey(Order)
    fit                    = models.CharField(max_length=10, choices=FIT_STYLE, default='Regular', verbose_name='H0001 / Fit Style')
    shirt_fabric           = models.ForeignKey(Material, related_name='shirt_fabric',
                             limit_choices_to={'material_type' : 'Shirt Fabric'}, verbose_name='H0002 / Shirt Fabric')
    shirt_buttons          = models.ForeignKey(Material, related_name='shirt_buttons',
                             limit_choices_to={'material_type' : 'Shirt Buttons'}, verbose_name='H0003 / Shirt Buttons')

    collar_style           = models.CharField(max_length=30,  choices=COLLAR_STYLE, default='Cut Away - medium', verbose_name='H0100 / Collar Style')
    collar_point           = models.CharField(max_length=30, choices=COLLAR_POINT, default='Removable Collar Stay', verbose_name='H0101 / Collar Point Style')
    collar_colour_contrast = models.CharField(max_length=20, choices=COLOUR_CONTRAST, default='Same as Shirt', verbose_name='H0102 / Collar Colour Contrast')
    collar_colour          = models.CharField(max_length=30, default='none')
    pocket                 = models.CharField(max_length=20, choices=FRONT_POCKET_STYLE, default='None', verbose_name='H0200 / Front Pocket')
    button_style           = models.CharField(max_length=20, choices=FRONT_BUTTON_STYLE, default='Plain Front', verbose_name='H0201 / Front Buttons Style')
    sleeve_style           = models.CharField(max_length=20, choices=SLEEVE_STYLE, default='Long Sleeve', verbose_name='H0300 / Sleeve Length')
    cuff_button_number     = models.CharField(max_length=1,  choices=CUFF_BUTTON_NUMBER, default='1', verbose_name='H0401 / Cuff Button Number')
    cuff_collour_contrast  = models.CharField(max_length=20, choices=COLOUR_CONTRAST, default='Same as Shirt', verbose_name='H0402 / Cuff Colour Contrast')
    cuff_colour            = models.CharField(max_length=30, default='none')
    cuff_style             = models.CharField(max_length=20, choices=CUFF_STYLE, default='Normal', verbose_name='H0403 / Cuff Style')
    cuff_shape_style       = models.CharField(max_length=20, choices=CUFF_SHAPE_STYLE, default='Square', verbose_name='H0404 / Cuff Shape Style')
    pleats                 = models.CharField(max_length=20, choices=PLEATS_STYLE, default='None', verbose_name='H0500 / Pleats')
    pick_stitching         = models.CharField(max_length=20, choices=PICK_STITCHING_STYLE, default='None', verbose_name='H0601 / Pick Stitching')
    shirt_length           = models.CharField(max_length=20, choices=SHIRT_LENGTH, default='Normal', verbose_name='H0700 / Shirt Length')

    price       = models.DecimalField(max_digits=8, decimal_places=2)
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

    front_button_number    = models.CharField(max_length=20, choices=FRONT_BUTTON_NUMBER, default='4 Buttons', verbose_name='V0100 / Front Buttons')
    front_button_style     = models.CharField(max_length=20, choices=FRONT_BUTTON_STYLE, default='Same as Suit', verbose_name='V0101 / Button Style')
    pocket                 = models.CharField(max_length=20, choices=POCKET_STYLE, default='Normal (x2)', verbose_name='V0102 / Front Pockets')
    pockets_satin_colour   = models.CharField(max_length=20, choices=POCKETS_SATIN_COLOUR, default='No Satin', verbose_name='V0103 / Pockets (satin colour)')
    back_material          = models.CharField(max_length=20, choices=BACK_MATERIAL, default='Lining', verbose_name='V0200 / Back Material Style')
    strap                  = models.CharField(max_length=20, choices=STRAP, default='Strap', verbose_name='V0201 / Strap')

    price       = models.DecimalField(max_digits=8, decimal_places=2)
    remark      = models.TextField(default='none')
    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return 'Vest#' + str(self.id)

