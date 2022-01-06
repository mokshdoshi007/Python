from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from myapp.models import TempUsers, Users
from turfs.models import Bookings, Turfs
from myapp.utilities import addtoken, check_pw_hash, make_pw_hash, sendmail, swaptoken, token_request
from django.views.decorators.csrf import csrf_exempt
from random import randint
from django.db import IntegrityError
from rest_framework.utils import json

def indexPage(request):
    return render(request,"index.html")

@csrf_exempt
def register(request):
    data = json.loads(request.body)
    name=data['name']
    contact=data['contact']
    emp=Users.objects.filter(contact=contact)
    if emp:
        response={'statusCode':404,'message':'Contact already exists'}
    else:
        email=data['email']
        emp=Users.objects.filter(email=email)
        if emp:
            response={'statusCode':404,'message':'Email already exists'}
        else:
            password=data['password']
            password=make_pw_hash(password)
            birthday=data['birthday']
            otp=randint(100000,999999)
            try:
                emp=TempUsers(name=name, contact=contact, email=email, password=password, birthday=birthday, otp=otp)
                emp.save()
            except IntegrityError:
                TempUsers.objects.filter(email=email).update(name=name, contact=contact, email=email, password=password, birthday=birthday, otp=otp)
                TempUsers.objects.filter(contact=contact).update(name=name, contact=contact, email=email, password=password, birthday=birthday, otp=otp)
            sendmail('Django','mail_template',email,{'name':name,'otp':otp})
            response={'statusCode':200,'message':'OTP sent'}
    return JsonResponse(response)

@csrf_exempt
def checkotp(request):
    data = json.loads(request.body)
    otp=data['otp'] 
    email=data['email'] 
    emp=TempUsers.objects.filter(email=email).first()
    if emp:
        if int(otp)==emp.otp:
            authToken=list()
            at=token_request()
            authToken.append(at)
            stu=Users(name=emp.name, contact=emp.contact, email=emp.email, password=emp.password, birthday=emp.birthday, authToken=authToken)
            stu.save()
            emp.delete()
            response={'statusCode':200,'message':'Account registered','authToken':at, 'id':stu.id}
        else:
            emp.delete()
            response={'statusCode':404,'message':'Wrong OTP. Register Again'}    
    else:
        response={'statusCode':404,'message':'Wrong Email'}
    return JsonResponse(response)        

@csrf_exempt
def forpass(request):
    data = json.loads(request.body)
    email=data['email'] 
    emp=Users.objects.filter(email=email)
    if emp:
        otp=randint(100000,999999)
        sendmail('Django','mail_template',email,{'otp':otp})
        try:
            emp=TempUsers(email=email, otp=otp, name="none", contact=1, birthday="1111-1-1")
            emp.save()
        except IntegrityError:
            TempUsers.objects.filter(email=email).update(otp=otp)
        response={'statusCode':200,'message':'OTP sent'}        
    else:
        response={'statusCode':404,'message':'Email does not exist'}
    return JsonResponse(response)

@csrf_exempt
def verifyotp(request):
    data = json.loads(request.body)
    otp=data['otp'] 
    email=data['email'] 
    emp=TempUsers.objects.filter(email=email).first()
    if emp:
        if int(otp)==emp.otp:
            emp.otp=randint(10000000,99999999)
            emp.save()
            response={'statusCode':200,'message':'OTP Verified. Ask for new password', "token":emp.otp}
        else:
            emp.delete()
            response={'statusCode':404,'message':'Wrong OTP. Try Again'}    
    else:
        response={'statusCode':404,'message':'Wrong Email'}
    return JsonResponse(response)        


@csrf_exempt
def editcity(request):
    data = json.loads(request.body)
    authToken=data['authToken']
    id=data['id']
    city=data['city']
    emp=Users.objects.filter(id=id, authToken__contains=[authToken]).first()
    if emp:
        emp.authToken=swaptoken(emp.authToken,authToken)
        emp.city=city
        emp.save()
        response={'statusCode':200,'message':'City changed'}
    else:
        response={'statusCode':404,'message':'Wrong Email'}
    return JsonResponse(response)        

@csrf_exempt
def changepass(request):
    data = json.loads(request.body)
    email=data['email'] 
    token=data['token']
    password=data['password']
    emp=TempUsers.objects.filter(email=email,otp=token)
    if emp:
        emp.delete()
        emp=get_object_or_404(Users,email=email)
        password=make_pw_hash(password)
        emp.password=password
        emp.save()
        response={'statusCode':200,'message':'Password changed'}
    else:
        response={'statusCode':404,'message':'Wrong Email/Token'}
    return JsonResponse(response)        

@csrf_exempt
def fetchall(request):
    emp=Users.objects.all() 
    if emp:
        data=list()
        for e in emp:
            data.append({'id':e.id,'name':e.name,'contact':e.contact,'email':e.email,'birthday':e.birthday,'authToken':e.authToken,'city':e.city,'stars':e.stars,'favturfs':e.favturfs})
        response={'statusCode':200,'message':'All OK!','data':data}
    else:
        response={'statusCode':404,'message':'No data'}
    return JsonResponse(response)

@csrf_exempt
def deleteprofile(request):
    data = json.loads(request.body)
    authToken=data['authToken']
    password=data['password']
    id=data['id']
    emp=Users.objects.filter(id=id, authToken__contains=[authToken]).first()
    if emp:
        if check_pw_hash(password,emp.password):    
            emp.delete()
            response={'statusCode':200,'message':'User Deleted'}
        else:
            response={'statusCode':404,'message':'Incorrect Password'}
    else:
        response={'statusCode':404,'message':'Invalid authToken/id'}
    return JsonResponse(response)

