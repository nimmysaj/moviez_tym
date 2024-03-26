from django.urls import path
from . import views

app_name='movie_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('articles/',views.articles,name='articles'),
    path('article/',views.article,name='article'),
    path('<slug:c_slug>/',views.allmoviecat,name='movies_by_category'),
    path('<slug:c_slug>/<slug:movie_slug>',views.moviedetail,name='moviedetail'),
]