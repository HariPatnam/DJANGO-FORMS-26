from django.shortcuts import render

from django.http import HttpResponse

from app.forms import *

# Create your views here.

def student(request):
    SFO=studentform()
    d={'SFO':SFO}

    if request.method=='POST':
        FD=studentform(request.POST)
        if FD.is_valid():
            return HttpResponse(str(FD.cleaned_data))
            
        return HttpResponse('YOUR DATA IS SUBMITTED ')










    return render(request,'studentform.html',d)
