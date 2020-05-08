from django import forms
from box.models import Author


class AddRecipeForm(forms.Form):
		title = forms.CharField(max_length=30)
		body = forms.CharField(widget=forms.Textarea)
		author = forms.ModelChoiceField(queryset=Author.objects.all())

class AddAuthorForm(forms.ModelForm):
	class Meta:
		model = Author
		fields = [
			"name",
			"bio",
			"user"
		]

class LoginForm(forms.Form):
	username = forms.CharField(max_length=50)
	password = forms.CharField(widget=forms.PasswordInput)

