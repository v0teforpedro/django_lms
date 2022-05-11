from django.shortcuts import render
from django.http import HttpResponse
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
