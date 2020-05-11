from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm, widgets

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=32)
    profile_image = forms.CharField(required=True, widget=forms.TextInput(attrs={ "class": "form-control"}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')


class EditProfileForm(ModelForm):
    class Meta:
        model = User
        widgets = {
            "first_name": widgets.TextInput(attrs={"class": "form-control"}),
            "last_name": widgets.TextInput(attrs={"class": "form-control"}),

        }
        fields = ('first_name', 'last_name')