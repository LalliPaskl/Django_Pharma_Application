from django import forms
from .models import Items, Customers


class ItemForm(forms.ModelForm):

    class Meta:
        model = Items
        fields = '__all__'


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customers
        fields = '__all__'