from django import forms


class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = None
        fields = None

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
