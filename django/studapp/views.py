from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def indexPage(request):
    time=datetime.now()
    return render(request,"index.html",{'name':'Moksh','time':time})
    #return HttpResponse("This message is returned from views")