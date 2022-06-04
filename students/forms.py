from core.forms import PersonCreateForm

from django_filters import FilterSet

from .models import Student


class StudentCreateForm(PersonCreateForm):
    class Meta(PersonCreateForm.Meta):
        model = Student
        fields = '__all__'


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
