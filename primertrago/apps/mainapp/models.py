from django.db import models
from django.utils.translation import gettext as _
from django.core.urlresolvers import reverse


class City(models.Model):
    name = models.CharField(max_length=32)
    
    def __unicode__(self):
        return self.name

class Neighborhood(models.Model):
    city = models.ForeignKey(City)
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return "%s: %s" % (self.city.name, self.name)

class SubNeighborhood(models.Model):
    city = models.ForeignKey(City)
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name


class Bar(models.Model):
    neighborhood       = models.ForeignKey(Neighborhood)
    sub_neighborhood   = models.ForeignKey(SubNeighborhood, null=True, blank=True)
    name               = models.CharField(max_length=32)
    slug               = models.SlugField(max_length=32, null=True, blank=True)
    address            = models.CharField(max_length=32, null=True, blank=True)
    phone              = models.CharField(max_length=32, null=True, blank=True)
    website            = models.URLField(verify_exists=False, null=True, blank=True)
    email              = models.EmailField(null=True, blank=True)
    facebook_page      = models.URLField(null=True, blank=True)
    description        = models.TextField(null=True, blank=True)
    image              = models.FileField(upload_to="bar", null=True, blank=True)
    featured           = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name
    
    def url(self):
        if self.slug:
            return reverse("mainapp_bar", args=[self.slug])
        else:
            return reverse("mainapp_bar", args=[self.id])

class HappyHour(models.Model):
    bar = models.ForeignKey(Bar)
    monday = models.BooleanField()
    tuesday = models.BooleanField()
    wednesday = models.BooleanField()
    thursday = models.BooleanField()
    friday= models.BooleanField()
    hour_start  = models.TimeField()
    hour_end    = models.TimeField()
    description = models.TextField()


