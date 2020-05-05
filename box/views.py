from django.shortcuts import render, get_object_or_404
from box.models import Recipe, Author
from box.forms import AddRecipeForm

def index(request):
    author_data = Author.objects.all()
    recipe_data = Recipe.objects.all()
    return render(request, "index.html", {"author_data": author_data, "recipe_data": recipe_data })

def recipeadd(request):
    html = "recipeaddform.html"
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
    return render(
        request, "author_detail.html", {"author": author, "recipes": recipes}
    )