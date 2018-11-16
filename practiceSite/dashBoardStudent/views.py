from django.shortcuts import render
from django.views import generic
# Create your views here.


from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from dashBoardProvost.models import studentModel, roomModel
#from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'dashBoardStudent/dashboard.html'


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
                
                student = studentModel.objects.get(eNo=username)
                room_data = roomModel.objects.get(student=student)



                context = {
                    'name': student.Name,
                    'eNo' : student.eNo,
                    'facNo': student.FacNo,
                    'standing': student.current_standing,
                    'room_no' : room_data.room_no,
                    'hostelName':room_data.hostel,
                    'seater':room_data.seater,
                }
                return render(request,'dashBoardStudent/dashboard.html',context)
            else:
                return HttpResponse("Your account is not active")
        else:
            return HttpResponse("Invalid Login Attempt")
    else:  
        return render(request, "dashBoardStudent/login.html", {}) 


# def index(request):
#     return render(request, "dashBoardStudent/dashboard.html", {})
