from django.conf.urls import patterns, include, url
from youthPlatform.views import Search, Login, Logout, Profile, Index
from youthPlatform.models import * 

urlpatterns = patterns('',
    # Examples:
     url(r'^$', Index.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^jobs/', Search.as_view(model=JobAd,searchtype='jobs'), name='jobs'),
    url(r'^trainings/', Search.as_view(model=TrainingAd,searchtype='trainings'), name='trainings'),
    url(r'^ideas/', Search.as_view(model=Idea,searchtype='ideas'), name='ideas'),
    url(r'^login/', Login.as_view(), name='login'),
    url(r'^logout/', Logout.as_view(), name='logout'),
    url(r'^profile/', Profile.as_view(), name='profile'),
    
)
