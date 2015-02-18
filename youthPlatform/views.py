from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.contrib.sessions.backends.db import SessionStore
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from youthPlatform.models import *

# Create your views here.
(IDEA, INVESTOR, PROVIDER) = range(1, 4)

# our search result view, which is universally applicable for searching
# all the things like jobs or trainings or ideas

class Search(View):
    model = None
    def __init__(self, model):
        model = model
        self.model = model

    def get(self, request):
        try:
            queryString = request.GET.get('query')
        except:
            queryString = None

        if queryString==None:
            # just show the results, no need of any filters
            results = self.model.objects.order_by('-priority')
        else:
            queryString = queryString.upper()
            # split the query by space and comma
            splitspace = queryString.split()
            splitcomma = queryString.split(',')
            splitted =  splitspace + splitcomma
            # match the querystring also
            allquals = []
            for x in splitted:
                allquals += Qualification.objects.filter(Q(level__contains=x) | Q(field__contains=x))

            q = Q()
            for x in allquals:
                q|=Q(qualification=x)
            
            querylocation = Q()
            for x in splitted:
                querylocation |= (Q(institutionLocation__contains=x) | Q(institutionDistrict__contains=x))

            results = self.model.objects.filter(q | querylocation)


        context = {}
        context['results'] = self.paginate(results, request)
        if len(context['results'])==0:
            error = "no results found"
        else:
            error = None
        context['error'] = error

        return render(request, 'youthPlatform/trainings.html', context)


    def paginate(self, results, request):
        paginator = Paginator(results, 10) # show 10 per page
        page = request.GET.get('page')

        try:
            result = paginator.page(page)
        except PageNotAnInteger:
            result = paginator.page(1)
        except EmptyPage:
            result = paginator.page(paginator.num_pages)

        error = None
        if len(result)==0:
            error = "No results found"

        return result


class Login(View):
    
    def get(self, request):
        if request.session.get('username', ''):
            return HttpResponseRedirect(reverse('profile'))
        else:
            return render(request, 'youthPlatform/Login.html', {'error' : None})

    def post(self, request):
        error = None
        if request.session.get('username',''):
            return HttpResponseRedirect(reverse("profile"))

        usrname = request.POST.get('username','')
        pssword = request.POST.get('password','')
        usertype = request.POST.get('type','')
            
        if usrname=='' or pssword=='':
            error = "username/password can't be empty"
            return render(request, 'youthPlatform/login.html', {'error':error})
        else:
            user = Account.objects.filter(username=usrname, password=pssword)
            if len(user)== 0:
                error = 'username/password not valid'
                return render(request, 'youthPlatform/login.html', {'error':error})
            else:
                request.session['username'] = user[0].username
                return HttpResponseRedirect(reverse('profile'))

class Logout(View):
    def post(self,request):
        pass

    def get(self,request):
        if request.session.get('username',''):
            del request.session['username']
        return render(request, 'youthPlatform/login.html', {'error':None})

class Profile(View):
    
    def get(self,request):
        usrname = request.session.get('username',"")
        if not usrname or usrname is None:
            return render(request, 'youthPlatform/login.html', {'error' : None})
#        return HttpResponse("user profile")
        return render(request, "youthPlatform/profile.html", {"username" : usrname})


class Index(View):
    def get(self, request):
        return render(request, "youthPlatform/index.html", {})











