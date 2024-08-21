from django import forms
from .models import Item


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'category', 'description', 'price', 'image']

        widgets = {
            'name': forms.TextInput(attrs={'class':'ml-2 border border-2 border-gray-500 rounded-xl px-5'}),
            'description': forms.Textarea(attrs={'class':'ml-2 border border-2 border-gray-500 rounded-xl px-5 h-[150px]'}),
           }