from django.urls import path
from .views import teachers
from .views import create_teacher
from .views import update_teacher
from .views import delete_teacher
from .views import generate_teachers

urlpatterns = [
    path('', teachers, name='teachers'),
    path('create/', create_teacher, name='create_teacher'),
    path('update/<int:pk>/', update_teacher, name='update_teacher'),
    path('delete/<int:pk>/', delete_teacher, name='delete_teacher'),
    path('generate_teachers/', generate_teachers)
]
