from django.conf.urls import patterns, include, url
from youthPlatform.views import Search, Login
from youthPlatform.models import * 

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'karmathalo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^jobs/', Search.as_view(model=JobAd), name='searchjob'),
    url(r'^trainings/', Search.as_view(model=TrainingAd), name='searchtraining'),
    url(r'^ideas/', Search.as_view(model=Idea), name='searchidea'),
    url(r'^login/', Login.as_view(), name='login'),
    url(r'^logout/', Logout.as_view(), name='logout'),
    
)
