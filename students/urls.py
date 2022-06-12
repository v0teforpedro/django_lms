from django.urls import path

from .views import CreateStudentView
from .views import DeleteStudentView
from .views import ListStudentView
from .views import UpdateStudentView


app_name = 'students'

urlpatterns = [
    path('', ListStudentView.as_view(), name='list'),
    path('create/', CreateStudentView.as_view(), name='create'),
    path('update/<int:pk>/', UpdateStudentView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteStudentView.as_view(), name='delete')
]
