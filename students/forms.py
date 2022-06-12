from django import forms

from django_filters import FilterSet

from .models import Student


class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_first_name(self):
        fn = self.cleaned_data['first_name']
        return fn.title()

    def clean_last_name(self):
        ln = self.cleaned_data['last_name']
        return ln.title()

    def clean_phone_number(self):
        try:
            pn = self.cleaned_data['phone_number']
            output = "".join([character for character in pn if character.isdigit()])
            return output
        except TypeError:
            pass


class StudentFilterForm(FilterSet):
    class Meta:
        model = Student
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith'],
        }


class StudentUpdateForm(StudentCreateForm):
    class Meta(StudentCreateForm.Meta):
        exclude = ['birthday']
