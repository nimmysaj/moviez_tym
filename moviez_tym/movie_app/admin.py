from django.contrib import admin

from movie_app.models import Category, Movie


# Register your models here.
class categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

class movieadmin(admin.ModelAdmin):
    list_display = ['name','category_name','release_date']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20

admin.site.register(Category,categoryadmin)
admin.site.register(Movie,movieadmin)