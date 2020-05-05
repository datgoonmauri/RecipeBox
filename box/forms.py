from django import forms
from box.models import Author


class AddRecipeForm(forms.Form):
		title = forms.CharField(max_length=30)
		body = forms.CharField(widget=forms.Textarea)
		author = forms.ModelMultipleChoiceField(queryset=Author.objects.all())

"""
class Author(models.Model):
	name = models.CharField(max_length=50)
	bio = models.TextField(max_length=150)

	def __str__(self):
		return self.name


class Recipe(models.Model):
	title = models.CharField(max_length=30)
	description = models.TextField()
	time_required = models.CharField(max_length=30)
	instructions = models.TextField()
	author = models.ForeignKey(Author, on_delete=models.CASCADE)

	def __str__(self):
		return self.title
"""