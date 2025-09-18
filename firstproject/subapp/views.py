from django.shortcuts import render
from django.http import HttpResponse
from . models import Student
# Create your views here.
def create(request):
    print(request,"ffffffffffff")
    if request.POST:
        title=request.POST.get('title')
        summary=request.POST.get('summary')
        year=request.POST.get('year')
        obj=Student(title=title,summary=summary,year=year)
        obj.save()
   
    return render(request,'create.html')

def edit(request):
   return render(request,'edit.html')
   
def list(request):
    return render(request,'list.html')