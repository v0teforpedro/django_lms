from core.forms import PersonCreateForm

from .models import Teacher


class TeacherCreateForm(PersonCreateForm):
    class Meta(PersonCreateForm.Meta):
        model = Teacher
        fields = '__all__'


class TeacherUpdateForm(TeacherCreateForm):
    class Meta(TeacherCreateForm.Meta):
        exclude = ['birthday']
