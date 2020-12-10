from django import forms
from .models import Post, PostImage


class AddTieUpForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'description', 'type', 'snippet', 'location', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'Placeholder': 'Your Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'Placeholder': 'Your Site Tag'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'Placeholder': 'Write a short description here'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'Placeholder': 'Write your Description here'}),
            'type': forms.TextInput(attrs={'class': 'form-control', 'Placeholder': 'Property Type'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'Placeholder': 'Property Location Link'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file', 'Placeholder': 'Image', 'type': 'file'}),
        }


class AddTieUpImagesForm(forms.ModelForm):
    class Meta:
        model = PostImage
        exclude = ()


class UpdateTieUpForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'description', 'type', 'snippet', 'location', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file', 'type': 'file'}),
        }