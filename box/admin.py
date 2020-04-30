from django.contrib import admin

from box import views, models

admin.site.register(models.Author)
admin.site.register(models.Recipe)
