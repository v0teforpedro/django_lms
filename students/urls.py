from django.urls import path

from .views import create_student
from .views import delete_student
from .views import students
from .views import update_student


app_name = 'students'

urlpatterns = [
    path('', students, name='list'),
    path('create/', create_student, name='create'),
    path('update/<int:pk>/', update_student, name='update'),
    path('delete/<int:pk>/', delete_student, name='delete')
]
