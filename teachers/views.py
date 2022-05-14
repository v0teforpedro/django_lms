from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import TeacherCreateForm
from .models import Teacher
from webargs.fields import Int
from webargs.djangoparser import use_args


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


@csrf_exempt
def create_teacher(request):
    if request.method == 'GET':
        form = TeacherCreateForm()
    else:
        form = TeacherCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Teacher Created!</h1>')

    html_form = f"""
        <form method="post">
            <table>
                {form.as_table()}
            </table>
            <input type="submit" value="Create">
        </form> 
        """

    return HttpResponse(html_form)
