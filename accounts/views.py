from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView
from django.views.generic.edit import ProcessFormView

from .forms import ProfileUpdateForm, UserRegistrationForm, UserUpdateForm
from .models import Profile


class AccountRegistrationView(CreateView):
    model = User
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/registration.html'
    form_class = UserRegistrationForm
    extra_context = {'title': 'Registration'}


class AccountLoginView(LoginView):
    template_name = 'accounts/login.html'
    extra_context = {'title': 'Login'}

    def get_redirect_url(self):
        next_value = self.request.GET.get('next')
        if next_value:
            return next_value

        return reverse('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'User <{self.request.user}> - Login successful!')
        return response


class AccountLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'index.html'


class AccountUpdateView(LoginRequiredMixin, ProcessFormView):
    def get(self, request, *args, **kwargs):
        user = request.user
        profile = request.user.profile
        user_form = UserUpdateForm(instance=user)
        profile_form = ProfileUpdateForm(instance=profile)

        return render(request, 'accounts/update.html', {'user_form': user_form, 'profile_form': profile_form})

    def post(self, request, *args, **kwargs):
        user = self.request.user
        profile = user.profile
        user_form = UserUpdateForm(instance=user, data=request.POST)
        profile_form = ProfileUpdateForm(instance=profile, data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('accounts:profile'))

        return render(request, 'accounts/update.html', {'user_form': user_form, 'profile_form': profile_form})


class AccountProfileView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'accounts/profile.html'
    extra_context = {'title': 'My Profile'}
