from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def create(request):
    s={'m':[{'im':'1.jpeg'},
            {'im':'1.jpeg'},
            {'im':'1.jpeg'},]}
    return render(request,'create.html',s)

def edit(request):
    return render(request,'edit.html')

def list(request):
    return render(request,'list.html')