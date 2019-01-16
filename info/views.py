from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from .models import Profile,User,Post,Comment,Stores,Schools
from .forms import ProfileForm,PostForm,CommentForm,NewStoresForm,NewSchoolsForm

@login_required( login_url= '/accounts/login')
def index(request):
    return render(request, 'index.html',{'stores':stores})


@login_required(login_url='/accounts/login/')
def edit(request):
    profile = User.objects.get(username=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('edit_profile')
    else:
        form = ProfileForm()
    return render(request, 'edit_profile.html', locals())


@login_required(login_url='/accounts/login/')
def mystores(request):
    stores = Stores.objects.all().order_by()
    return render(request,'mystores.html', {'stores':stores})

@login_required(login_url='/accounts/login/')
def stores(request, id):
  ida = request.user.id
  ratings = Rating.objects.filter(project=id)
  stores = Store.objects.get(pk=id)

  return render(request, 'stores.html',{'stores':stores,'ratings':ratings})

@login_required(login_url='/accounts/login/')
def new_stores(request):
  ida = request.user.id

  if request.method == 'POST':
    form = NewStoresForm(request.POST, request.FILES)
    if form.is_valid():
      stores = form.save(commit=False)
      stores.save()
    return redirect('index')

  else:
    form = NewStoresForm()

  return render(request, 'new_stores.html',{'form':form})


@login_required(login_url='/accounts/login/')
def myschools(request):
    schools = Schools.objects.all().order_by()
    return render(request,'myschools.html', {'schools':schools})

@login_required(login_url='/accounts/login/')
def schools(request, id):
  ida = request.user.id
  ratings = Rating.objects.filter(project=id)
  schools = School.objects.get(pk=id)

  return render(request, 'schools.html',{'schools':schools,'ratings':ratings})

@login_required(login_url='/accounts/login/')
def new_schools(request):
  ida = request.user.id

  if request.method == 'POST':
    form = NewSchoolsForm(request.POST, request.FILES)
    if form.is_valid():
      schools = form.save(commit=False)
      schools.save()
    return redirect('index')

  else:
    form = NewSchoolsForm()

  return render(request, 'new_schools.html',{'form':form})


@login_required(login_url='/accounts/login')
def add_post(request):
    if request.method == 'POST':
        postform = PostForm(request.POST, request.FILES)
        if postform.is_valid():
            post = postform.save(commit=False)
            post.profile = request.user.profile
            post.user = request.user
            # post.neighborHood=request.user.profile.neighborhood
            post.save()
            # return redirect('hood',request.user.profile.neighborhood.id)
    else:
        postform = PostForm()
    return render(request,'add_post.html',locals())

@login_required(login_url='/accounts/login')
def search_results(request):
    stores= Stores.objects.all()
    if 'stores' in request.GET and request.GET["stores"]:
        search_term = request.GET.get("stores")
        searched_stores = Stores.search(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',locals())


@login_required(login_url='/accounts/login/')
def newrating(request,id):
  ida = request.user.id
  idd = id
  current_username = request.user.username

  if request.method == 'POST':
    form = NewRatingForm(request.POST)
    if form.is_valid():
      rating = form.save(commit=False)
      affordability_rating = form.cleaned_data['affordability']
      reliability_rating = form.cleaned_data[' reliability']
      convieniency_rating = form.cleaned_data['convieniency']
      rating.postername = current_username
      rating.project = stores.objects.get(pk=id)

      rating.save()
    return redirect('stores',id)

  else:
    form = NewRatingForm()

  return render(request, 'newrating.html',{'form':form,'profile':profile,'idd':idd})

