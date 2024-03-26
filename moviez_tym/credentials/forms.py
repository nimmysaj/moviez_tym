from django import forms
from django.contrib.auth.models import User

from credentials.models import Review
from movie_app.models import Movie,Category

class movieform(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['name','slug','description','category_name','poster','actors','release_date','youtube_link','user']
        widgets={
            'slug':forms.TextInput(attrs={'placeholder':'same as movie name'}),
            'user': forms.TextInput(attrs={'placeholder': 'same as username'})
        }

class userform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']

class userupdateform(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email']


class reviewform(forms.ModelForm):
    class Meta:
        model=Review
        fields=['user','movie','comments','rate']
        widgets={
            'user': forms.TextInput(attrs={'placeholder': 'same as username'}),
            'rate': forms.NumberInput(attrs={'placeholder': 'out of 10'})
        }