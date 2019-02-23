from django import forms

class AddItemForm(forms.Form):
    item_name = forms.CharField(max_length=70,
            widget=forms.TextInput(
                attrs={'class':'form-control input-md' , 'id':'item', 'placeholder':'Add items in the list'}
            ))