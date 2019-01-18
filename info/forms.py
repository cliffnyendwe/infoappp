from django import forms
from .models import Profile,Post,Comment,Stores,Rating,Schools,Hospitals
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ['user']


# class HoodForm(forms.ModelForm):
#     class Meta:
#         model = NeighborHood
#         exclude= ['occupants']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','pub_date']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name']



class NewStoresForm(forms.ModelForm):
  class Meta:
    model = Stores
    exclude = ['poster','postername', 'pub_date']



class NewHospitalsForm(forms.ModelForm):
  class Meta:
    model = Hospitals
    exclude = ['poster','postername', 'pub_date']

class NewSchoolsForm(forms.ModelForm):
  class Meta:
    model = Schools
    exclude = ['poster','postername', 'pub_date']


class NewRatingForm(forms.ModelForm):
  class Meta:
    model = Rating
    exclude = ['project','postername','pub_date']

