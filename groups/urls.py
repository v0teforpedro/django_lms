# # from .views import create_group
# # from .views import delete_group
# # from .views import groups
# # from .views import update_group
#
#
# app_name = 'groups'
#
# urlpatterns = [
#     path('', groups, name='list'),
#     path('create/', create_group, name='create'),
#     path('update/<int:pk>/', update_group, name='update'),
#     path('delete/<int:pk>/', delete_group, name='delete')
# ]

from django.urls import path

from .views import CreateGroupView
from .views import DeleteGroupView
from .views import ListGroupView
from .views import UpdateGroupView


app_name = 'groups'

urlpatterns = [
    path('', ListGroupView.as_view(), name='list'),
    path('create/', CreateGroupView.as_view(), name='create'),
    path('update/<int:pk>/', UpdateGroupView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteGroupView.as_view(), name='delete')
]
