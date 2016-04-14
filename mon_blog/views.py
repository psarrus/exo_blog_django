# from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def hello_world(request):
    # return HttpResponse("Hello World")
    date = datetime.now()
    return render(request,'index.html',{'current_date':date})
