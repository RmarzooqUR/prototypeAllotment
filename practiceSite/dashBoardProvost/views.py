from django.shortcuts import render
import csv
import os
from django.views import generic
from .forms import DocumentForm,dataModelForm,InitializeHostelForm
from .models import dataModel,roomModel,studentModel
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from dashBoardStudent.models import UserLogin

from django.conf import settings
# Create your views here.
# @login_required


# @method_decorator(login_required, name='dispatch')
class IndexView(generic.TemplateView):
    template_name = 'dashBoardProvost/dashboard.html'

def dispath(request):
    return render(request,"Please Login to the system")

@login_required
def modelFormUpload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'File was uploaded Successfully')

            # rows = open(os.path.join(settings.BASE_DIR, 'media/documents/filename.csv'))
            # for row in csv.DictReader(rows, delimiter=","):
            #     form_data =  dataModelForm(row)
            #     if form_data.is_valid():
            #         form_data.save()
            with open(os.path.join(settings.BASE_DIR, 'media/documents/filename.csv')) as f:
                reader = csv.reader(f)
               

                for row in reader:
                    # _, created = dataModel.objects.get_or_create(
                    #     fname = row[0],
                    #     lname = row[1],
                    # )
                    _, created = studentModel.objects.get_or_create(
                        eNo                 = row[0],
                        Name                = row[1],
                        FacNo               = row[2],
                        current_standing    = row[3],
                    )
                    
                    # _, user = UserLogin(
                    #     username = row[0],
                    #     password = row[2],
                    # )
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



def InitializeHostelView(request):
    if request.method == 'POST':
        form = InitializeHostelForm(request.POST)
        if form.is_valid():
            # form.save()

            hostelName = str(form.cleaned_data.get("hostel_name"))
            numberOfRooms = int(form.cleaned_data.get("numberOfRooms"))
            seater = int(form.cleaned_data.get("seater"))
            room_num = 1
            seat_num = 1

            for seat in range(numberOfRooms * seater):
                
                _, instance = roomModel.objects.get_or_create(
                    hostel = hostelName,
                    seat_no = seat_num,
                    room_no = room_num,
                )
                seat_num = seat_num + 1

                if seat % seater == seater-1:
                    room_num = room_num + 1
                    seat_num = 1
            
            return HttpResponseRedirect('')
                # room = roomModel(
                #     hostel=hostelName,
                #     seater = seater,
                #     room_no = room+1,
                #     vacancy = seater,
                # )
                # room.save()
        else:
            messages.info(
                request, 'Invalid Form')
    else:
        form = InitializeHostelForm()
        return render(request,'dashBoardProvost/InitializeHostelForm.html',{'form': form})


             
def allotRooms(request):
    if request.method == 'POST':
        for students in studentModel.objects.all():
            print('hello')

