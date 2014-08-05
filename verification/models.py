from django.db import models

from suits.models import Suit
from suits.models import Pant
from suits.models import Shirt
from suits.models import Vest


class VeriSuit(models.Model):
    suit              = models.OneToOneField(Suit)

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

    remark      = models.TextField(default='none')
    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.suit.id) + ' | Verified Suit# ' + str(self.id)

class VeriPant(models.Model):
    pant              = models.OneToOneField(Pant)

    waist_girth       = models.DecimalField(max_digits=5, decimal_places=2)
    hip_girth         = models.DecimalField(max_digits=5, decimal_places=2)
    thigh             = models.DecimalField(max_digits=5, decimal_places=2)
    knee_girth        = models.DecimalField(max_digits=5, decimal_places=2)
    ankel_girth       = models.DecimalField(max_digits=5, decimal_places=2)
    pant_outseam      = models.DecimalField(max_digits=5, decimal_places=2)
    front_crotch      = models.DecimalField(max_digits=5, decimal_places=2)
    back_crotch       = models.DecimalField(max_digits=5, decimal_places=2)

    remark      = models.TextField(default='none')
    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.pant.id) + ' | Verified Pant# ' + str(self.id)

class VeriShirt(models.Model):
    shirt             = models.OneToOneField(Shirt)

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

    remark      = models.TextField(default='none')
    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.shirt.id) + ' | Verified Shirt# ' + str(self.id)

class VeriVest(models.Model):
    vest             = models.OneToOneField(Vest)

    remark      = models.TextField(default='none')
    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.vest.id) + ' | Verified Vest# ' + str(self.id)
