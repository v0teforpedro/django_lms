from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import TeacherCreateForm
from .models import Teacher
from webargs.fields import Int
from webargs.djangoparser import use_args


def create_teacher(request):
    if request.method == 'GET':
        form = TeacherCreateForm()
    else:
        form = TeacherCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Teacher Created!</h1>')

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
    teacher = Teacher.objects.get(pk=pk)
    if request.method == 'GET':
        form = TeacherCreateForm(instance=teacher)
    else:
        form = TeacherCreateForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers'))

    return render(
        request,
        'teachers/update_teacher.html',
        context={'title': 'Update Teacher', 'form': form}
    )


def delete_teacher(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return HttpResponseRedirect(reverse('teachers'))
    else:
        return render(request, 'confirmation.html', {'object': teacher})


@use_args(
    {
        'cnt': Int(required=False)
    },
    location='query'
)
def generate_teachers(request, args):
    if args:
        for key, value in args.items():
            Teacher.gen_teachers(**{key: value})
            return HttpResponse(f'Successfully generated {value} teacher(s)!')
    else:
        Teacher.gen_teachers()
        return HttpResponse('Successfully generated 10 teachers!')
