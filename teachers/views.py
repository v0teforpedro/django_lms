from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


from .forms import TeacherCreateForm, TeacherUpdateForm
from .models import Teacher


def create_teacher(request):
    if request.method == 'GET':
        form = TeacherCreateForm()
    else:
        form = TeacherCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))

    return render(
        request,
        'teachers/create_teacher.html',
        context={'title': 'Create Teacher', 'form': form}
    )


def teachers(request):
    tch = Teacher.objects.all()
    return render(
        request,
        'teachers/teachers.html',
        context={'title': 'List of Teachers', 'teachers': tch}
    )


def update_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'GET':
        form = TeacherUpdateForm(instance=teacher)
    else:
        form = TeacherUpdateForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))

    return render(
        request,
        'teachers/update_teacher.html',
        context={'title': 'Update Teacher', 'form': form}
    )


def delete_teacher(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return HttpResponseRedirect(reverse('teachers:list'))
    else:
        return render(request, 'confirmation.html', {'object': teacher})
