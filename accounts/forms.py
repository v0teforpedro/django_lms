from accounts.models import Profile

from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = [
            'username',
            'email'
        ]


class UserUpdateForm(UserChangeForm):
    password = None

    class Meta(UserChangeForm.Meta):
        fields = [
            'first_name',
            'last_name',
            'email'
        ]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'birthday',
            'city'
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
