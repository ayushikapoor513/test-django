from django.shortcuts import render
from django.http import HttpResponse
from . models import Test
def index(request):
    return render(request,'index.html')
def final(request):
    name=request.POST['n1']
    roll=request.POST['roll']
    ins = Test(name=name,roll=roll)
    ins.save()
    res=Test.objects.all()
    return render(request,'index.html',{'result':res})