from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Profile(models.Model):
    Profile_photo = models.ImageField(upload_to = 'images/',blank=True)
    Bio = models.TextField(max_length = 50,null = True)
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    email_address = models.CharField(max_length = 50,null = True)
    location = models.CharField(max_length = 50,null = True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)

    def save_profile(self):
        self.save()

    @classmethod
    def get_by_id(cls, id):
        details = Profile.objects.get(user = id)
        return details

    @classmethod
    def filter_by_id(cls, id):
        details = Profile.objects.filter(user = id).first()
        return details
    
    @classmethod
    def search_user(cls, name):
        userprof = Profile.objects.filter(user__username__icontains = name)
        return userprof


class Post(models.Model):
    name = models.CharField(max_length=50,blank=True)
    image = models.ImageField(upload_to = 'images/')
    description = models.TextField(max_length = 50,null = True)
    user = models.ForeignKey(User, null = True,related_name='post')
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    
    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def get_hood_posts(cls,id):
        posts = Post.objects.filter(id = id)
        return posts

class Comment(models.Model):
    name = models.CharField(max_length=30)
    post = models.ForeignKey(Post,null = True)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def find_commentpost(cls,id):
        comments = Comments.objects.filter(post__pk = id)
        return comments

