from django.contrib import admin
from django.urls import path

from box import views
from box.models import *
from box.views import *

urlpatterns = [
	path('recipeadd/', views.recipeadd),
	path("", recipe_list_view, name="recipes"),
	path("recipes/<int:recipe_id>", recipe_detail_view, name="recipe_detail"),
	path("author/<int:author_id>", author_detail_view, name="author_detail"),
	# path('admin/', admin.site.urls),
]
