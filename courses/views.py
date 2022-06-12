from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import CourseCreateForm
from .models import Course


def create_course(request):
    if request.method == 'GET':
        form = CourseCreateForm()
    else:
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses:list'))

    return render(
        request,
        'courses/create_course.html',
        context={'title': 'Create Course', 'form': form}
    )


def courses(request):
    cs = Course.objects.all()
    return render(
        request,
        'courses/courses.html',
        context={'title': 'List of Courses', 'courses': cs}
    )


def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'GET':
        form = CourseCreateForm(instance=course)
    else:
        form = CourseCreateForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses:list'))

    return render(
        request,
        'courses/update_course.html',
        context={'title': 'Update Course', 'form': form, 'course': course}
    )


def delete_course(request, pk):
    course = Course.objects.get(pk=pk)
    if request.method == 'POST':
        course.delete()
        return HttpResponseRedirect(reverse('courses:list'))
    else:
        return render(request, 'confirmation.html', {'object': course})
