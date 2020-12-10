from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=250)
    title_tag = models.CharField(max_length=200)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    type = models.CharField(max_length=250)
    description = models.TextField()
    location = models.CharField(max_length=300)
    snippet = models.CharField(max_length=300)
    image = models.FileField(blank=True)

    def __str__(self):
        return self.title + " : " + str(self.author)

    def get_absolute_url(self):
        return reverse('tie_up_list')


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, related_name='has_images', on_delete=models.CASCADE)
    images = models.FileField(upload_to='Images/')

    def __str__(self):
        return self.post.title