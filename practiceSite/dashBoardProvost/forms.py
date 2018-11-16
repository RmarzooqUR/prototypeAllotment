from django import forms
from .models import Document,dataModel

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('file', )

class dataModelForm(forms.ModelForm):
    class Meta:
        model=dataModel
        fields = "__all__"

class InitializeHostelForm(forms.Form):
    hostel_name = forms.CharField(max_length=120)
    numberOfRooms = forms.IntegerField()
    seater = forms.IntegerField()

