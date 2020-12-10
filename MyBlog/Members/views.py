from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordForm, UpdateProfileForm, CreateProfileForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView, CreateView
from BlogApp.models import UserProfile


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordForm
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'registration/Password_Success.html', {})


class UserRegistrationView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/Registration.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/Edit_Profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class UserProfileView(DetailView):
    model = UserProfile
    template_name = 'registration/User_Profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(UserProfileView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context


class EditUserProfileView(generic.UpdateView):
    model = UserProfile
    template_name = 'registration/Edit_User_Profile.html'
    form_class = UpdateProfileForm
    success_url = reverse_lazy('home')


class CreateUserProfileView(CreateView):
    model = UserProfile
    template_name = 'registration/Create_User_Profile.html'
    form_class = CreateProfileForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



