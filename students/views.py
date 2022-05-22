from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import StudentCreateForm
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
    st = Student.objects.all()
    return render(
        request,
        'students/students.html',
        context={'title': 'List of Students', 'students': st}
    )


def update_student(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'GET':
        form = StudentCreateForm(instance=student)
    else:
        form = StudentCreateForm(request.POST, instance=student)
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
