from django import forms

from .models import Teacher


class TeacherCreateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

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


class TeacherUpdateForm(TeacherCreateForm):
    class Meta(TeacherCreateForm.Meta):
        exclude = ['birthday']
