from django import forms

from .models import Menu


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('item_type','item_name', 'item_price', 'item_description')
