from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import StudentCreateForm
from .models import Student
from .utils import qs2html
from webargs.fields import Str, Int
from webargs.djangoparser import use_args
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'index.html')


@use_args(
    {
        'first_name': Str(required=False),
        'last_name': Str(required=False),
        'age': Int(required=False),
        'phone_number': Int(required=False)
    },
    location='query'
)
def students(request, args):
    st = Student.objects.all()
    for key, value in args.items():
        st = st.filter(**{key: value})
    return render(
        request,
        'students/students.html',
        context={'title': 'List of Students', 'students': qs2html(st)}
    )


@csrf_exempt
def create_student(request):
    if request.method == 'GET':
        form = StudentCreateForm()
    else:
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students')

    html_form = f"""
        <form method="post">
            <table>
                {form.as_table()}
            </table>
            <input type="submit" value="Create">
        </form> 
        """

    return HttpResponse(html_form)


@csrf_exempt
def update_student(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'GET':
        form = StudentCreateForm(instance=student)
    else:
        form = StudentCreateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students')

    html_form = f"""
        <form method="post">
            <table>
                {form.as_table()}
            </table>
            <input type="submit" value="Update">
        </form> 
        """

    return HttpResponse(html_form)
