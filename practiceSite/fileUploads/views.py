from django.shortcuts import render
from .forms import DocumentForm
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib import messages
# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'fileUploads/index.html'

def modelFormUpload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request,'File was uploaded Successfully')
            return HttpResponseRedirect('')
        else:
            messages.info(request,'There was some issue in uploading the file please try again')
    else:
        form = DocumentForm()
    return render(request,'fileUploads/upload.html',{'form':form})