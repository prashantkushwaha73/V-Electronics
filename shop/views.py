from django.shortcuts import render
from django.http import HttpResponse
from .models import Prod


# Create your views here.


def index(request):
    
    ############################################################
    
    myset = set([])
    all = Prod.objects.all() 
    
    for i in all:
        myset.add(i.category)
    
    
    
    
    
    ############################################################
    
    
    
    
    params = {'alll':myset,'list':all}
    return render(request,'shop/index.html',params)
