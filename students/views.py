from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import StudentCreateForm
from .models import Student
from .utils import qs2html
from webargs.fields import Str, Int
from webargs.djangoparser import use_args
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse('LMS System!')


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

    html_form = """
    <form method="get">
        <label for="first_name">First name:</label><br>
        <input type="text" id="fname" name="first_name" placeholder="Jane"><br>
        <label for="last_name">Last name:</label><br>
        <input type="text" id="lname" name="last_name" placeholder="Doe"><br><br>
        <label for="age">Age:</label><br>
        <input type="number" id="age_id" name="age" placeholder="33"><br><br>
        <label for="phone">Phone Number:</label><br>
        <input type="number" id="phone_number" name="phone_number" placeholder="380*********"><br><br>
        <input type="submit" value="Submit">
    </form> 
    """

    html = qs2html(st)
    response = html_form + html
    return HttpResponse(response)


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
            <input type="submit" value="Submit">
        </form> 
        """

    return HttpResponse(html_form)
