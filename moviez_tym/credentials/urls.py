from django.urls import path
from . import views

app_name='credentials'

urlpatterns = [
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('add_movie/',views.addmovie,name='add_movie'),
    path('movie_list/',views.movielist,name='movie_list'),
    path('review_list/',views.review_list,name='review_list'),
    path('review/',views.review,name='review'),
    path('edit_movie/<int:id>/',views.editmovie,name='edit_movie'),
    path('delete_movie/<int:id>/',views.deletemovie,name='delete_movie'),
    path('edit_profile/<int:id>/',views.editprofile,name='edit_profile'),
    path('view_profile/<int:id>/',views.viewprofile,name='view_profile'),

]