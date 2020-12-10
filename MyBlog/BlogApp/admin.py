from django.contrib import admin
from .models import BlogPost, UserProfile, BlogComment

admin.site.register(BlogPost)
#admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(BlogComment)

