from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.fields import EmailField, CharField

from .models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['phone']


class UserForm(ModelForm):
    email = EmailField()
    first_name = CharField(required=True, max_length=30)
    last_name = CharField(required=True, max_length=30)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']
        localized_fields = ['email', 'first_name', 'last_name', 'password']
        widgets = {
            'password' : forms.PasswordInput
        }
