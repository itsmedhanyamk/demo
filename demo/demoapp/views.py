from django.http import HttpResponse
from django.shortcuts import render
from .models import Places,Team_members
# Create your views here.
def home(request):
    obj=Places.objects.all()
    team=Team_members.objects.all()
    return render(request,'index.html',{'results':obj,'team_members':team})
def about(request):
    return render(request,'about.html')
def contact(request):
    return HttpResponse("Hi.....am Contact")
def details(request):
    return render(request,'details.html')
def thanks(request):
    return HttpResponse('Thank you...')
def operate(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    add=x+y
    sub=x-y
    mul=x*y
    div=x/y
    return render(request,'result.html',{'num1':x,'num2':y,'add':add,'sub':sub,'mul':mul,'div':div})