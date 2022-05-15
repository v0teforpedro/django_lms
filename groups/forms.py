from django import forms
from .models import Group


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'group_name',
            'max_capacity',
            'curr_students',
            'disciplines'
        ]


