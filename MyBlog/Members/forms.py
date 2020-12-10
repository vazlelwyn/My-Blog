from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext_lazy as _
from BlogApp.models import UserProfile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'Placeholder': 'Enter Valid Email'}))
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'class': 'form-control', 'Placeholder': 'Enter your First Name'}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'class': 'form-control', 'Placeholder': 'Enter your Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'Placeholder': 'Enter Unique Username'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'type': 'password', 'Placeholder': 'Enter Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'type': 'password', 'Placeholder': 'Re-Enter Password'})


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_superuser = forms.CharField(max_length=200, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_staff = forms.CharField(max_length=200, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_active = forms.CharField(max_length=200, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_active', 'is_staff')


class PasswordForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=200, label='Current Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password', 'Placeholder': 'Enter Your Old Password'}))
    new_password1 = forms.CharField(max_length=200, label='New Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password', 'Placeholder': 'Enter New Password'}))
    new_password2 = forms.CharField(max_length=200, label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password', 'Placeholder': 'Re-Enter New Password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url')
        labels = {
            'bio': _('Short Description'),
            'profile_pic': _('Profile Pic'),
        }

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control-file', 'type': 'file'}),
            'website_url': forms.TextInput(attrs={'class': 'form-control', 'Placeholder': 'Enter Website link(Optional)'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control', 'Placeholder': 'Enter Facebook link(Optional)'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control', 'Placeholder': 'Enter Twitter link(Optional)'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control', 'Placeholder': 'Enter Instagram link(Optional)'}),
            'pinterest_url': forms.TextInput(attrs={'class': 'form-control', 'Placeholder': 'Enter Pinterest link(Optional)'}),
        }


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url')
        labels = {
            'bio': _('Short Description'),
            'profile_pic': _('Profile Pic'),
        }

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'Placeholder': 'Write Short Description About You'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control-file', 'type': 'file', 'Placeholder': 'Upload Profile Pic'}),
            'website_url': forms.TextInput(attrs={'class': 'form-control', 'Placeholder': 'Enter Website link(Optional)'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control', 'Placeholder': 'Enter Facebook link(Optional)'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control', 'Placeholder': 'Enter Twitter link(Optional)'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control', 'Placeholder': 'Enter Instagram link(Optional)'}),
            'pinterest_url': forms.TextInput(attrs={'class': 'form-control', 'Placeholder': 'Enter Pinterest link(Optional)'}),
        }
