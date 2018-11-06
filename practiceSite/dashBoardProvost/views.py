from django.shortcuts import render
from django.views import generic
from .forms import DocumentForm
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'dashBoardProvost/dashboard.html'


def modelFormUpload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'File was uploaded Successfully')
            return HttpResponseRedirect('')
        else:
            messages.info(
                request, 'There was some issue in uploading the file please try again')
    else:
        form = DocumentForm()
    return render(request, 'dashBoardProvost/upload.html', {'form': form})


def index(request):
    return render(request, "dashBoardStudent/index.html", {})


def logged_in(request):
    return HttpResponse("SuccessFully logged in")


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect('/dashBoardProvost/')
            else:
                return HttpResponse("Your account is not active")
        else:
            return HttpResponse("Invalid Login Attempt")
    else:
        return render(request, "dashBoardProvost/login.html", {})
