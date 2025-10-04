from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context={'name':'Tawfiq','mark':'99'}
    return render(request,'index.html',context)
