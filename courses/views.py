from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import CourseCreateForm
from .models import Course


class CreateCourseView(CreateView):
    model = Course
    success_url = reverse_lazy('groups:list')
    template_name = 'courses/create_course.html'
    form_class = CourseCreateForm
    extra_context = {'title': 'Create Course'}


class ListCourseView(ListView):
    model = Course
    template_name = 'courses/courses.html'
    extra_context = {'title': 'List of Courses'}


class UpdateCourseView(UpdateView):
    model = Course
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/update_course.html'
    form_class = CourseCreateForm
    extra_context = {'title': 'Update Course'}


class DeleteCourseView(DeleteView):
    model = Course
    success_url = reverse_lazy('courses:list')
    template_name = 'confirmation.html'
