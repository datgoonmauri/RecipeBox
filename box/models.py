from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField(max_length=150)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    time_required = models.CharField(max_length=30)
    instructions = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    favorite = models.ManyToManyField(User, related_name="fav_recipe", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'recipe_id': self.pk})
