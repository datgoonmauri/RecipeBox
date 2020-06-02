from django.contrib import admin
from django.urls import path
from box import views
from box.models import *
from box.views import *

urlpatterns = [
    path('', views.index, name='homepage'),
    path('addauthor/', views.addauthor, name="addauthor"),
    path('recipeadd/', views.recipeadd, name="recipeadd"),
    path("", views.recipe_list_view, name="recipes"),
    path("recipes/<int:recipe_id>", views.recipe_detail_view, name="recipe_detail"),
    path("author/<int:author_id>", views.author_detail_view, name="author_detail"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logoutview, name="logout"),
    path('recipes/<int:pk>/update/', RecipeUpdateView.as_view(), name="recipeupdate"),

    # path('admin/', admin.site.urls),
]
