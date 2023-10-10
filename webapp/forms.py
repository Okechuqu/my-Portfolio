from django import forms


class ClientForm(forms.Form):
    first_name = forms.CharField(max_length=50, label='', widget=forms.TextInput(
        attrs={'class': 'form-control py-2 mb-1', 'placeholder': 'First Name', 'required': 'true'}))
    last_name = forms.CharField(max_length=50,label='', widget=forms.TextInput(
        attrs={'class': 'form-control py-2 mb-1', 'placeholder': 'Last Name', 'required': 'true'}))
    email = forms.EmailField(max_length=100,label='', widget=forms.EmailInput(
        attrs={'class': 'form-control py-2 mb-1', 'placeholder': 'Email', 'required': 'true'}))
    phone = forms.IntegerField(label='', widget=forms.NumberInput(
        attrs={'class': 'form-control py-2 mb-1', 'placeholder': '+234', 'required': 'true'}))
    message = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'form-control py-2 mb-1', 'rows': 4, 'placeholder': 'Message Me'}))
