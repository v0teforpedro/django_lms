from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import TeacherCreateForm, TeacherUpdateForm
from .models import Teacher


class CreateTeacherView(LoginRequiredMixin, CreateView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/create_teacher.html'
    form_class = TeacherCreateForm
    extra_context = {'title': 'Create Teacher'}


class ListTeacherView(ListView):
    model = Teacher
    template_name = 'teachers/teachers.html'
    extra_context = {'title': 'List of Teachers'}
    paginate_by = 10


class UpdateTeacherView(LoginRequiredMixin, UpdateView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/update_teacher.html'
    form_class = TeacherUpdateForm
    extra_context = {'title': 'Update Teacher'}


class DeleteTeacherView(LoginRequiredMixin, DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'confirmation.html'
