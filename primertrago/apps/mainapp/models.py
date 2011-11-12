from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
DAYS = (
    ('0', _("Lunes")),
    ('1', _("Martes")),
    ('2', _("Miercoles")),
    ('3', _("Jueves")),
    ('4', _("Viernes")),
    ('5', _("Sabado")),
    ('6', _("Domingo")),
)

class City(models.Model):
    name = models.CharField(max_length=32)

class Neighborhood(models.Model):
    city = models.ForeignKey(City)
    name = models.CharField(max_length=32)

class Bar(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=32, null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    website = models.URLField(verify_exists=False, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    facebook_page = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class HappyHour(models.Model):
    bar = models.ForeignKey(Bar)
    day = models.CharField(choices=DAYS, max_length=1)
    hour_start  = models.TimeField()
    hour_end    = models.TimeField()
    description = models.TextField()


