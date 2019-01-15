from django import forms
from .models import Profile,Post,Comment
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
        exclude = ['user','neighborHood','pub_date']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name']