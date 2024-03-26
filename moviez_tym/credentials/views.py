from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponseRedirect

from credentials.forms import movieform, userform, reviewform, userupdateform
from credentials.models import Review
from movie_app.models import Movie


# Create your views here.

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists")
                return redirect('/register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exists")
                return redirect('/register/')
            else:
                user = User.objects.create_user(username=username, first_name=fname, last_name=lname, email=email,
                                                password=password)
                user.save()
                print("user created")
                messages.info(request, 'Congratulations, Your account has been successfully created.')
                return redirect('credentials:register')
        else:
            messages.info(request,'password not matching')
            return redirect('credentials:register')
        return redirect('/')
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('credentials:movie_list')
        else:
            messages.info(request,'invalid credentials')
            return redirect('credentials:login')

    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')

def movielist(request):
    movie_list = Movie.objects.filter(user=request.user)
    return render (request,'movie_list.html',{'movie_list':movie_list})
def addmovie(request):
    if request.method=="POST":
        form = movieform(request.POST or None,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('credentials:movie_list')
    else:
        form = movieform
    return render(request,'add_movie.html',{'form':form})

def editmovie(request,id):
    movie=Movie.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('credentials:movie_list')
    return render(request,'edit_movie.html',{'form':form,'movie':movie})


def deletemovie(request,id):
    if request.method=="POST":
        m=Movie.objects.get(id=id)
        m.delete()
        return redirect('credentials:movie_list')
    return render(request,'delete_movie.html')

def editprofile(request,id):
    if request.user.is_authenticated:
        p = User.objects.get(id=request.user.id)
        form = userupdateform(request.POST or None, instance=p)
        if form.is_valid():
            form.save()
            return redirect('credentials:view_profile', id)
        return render(request, 'edit_profile.html', {'form': form})

def viewprofile(request,id):
    p=User.objects.get(id=id)
    return render(request,'view_profile.html',{'profile':p})

def review(request):
    if request.method=="POST":
        form = reviewform(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('credentials:movie_list')
    else:
        form = reviewform
    return render(request,'review.html',{'form':form})

def review_list(request):
    x = Review.objects.all()
    return render(request, 'review_list.html', {'reviews':x})
