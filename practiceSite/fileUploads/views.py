from django.shortcuts import render
from .forms import DocumentForm
from django.http import HttpResponseRedirect
# Create your views here.
def modelFormUpload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')
    else:
        form = DocumentForm()
    return render(request,'fileUploads/upload.html',{'form':form})    