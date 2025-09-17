from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def create(request):
    s={'title':'the gold','summary':'the gold ','year':2010}
    return render(request,'create.html',s)