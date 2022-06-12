from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import StudentCreateForm, StudentFilterForm, StudentUpdateForm
from .models import Student


def create_student(request):
    if request.method == 'GET':
        form = StudentCreateForm()
    else:
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))

    return render(
        request,
        'students/create_student.html',
        context={'title': 'Create Student', 'form': form}
    )


def students(request):
    st = Student.objects.all().select_related('group', 'headman_group')
    students_filter = StudentFilterForm(data=request.GET, queryset=st)

    return render(
        request,
        'students/students.html',
        context={'title': 'List of Students', 'students_filter': students_filter}
    )


def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'GET':
        form = StudentUpdateForm(instance=student)
    else:
        form = StudentUpdateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))

    return render(
        request,
        'students/update_student.html',
        context={'title': 'Update Student', 'form': form}
    )


def delete_student(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('students:list'))
    else:
        return render(request, 'confirmation.html', {'object': student})
