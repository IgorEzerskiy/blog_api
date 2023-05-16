from django.db import models

# Create your models here.

import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Topic(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    prefers = models.ManyToManyField(User)

    def __str__(self):
        return self.title


class Post(models.Model):
    slug = models.SlugField(max_length=150, unique=True)
    title = models.CharField(max_length=150)
    text = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    contains = models.ManyToManyField(Topic)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) + '-' + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M"))
        return super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    created_at = models.DateField(auto_now=True)
    content = models.CharField(max_length=150)
    contains = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
