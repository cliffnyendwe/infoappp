from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^edit$', views.edit, name='edit_profile'),
    url(r'^comment/(?P<post_id>\d+)', views.add_post, name='comment'),
    url(r'^post/$', views.add_post,name='add_post'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^new/rating/(\d+)',views.newrating, name='newrating'),
    url(r'^mystores/$',views.mystores,name = 'mystores'),
    url(r'^stores/(\d+)',views.stores,name ='stores'),
    url(r'^new_stores$', views.new_stores, name='new_stores'),
    url(r'^myschools/$',views.myschools,name = 'myschools'),
    url(r'^schools/(\d+)',views.schools,name ='schools'),
    url(r'^new_schools$', views.new_schools, name='new_schools'),
  
  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
