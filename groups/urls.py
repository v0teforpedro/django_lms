from django.urls import path
from .views import groups
from .views import create_group
from .views import update_group
from .views import delete_group

urlpatterns = [
    path('', groups, name='groups'),
    path('create/', create_group, name='create_group'),
    path('update/<int:pk>/', update_group, name='update_group'),
    path('delete/<int:pk>/', delete_group, name='delete_group')
]
