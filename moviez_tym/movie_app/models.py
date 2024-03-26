from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='category',blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('movie_app:movies_by_category',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Movie(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    category_name=models.ForeignKey(Category,on_delete=models.CASCADE)
    poster=models.ImageField(upload_to='movie_poster',blank=True)
    actors=models.TextField(blank=True)
    release_date=models.DateField()
    youtube_link=models.URLField(max_length=500)
    user=models.CharField(max_length=200)

    class Meta:
        ordering=('name',)
        verbose_name='movie'
        verbose_name_plural=('movies')

    def get_url(self):
        return reverse('movie_app:moviedetail',args=[self.category_name.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)


