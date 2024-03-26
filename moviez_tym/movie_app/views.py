from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render, get_object_or_404

from credentials.models import Review
from movie_app.models import Movie, Category


# Create your views here.
def index(request):
    category = Category.objects.all()
    return render(request,'index.html',{'category':category})
def about(request):
    return render(request,'about-us.html')
def contact(request):
    return render(request,'contact-us.html')
def sitemap(request):
    return render(request,'sitemap.html')
def articles(request):
    return render(request,'articles.html')
def article(request):
    return render(request,'article.html')

def allmoviecat(request,c_slug=None):
    c_page=None
    movies_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        movies_list=Movie.objects.all().filter(category_name=c_page)
    else:
        movies_list=Movie.objects.all()

    paginator=Paginator(movies_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        movies=paginator.page(page)
    except(EmptyPage,InvalidPage):
        movies=paginator.page(paginator.num_pages)

    return render(request,'category.html',{'category':c_page,'movies':movies})

def moviedetail(request,c_slug,movie_slug):
    try:
        movies=Movie.objects.get(category_name__slug=c_slug,slug=movie_slug)
    except Exception as e:
        raise e
    return render(request,'movie.html',{'movie':movies})


