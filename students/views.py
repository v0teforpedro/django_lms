# from copy import copy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import StudentCreateForm, StudentFilterForm, StudentUpdateForm
from .models import Student


class CreateStudentView(LoginRequiredMixin, CreateView):
    model = Student
    success_url = reverse_lazy('students:list')
    template_name = 'students/create_student.html'
    form_class = StudentCreateForm
    extra_context = {'title': 'Create Student'}


class ListStudentView(ListView):
    model = Student
    template_name = 'students/students.html'
    paginate_by = 10

    def get_filter(self):
        return StudentFilterForm(
            data=self.request.GET,
            queryset=self.model.objects.all().select_related('group', 'headman_group')
        )

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.get_filter().form

        # params = self.request.GET
        # if 'page' in params:
        #     params = copy(params)
        #     del params['page']
        #
        # context['params'] = f'&{params.urlencode()}' if params else ''

        return context


# def students(request):
#     st = Student.objects.all().select_related('group', 'headman_group')
#     students_filter = StudentFilterForm(data=request.GET, queryset=st)
#
#     return render(
#         request,
#         'students/students.html',
#         context={'title': 'List of Students', 'students_filter': students_filter}
#     )


class UpdateStudentView(LoginRequiredMixin, UpdateView):
    model = Student
    success_url = reverse_lazy('students:list')
    template_name = 'students/update_student.html'
    form_class = StudentUpdateForm
    extra_context = {'title': 'Update Student'}


class DeleteStudentView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('students:list')
    template_name = 'confirmation.html'
