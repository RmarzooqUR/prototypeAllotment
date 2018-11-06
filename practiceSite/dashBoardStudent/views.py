from django.shortcuts import render
from django.views import generic
# Create your views here.


from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
#from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'dashBoardStudent/dashboard.html'


def index(request):
    return render(request,"dashBoardStudent/index.html",{})

def logged_in(request):
    return HttpResponse("SuccessFully logged in")

def login_view(request):

    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)

                return HttpResponseRedirect('/dashBoardStudent/')
            else:
                return HttpResponse("Your account is not active")
        else:
            return HttpResponse("Invalid Login Attempt")
    else:  
        return render(request, "dashBoardStudent/login.html", {}) 

