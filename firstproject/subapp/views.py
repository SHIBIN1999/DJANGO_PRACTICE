from django.shortcuts import render
from django.http import HttpResponse
from . models import Student
from . forms import StudentModel
# Create your views here.
def create(request):
    if request.POST:
        obj1=StudentModel(request.POST)
        if obj1.is_valid():
            obj1.save()
    else:
        obj1=StudentModel()
    
   
    return render(request,'create.html',{'obj':obj1})

   
def list(request):
    t=Student.objects.all()
    return render(request,'list.html',{'t':t})
def table(request):
    t=Student.objects.all()
    return render(request,'table.html',{'t':t})

def delete(request,pk):
    get_id=Student.objects.get(pk=pk)
    print(get_id)
    get_id.delete()
    t=Student.objects.all()
    return render(request,'table.html',{'t':t})



def edit(request,pk):
   get_id=Student.objects.get(pk=pk)
   obj1=StudentModel(instance=get_id)
   if request.POST:
       title=request.POST.get('title')
       summary=request.POST.get('summary')
       year=request.POST.get('year')
       get_id.title=title
       get_id.summary=summary
       get_id.year=year
       get_id.save()

       
   return render(request,'create.html',{'obj':obj1})