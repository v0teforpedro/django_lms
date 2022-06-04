from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import TeacherCreateForm, TeacherUpdateForm
from .models import Teacher


class CreateTeacherView(CreateView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/create_teacher.html'
    form_class = TeacherCreateForm
    extra_context = {'title': 'Create Teacher'}


class ListTeacherView(ListView):
    model = Teacher
    template_name = 'teachers/teachers.html'
    extra_context = {'title': 'List of Teachers'}


class UpdateTeacherView(UpdateView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/update_teacher.html'
    form_class = TeacherUpdateForm
    extra_context = {'title': 'Update Teacher'}


class DeleteTeacherView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'confirmation.html'
