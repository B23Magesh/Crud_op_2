from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.

def Home(request):
    form=Creation()
    d={'form':form}
    if request.method =='POST':
        form=Creation(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'message.html')
    
    return render(request,'index.html',d)

def Message(request):
    return render(request,'index.html')

