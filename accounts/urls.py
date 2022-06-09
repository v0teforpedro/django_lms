from django.urls import path

from .views import AccountLoginView
from .views import AccountLogoutView
from .views import AccountProfileView
from .views import AccountRegistrationView
from .views import AccountUpdateView

app_name = 'accounts'

urlpatterns = [
    path('registration/', AccountRegistrationView.as_view(), name='registration'),
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', AccountLogoutView.as_view(), name='logout'),
    path('profile/', AccountProfileView.as_view(), name='profile'),
    path('update/', AccountUpdateView.as_view(), name='update'),
]
