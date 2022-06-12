from django import forms

from .models import Group


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

        exclude = ['headman']


class GroupUpdateForm(GroupCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['headman_field'] = forms.ChoiceField(
            choices=[
                (student.pk, f'{student.first_name} {student.last_name}') for student in self.instance.students.all()
            ],
            label='Headman',
            required=False
        )
