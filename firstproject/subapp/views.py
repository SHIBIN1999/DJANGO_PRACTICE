from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def create(request):
    s={'m':[{'title':'the gold','summary':'the gold ','year':2010,'success':True},
            {'title':'the car','summary':'the vilage ','year':2020,'success':True},
            {'title':'the village','summary':'the major ','year':2009,'success':True}]}
    return render(request,'create.html',s)