@csrf_exempt
def updateprofile(request):
    data = json.loads(request.body)
    authToken=data['authToken']
    id=data['id']
    emp=Users.objects.filter(id=id,authToken__contains=[authToken]).first()
    if emp:
        name=data['name']
        contact=data['contact']
        emp.authToken=swaptoken(emp.authToken,authToken)
        emp.save()
        emp=Users.objects.filter(contact=contact).exclude(id=id)
        if emp:
            response={'statusCode':404,'message':'Contact already exists'}
        else:
            birthday=data['birthday']
            Users.objects.filter(id=id).update(name=name, contact=contact, birthday=birthday)
            response={'statusCode':200,'message':'Data updated successfully'}
    else:
        response={'statusCode':404,'message':'Invalid authToken/id'}
    return JsonResponse(response)

@csrf_exempt
def login(request):
    data = json.loads(request.body)
    email=data['email']
    password=data['password']
    emp=Users.objects.filter(email=email).first()
    if emp:
        if check_pw_hash(password,emp.password):
            at=token_request()
            emp.authToken=addtoken(emp.authToken,at)
            emp.save()
            response={'statusCode':200,'message':'All OK!','authToken':at,'id':emp.id}
        else:
            response={'statusCode':404,'message':'Check Password'}    
    else:
        response={'statusCode':404,'message':'Check Email'}
    return JsonResponse(response)

@csrf_exempt
def togglefav(request):
    data = json.loads(request.body)
    authToken=data['authToken']
    id=data['id']
    tid=data['tid']
    emp=Users.objects.filter(id=id, authToken__contains=[authToken]).first()
    if emp:
        emp.authToken=swaptoken(emp.authToken,authToken)
        x=emp.favturfs
        if tid in x:
            x.remove(tid)
            emp.favturfs=x
            emp.save()
            response={'statusCode':200,'message':'Turf removed from favourites'}
        else:
            x.append(tid)
            emp.favturfs=x
            emp.save()
            response={'statusCode':200,'message':'Turf added in favourites'}
    else:
        response={'statusCode':404,'message':'Invalid authToken/id'}
    return JsonResponse(response)    

@csrf_exempt
def rateturf(request):
    data = json.loads(request.body)
    authToken=data['authToken']
    id=data['id']
    tid=data['tid']
    stars=data['stars']
    emp=Users.objects.filter(id=id, authToken__contains=[authToken]).first()
    trf=Turfs.objects.filter(id=tid).first()
    if emp:
        emp.authToken=swaptoken(emp.authToken,authToken)
        x=emp.stars
        flag=0
        for i in range(len(x)) :
            if tid==x[i][0]:
                m=trf.users*trf.stars-x[i][1]+stars
                trf.stars=m/trf.users
                x[i][1]=stars
                flag=1
                break
        if flag==0:
            m=trf.users*trf.stars+stars
            trf.users=trf.users+1
            trf.stars=m/trf.users
            x.append([tid,stars])
        emp.stars=x
        emp.save()
        trf.save()
        response={'statusCode':200,'message':'Turf rated'}
    else:
        response={'statusCode':404,'message':'Invalid authToken/id'}
    return JsonResponse(response)    

@csrf_exempt        
def getfav(request):
    data = json.loads(request.body)
    authToken=data['authToken']
    id=data['id']
    emp=Users.objects.filter(id=id, authToken__contains=[authToken]).first()
    if emp:
        emp.authToken=swaptoken(emp.authToken,authToken)
        emp.save()
        response={'statusCode':200,'message':'All OK!','data':{'favturfs':emp.favturfs,'stars':emp.stars}}
    else:
        response={'statusCode':404,'message':'Invalid authToken/id'}
    return JsonResponse(response)    

@csrf_exempt        
def getprofile(request):
    data = json.loads(request.body)
    authToken=data['authToken']
    id=data['id']
    emp=Users.objects.filter(id=id, authToken__contains=[authToken]).first()
    if emp:
        emp.authToken=swaptoken(emp.authToken,authToken)
        emp.save()
        data={'name':emp.name,'contact':emp.contact,'email':emp.email,'birthday':emp.birthday,'city':emp.city}
        if emp.owner:
            owner=list()
            t=Turfs.objects.filter(user=emp)
            for trf in t:
                owner.append([trf.id,trf.name])
            data['owner']=owner
        response={'statusCode':200,'message':'All OK!','data':data}
    else:
        response={'statusCode':404,'message':'Invalid authToken/id'}
    return JsonResponse(response)    
    
@csrf_exempt        
def logout(request):
    data = json.loads(request.body)
    authToken=data['authToken']
    id=data['id']
    emp=Users.objects.filter(id=id, authToken__contains=[authToken]).first()
    if emp:
        emp.authToken.remove(authToken)
        emp.save()
        response={'statusCode':200,'message':'Logout Successful'}
    else:
        response={'statusCode':404,'message':'Invalid authToken/id'}
    return JsonResponse(response)    
    
@csrf_exempt        
def records(request):
    data = json.loads(request.body)
    authToken=data['authToken']
    id=data['id']
    emp=Users.objects.filter(id=id, authToken__contains=[authToken]).first()
    if emp:
        emp.authToken=swaptoken(emp.authToken,authToken)
        emp.save()
        booking=Bookings.objects.filter(user=emp)
        data=list()
        for b in booking:
            data.append({'ticket':'A12345', 'tid':b.turf.id, 'date':b.date, 'slot':b.slot, 'timestamp':b.time})
        response={'statusCode':200,'message':'All OK!','data':data}
    else:
        response={'statusCode':404,'message':'Invalid authToken/id'}
    return JsonResponse(response)    
