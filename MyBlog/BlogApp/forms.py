from django import forms
from .models import BlogPost, BlogComment
from django.utils.translation import gettext_lazy as _

# choices = Category.objects.all().values_list('name', 'name')
#
# choice_list = []
# for item in choices:
#     choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'author', 'reference_author', 'header_image', 'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'Placeholder': 'Your BlogApp Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            'reference_author': forms.TextInput(attrs={'class': 'form-control', 'Placeholder': 'Your Reference Author (Optional)'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'Placeholder': 'Write a short description here'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'Placeholder': 'Write your BlogApp here'}),
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'reference_author', 'header_image', 'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'reference_author': forms.TextInput(attrs={'class': 'form-control', 'Placeholder': '(Optional)'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = ('name',)
#
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#         }
#
#
# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = BlogComment
#         fields = ('name', 'body')
#         labels = {
#             'body': _('Comment'),
#         }
#
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control', 'Placeholder': 'Enter your name'}),
#             'body': forms.Textarea(attrs={'class': 'form-control', 'Placeholder': 'Write your Comment'}),
#         }