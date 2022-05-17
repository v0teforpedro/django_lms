from django.urls import path
from .views import students
from .views import create_student
from .views import update_student
from .views import delete_student

urlpatterns = [
    path('', students, name='students'),
    path('create/', create_student, name='create_student'),
    path('update/<int:pk>/', update_student, name='update_student'),
    path('delete/<int:pk>/', delete_student, name='delete_student')
]
