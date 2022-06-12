from django.urls import path

from .views import create_teacher
from .views import delete_teacher
from .views import teachers
from .views import update_teacher


app_name = 'teachers'

urlpatterns = [
    path('', teachers, name='list'),
    path('create/', create_teacher, name='create'),
    path('update/<int:pk>/', update_teacher, name='update'),
    path('delete/<int:pk>/', delete_teacher, name='delete')
]
