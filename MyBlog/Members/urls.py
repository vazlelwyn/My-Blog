from django.urls import path
from .views import UserRegistrationView, UserEditView, PasswordsChangeView, UserProfileView, EditUserProfileView, CreateUserProfileView
from . import views

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/Change_Password.html')),
    path('password_success/', views.password_success, name='password_success'),
    path('<int:pk>/User_Profile/', UserProfileView.as_view(), name='user_profile'),
    path('<int:pk>/Edit_User_Profile/', EditUserProfileView.as_view(), name='edit_user_profile'),
    path('Create_User_Profile/', CreateUserProfileView.as_view(), name='create_user_profile'),
]
