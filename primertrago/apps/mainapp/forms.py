from django import forms
from mainapp.models import Neighborhood
from django.utils.translation import gettext as _

WEEKDAY = (
    ('monday', _("Lunes")),
    ('tuesday', _("Martes")),
    ('wednesday', _("Miercoles")),
    ('jueves', _("Jueves")),
    ('viernes', _("Viernes")),
    ('sabado', _("Sabado")),
    ('domingo', _("Domingo")),
)

class FilterForm(forms.Form):
    weekday = forms.ChoiceField(choices=WEEKDAY, widget=forms.Select(attrs={'class': 'medium'}))
    hour    = forms.TimeField(widget=forms.TextInput(attrs={'class': 'mini'}))
    neighborhood = forms.ModelChoiceField(Neighborhood.objects.all(), widget=forms.Select(attrs={'class': 'medium'}))
#                                          to_field_name=lambda x: x.name)
