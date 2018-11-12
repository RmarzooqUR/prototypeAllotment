from django.contrib import admin
from .models import dataModel,studentModel,roomModel
# Register your models here.


admin.site.register(dataModel)
admin.site.register(roomModel)
admin.site.register(studentModel)
