from django.db import models
from movie_app.models import Movie
# Create your models here.

class Review(models.Model):
    user = models.CharField(max_length=200)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    comments = models.TextField(blank=True)
    rate = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.movie)