"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from teachers.views import generate_teachers, teachers, create_teacher, update_teacher, delete_teacher
from students.views import students, create_student, update_student, index
from groups.views import groups, create_group, update_group, delete_group

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate_teachers/', generate_teachers),
    path('students/', students),
    path('students/create/', create_student),
    path('students/update/<int:pk>/', update_student),
    path('teachers/', teachers),
    path('teachers/create/', create_teacher),
    path('teachers/update/<int:pk>/', update_teacher),
    path('teachers/delete/<int:pk>/', delete_teacher),
    path('groups/', groups),
    path('groups/create/', create_group),
    path('groups/update/<int:pk>/', update_group),
    path('groups/delete/<int:pk>/', delete_group),
    path('', index)
]