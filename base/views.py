from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def tasklist(request):
    return HttpResponse('To Do list')
