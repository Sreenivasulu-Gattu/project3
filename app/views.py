from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def helo(request):
    return HttpResponse('<h1 style="color:red">Hello ,, Hi .. Successfully executed..</h1>')