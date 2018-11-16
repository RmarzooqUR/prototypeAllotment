from django.db import models
from django.contrib.auth.models import User



class Document(models.Model):
    file = models.FileField(upload_to='documents/')

class dataModel(models.Model):
    fname = models.CharField(max_length=120)
    lname = models.CharField(max_length=120)


class studentModel(models.Model):
    eNo = models.CharField(max_length=6)
    Name = models.CharField(max_length=120)
    FacNo = models.CharField(max_length=10)
    current_standing = models.IntegerField(default=0)
    # room = models.OneToOneField(roomModel,blank=True, on_delete=models.CASCADE)
    # room = models.ManyToManyField(roomModel)


class roomModel(models.Model):
    hostel = models.CharField(max_length=120)
    seater = models.IntegerField()
    room_no= models.IntegerField()
    seat_no = models.IntegerField()
    student = models.OneToOneField(studentModel, on_delete=models.CASCADE, null = True)
    vacant = models.BooleanField()
    



    
# class studentModel(models.Model):
    # eNo = models.CharField(max_length=6)
    # Name = models.CharField(max_length=120)
    # FacNo = models.CharField(max_length=10)
    # current_standing = models.IntegerField(default=0)
    # room = models.ForeignKey(roomModel,on_delete=models.CASCADE,related_name='roomAlloted',blank=True)
    # abcd = models.CharField(max_length = 120)
