from django import forms
from mainapp.models import Neighborhood
from django.utils.translation import gettext as _

WEEKDAY = (
    ('', "--"),
    ('monday', _("Lunes")),
    ('tuesday', _("Martes")),
    ('wednesday', _("Miercoles")),
    ('thursday', _("Jueves")),
    ('friday', _("Viernes")),
    ('saturday', _("Sabado")),
    ('sunday', _("Domingo")),
)
class FilterForm(forms.Form):
    weekday = forms.ChoiceField(required=False,choices=WEEKDAY, widget=forms.Select(attrs={'class': 'medium dropdown day'}))
    hour    = forms.TimeField(required=False,widget=forms.TextInput(attrs={'class': 'mini time'}))
    neighborhood = forms.ModelChoiceField(Neighborhood.objects.all(),required=False, widget=forms.Select(attrs={'class': 'medium dropdown location'}))
#                                          to_field_name=lambda x: x.name)
