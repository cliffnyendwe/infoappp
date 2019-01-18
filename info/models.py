from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import URLValidator

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
    location = models.CharField(max_length=50,blank=True)
    
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


class Stores(models.Model):
    image = models.ImageField(upload_to = 'stores/',default='pic.jpg')
    name_of_store = models.CharField(max_length=50,blank=True)
    brach_number = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    branch_email_address = models.CharField(max_length = 50,null = True)
    description = models.TextField(max_length = 500)
    link = models.TextField(validators=[URLValidator()],null=True)
    
  

    def save_stores(self):
        self.save()

    def delete_stores(self):
        self.delete()

    @classmethod
    def get_all(cls):
        projects = cls.objects.all()
        return stores

    @classmethod
    def get_stores(cls, project_id):
        project = cls.objects.get(id=site_id)
        return stores

    @classmethod
    def search_by_title(cls,search_term):
        stores_location = cls.objects.filter(title__icontains=search_term)


class Hospitals(models.Model):
    image = models.ImageField(upload_to = 'stores/',default='pic.jpg')
    name_of_hospital = models.CharField(max_length=50,blank=True)
    location = models.CharField(max_length = 50)
    hospital_email_address = models.CharField(max_length = 50,null = True)
    description = models.TextField(max_length = 500)
    link = models.TextField(validators=[URLValidator()],null=True)
    
  

    def save_hospitals(self):
        self.save()

    def delete_hospitalls(self):
        self.delete()

    @classmethod
    def get_all(cls):
        projects = cls.objects.all()
        return hospitals

    @classmethod
    def get_hospitals(cls, project_id):
        project = cls.objects.get(id=site_id)
        return hospitals

        return sites_title


class Schools(models.Model):
    image = models.ImageField(upload_to = 'stores/',default='pic.jpg')
    name_of_school = models.CharField(max_length=50,blank=True)
    location = models.CharField(max_length = 50)
    school_email_address = models.CharField(max_length = 50,null = True)
    description = models.TextField(max_length = 500)
    link = models.TextField(validators=[URLValidator()],null=True)
    
  

    def save_schools(self):
        self.save()

    def delete_schools(self):
        self.delete()

    @classmethod
    def get_all(cls):
        projects = cls.objects.all()
        return schools

    @classmethod
    def get_schools(cls, project_id):
        project = cls.objects.get(id=site_id)
        return schools

        return sites_title


class Rating(models.Model):

  CHOICES = [(i,i) for i in range(11)]

  affordability = models.IntegerField(choices=CHOICES)
  reliability = models.IntegerField(choices=CHOICES)
  conviniency = models.IntegerField(choices=CHOICES)
  postername = models.CharField(max_length=60)
  pub_date = models.DateTimeField(auto_now_add=True)


  def save_rating(self):
    self.save()

  def delete_rating(self):
    self.delete()