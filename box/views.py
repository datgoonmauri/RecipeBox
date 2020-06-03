from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import UpdateView, DeleteView, TemplateView

from box.models import *
from box.forms import *
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User


def index(request):
    author_data = Author.objects.all()
    recipe_data = Recipe.objects.all()
    return render(request, "index.html", {"author_data": author_data, "recipe_data": recipe_data})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})


@login_required()
def addauthor(request):
    html = "generic_form.html"
    form = AddAuthorForm()
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['name']
            )
            author = Author.objects.create(
                name=data['name'], bio=data['bio'], user=user)
            author.save()
        return HttpResponseRedirect(
            request.GET.get('next', reverse('homepage')))

    if request.user.is_staff:
        return render(request, html, {"form": form})
    return render(request, '')


@login_required()
def recipeadd(request):
    html = "generic_form.html"

    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            Recipe.objects.create(
                title=data['title'],
                author=data['author']
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = AddRecipeForm()
    return render(request, html, {"form": form})


def recipe_detail_view(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, "recipe_detail.html", {"recipe": recipe})


def recipe_list_view(request):
    recipes = Recipe.objects.all()
    return render(request, "recipe_list.html", {"recipes": recipes})


def author_detail_view(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    recipes = Recipe.objects.filter(author=author_id)
    viewed_user = User.objects.get(username=author)
    print('view', viewed_user)
    return render(
        request, "author_detail.html", {"author": author, "recipes": recipes, 'viewed_user': viewed_user}
    )


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ['title', 'description', 'instructions']

    def form_valid(self, form):
        return super().form_valid(form)


def favorite_recipe(request, recipe_id):
    curr_user = request.user
    print(curr_user)
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe.favorite.add(curr_user)
    return HttpResponseRedirect(reverse('homepage'))



