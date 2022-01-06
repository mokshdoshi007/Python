import datetime 
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.utils import json
from turfs.models import Turfs, Location, Bookings
from myapp.models import Users
from turfs.utilities import ntime,changeday
from django.db.models import Count
from myapp.utilities import swaptoken

@csrf_exempt
def view(request):
    turf=Turfs.objects.all()
    loc=Location.objects.all()
    if turf and loc:
        data=list()
        for e in turf:
            data.append({'tid':e.id,'name':e.name,'capacity':e.capacity,'description':e.description,'stars':e.stars,'users':e.users,'imageUrls':e.imageUrls,'price':e.price,'slots':e.slots,'sourceslots':e.sourceslots,'sourceprice':e.sourceprice})
        for l in loc:
            data.append({'latitude':l.latitude,'longitude':l.longitude,'address':l.address,'area':l.area,'city':l.city,'pincode':l.pincode})
        response={'statusCode':200,'message':'All OK!','data':data}
    else:
        response={'statusCode':404,'message':'No data'}
    return JsonResponse(response)

@csrf_exempt
def addturf(request):
    data = json.loads(request.body)
    name=data['name']
    capacity=data['capacity']
    description=data['description']
    contact=data['contact']
    a=[[""]*48]*7
    b=[[0]*48]*7    
    rate=data['rate']
    imageUrls=data['imageUrls']
    latitude=data['latitude']
    longitude=data['longitude']
    address=data['address']
    area=data['area']
    city=data['city']
    pincode=data['pincode']
    try:
        t=Turfs(name=name, rate=rate, capacity=capacity, description=description, contact=contact, sourceslots=a, sourceprice=b, price=b, slots=a, imageUrls=imageUrls)
        t.save()
        l=Location(latitude=latitude, longitude=longitude, address=address, area=area, city=city, pincode=pincode, turf=t)
        l.save()
        response={'statusCode':200,'message':'Turf Added'}
    except:
        response={'statusCode':404,'message':'Turf Not Added'}    
    return JsonResponse(response)

@csrf_exempt
def editslot(request):
    data = json.loads(request.body)
    id=data['id']
    authToken=data['authToken']
    tid=data['tid']
    day=data['day']
    slot=data['slots']
    emp=Users.objects.filter(id=id, authToken__contains=[authToken]).first()
    turf=Turfs.objects.filter(id=tid).first()
    if emp and turf:
        emp.authToken=swaptoken(emp.authToken,authToken)
        emp.save()
        if turf.user==emp:
            slots=list()
            price=list()
            for i in range (len(slot)):
                slots.append(slot[i]['show'])
                price.append(slot[i]['price'])
            slots=slots+['']*(48-len(slots))
            price=price+[0]*(48-len(price))
            x=turf.sourceslots
            x[day]=slots
            y=turf.sourceprice
            y[day]=price
            a=turf.slots
            b=turf.price
            date=datetime.date.today().strftime('%Y-%m-%d')
            day2=datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
            if day2>day:
                m=7-day2+day
            else:
                m=day-day2
            if a[m][0]=="":
                a[m]=slots
                b[m]=price
                turf.slots=a
                turf.price=b
                response={'statusCode':200,'message':'Turf Updated Immediately'}
            else:
                t=datetime.datetime.strptime(date, "%Y-%m-%d") + datetime.timedelta(days=m+1)
                date=t.strftime('%Y-%m-%d')
                response={'statusCode':200,'message':'Turf will be Updated','date':date}
            turf.sourceslots=x
            turf.sourceprice=y
            turf.save()
            
        else:
            response={'statusCode':404,'message':'Wrong Owner'}
    else:
        response={'statusCode':404,'message':'Invalid Turf/Owner Details'}
    return JsonResponse(response)

@csrf_exempt
def turfprofile(request):
    data = json.loads(request.body)
    id=data['id']
    authToken=data['authToken']
    tid=data['tid']
    emp=Users.objects.filter(id=id, authToken__contains=[authToken]).first()
    turf=Turfs.objects.filter(id=tid).first()
    if emp and turf:
        emp.authToken=swaptoken(emp.authToken,authToken)
        emp.save()
        if turf.user==emp:
            date=datetime.date.today().strftime('%Y-%m-%d')
            data=list()
            for i in range(7):
                try:
                    x=turf.slots[i]
                    y=turf.price[i]
                    data2=list()    
                    j=int(0)
                    while x[j]!="":
                        data2.append([x[j],y[j],ntime(x[j]),""])
                        j=j+1
                    bookings=Bookings.objects.filter(turf=turf, date=date)
                    if bookings:
                        for b in bookings:
                            for i in range(len(data2)):
                                if data2[i][0]==b.slot:
                                    data2[i][3]="1"
                                    break
                    data.append({'date':date,'slots':data2})
                except:
                    data.append({'date':date,'slots':[]})
                x=datetime.datetime.strptime(date, "%Y-%m-%d") + datetime.timedelta(days=1)
                date=x.strftime('%Y-%m-%d')
            response={'statusCode':200,'message':'All OK!','data':data}
        else:
            response={'statusCode':404,'message':'Wrong Owner'}
    else:
        response={'statusCode':404,'message':'Invalid Turf/Owner Details'}
    return JsonResponse(response)

@csrf_exempt
def getslot(request):
    data = json.loads(request.body)
    id=data['id']
    authToken=data['authToken']
    tid=data['tid']
    emp=Users.objects.filter(id=id, authToken__contains=[authToken]).first()
    turf=Turfs.objects.filter(id=tid).first()
    if emp and turf:
        emp.authToken=swaptoken(emp.authToken,authToken)
        emp.save()
        if turf.user==emp:
            data2=dict()
            for i in range(7):
                data=list()
                x=turf.sourceslots[i]
                y=turf.sourceprice[i]
                j=int(0)
                while x[j]!="":
                    data.append([x[j],y[j],ntime(x[j])])
                    j=j+1
                data2[i]=data
            response={'statusCode':200,'message':'All OK!','data':data2}
        else:
            response={'statusCode':404,'message':'Wrong Owner'}
    else:
        response={'statusCode':404,'message':'Invalid Turf/Owner Details'}
    return JsonResponse(response)

@csrf_exempt
def editturf(request):
    data = json.loads(request.body)
    id=data['id']
    authToken=data['authToken']
    tid=data['tid']
    emp=Users.objects.filter(id=id, authToken__contains=[authToken]).first()
    turf=Turfs.objects.filter(id=tid).first()
    if emp and turf:
        emp.authToken=swaptoken(emp.authToken,authToken)
        emp.save()
        if turf.user==emp:
            turf.description=data['description']
            turf.contact=data['contact']
            turf.capacity=data['capacity']
            turf.save()
            response={'statusCode':200,'message':'Details Updated'}
        else:
            response={'statusCode':404,'message':'Wrong Owner'}
    else:
        response={'statusCode':404,'message':'Invalid Turf/Owner Details'}
    return JsonResponse(response)

@csrf_exempt
def brief(request):
    data = json.loads(request.body)
    city=data['city']
    trfs=Location.objects.filter(city=city)
    if trfs:
        data=list()
        for t in trfs:
            data.append({'tid':t.turf.id,'name':t.turf.name,'area':t.area,'rate':t.turf.rate,'capacity':t.turf.capacity,'stars':t.turf.stars})
        response={'statusCode':200,'message':'All OK!','data':data}
    else:
        response={'statusCode':404,'message':'No turfs'}
    return JsonResponse(response)

@csrf_exempt
def getcity(request):
    cityset = Location.objects.values('city').annotate(count=Count('city'))
    if cityset:
        data=list()
        for c in cityset:
           data.append([c['city'],c['count']])
        response={'statusCode':200,'message':'All OK!','data':data}
    else:
        response={'statusCode':404,'message':'No Cities'}
    return JsonResponse(response)

@csrf_exempt
def detail(request):
    data = json.loads(request.body)
    city=data['city']
    l=Location.objects.filter(city=city)
    if l:
        data=list()
        for loc in l:
            trf=loc.turf
            data.append({'tid':trf.id,'name':trf.name,'capacity':trf.capacity,'stars':trf.stars,'users':trf.users,'contact':trf.contact,'rate':trf.rate,'description':trf.description,'imageUrls':trf.imageUrls,
            'latitude':loc.latitude,'longitude':loc.longitude,'address':loc.address,'area':loc.area,'city':loc.city,'pincode':loc.pincode})
        response={'statusCode':200,'message':'All OK!','data':data}            
    else:
        response={'statusCode':404,'message':'Check City'}
    return JsonResponse(response)

@csrf_exempt
def singleturf(request):
    data = json.loads(request.body)
    tid=data['tid']
    trf=Turfs.objects.filter(id=tid).first()
    if tid:
        loc=Location.objects.filter(turf=trf).first()
        data={'tid':trf.id,'name':trf.name,'capacity':trf.capacity,'stars':trf.stars,'users':trf.users,'contact':trf.contact,'rate':trf.rate,'description':trf.description,'imageUrls':trf.imageUrls,
            'latitude':loc.latitude,'longitude':loc.longitude,'address':loc.address,'area':loc.area,'city':loc.city,'pincode':loc.pincode}
        response={'statusCode':200,'message':'All OK!','data':data}            
    else:
        response={'statusCode':404,'message':'Check Turf ID'}
    return JsonResponse(response)

@csrf_exempt
def defaultit(request):
    turfs=Turfs.objects.all()
    if turfs:
        a=[[""]*48]*7
        b=[[0]*48]*7
        for t in turfs:
            t.slots=a
            t.price=b
            t.sourceslots=a
            t.sourceprice=b
            t.save()
    Bookings.objects.all().delete()
    response={'statusCode':200,'message':'All Slots & Bookings Cleared'}
    return JsonResponse(response)

@csrf_exempt
def citybookings(request):
    data = json.loads(request.body)
    city=data['city']
    date=data['date']
    day=datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
    date2=datetime.date.today().strftime('%Y-%m-%d')
    day2=datetime.datetime.strptime(date2, '%Y-%m-%d').weekday()
    if day2>day:
        m=7-day2+day
    else:
        m=day-day2
    loc=Location.objects.filter(city=city)
    if loc:
        data=list()
        for l in loc:
            try:
                x=l.turf.slots[m]
                y=l.turf.price[m]
                data2=list() 
                i=int(0)
                while x[i]!="":
                    data2.append([x[i],y[i],ntime(x[i])])
                    i=i+1
                bookings=Bookings.objects.filter(turf=l.turf, date=date)
                if bookings:
                    for b in bookings:
                        for i in range(len(data2)):
                            if data2[i][0]==b.slot:
                                data2[i][1]=0
                                break
                data.append({'tid':l.turf.id,'slots':data2})
            except:
                data.append({'tid':l.turf.id,'slots':[]})
        response={'statusCode':200,'message':'All OK!','data':data}
    else:
        response={'statusCode':404,'message':'Check City'}
    return JsonResponse(response)

@csrf_exempt
def turfbookings(request):
    data = json.loads(request.body)
    tid=data['tid']
    turf=Turfs.objects.filter(id=tid).first()
    if turf:
        date=datetime.date.today().strftime('%Y-%m-%d')
        data=list()
        for i in range(7):
            try:
                x=turf.slots[i]
                y=turf.price[i]
                data2=list()    
                j=int(0)
                while x[j]!="":
                    data2.append([x[j],y[j],ntime(x[j])])
                    j=j+1
                bookings=Bookings.objects.filter(turf=turf, date=date)
                if bookings:
                    for b in bookings:
                        for i in range(len(data2)):
                            if data2[i][0]==b.slot:
                                data2[i][1]=0
                                break
                data.append({'date':date,'slots':data2})
            except:
                data.append({'date':date,'slots':[]})
            x=datetime.datetime.strptime(date, "%Y-%m-%d") + datetime.timedelta(days=1)
            date=x.strftime('%Y-%m-%d')
        response={'statusCode':200,'message':'All OK!','data':data}
    else:
        response={'statusCode':404,'message':'Invalid Turf ID'}
    return JsonResponse(response)

@csrf_exempt
def turfrecords(request):
    data = json.loads(request.body)
    id=data['id']
    authToken=data['authToken']
    tid=data['tid']
    emp=Users.objects.filter(id=id, authToken__contains=[authToken]).first()
    turf=Turfs.objects.filter(id=tid).first()
    if emp and turf:
        emp.authToken=swaptoken(emp.authToken,authToken)
        emp.save()
        if turf.user==emp:
            booking=Bookings.objects.filter(turf=turf)
            data=list()
            for b in booking:
                data.append({'ticket':'A12345', 'name':b.user.name, 'date':b.date, 'slot':b.slot, 'timestamp':b.time})
            response={'statusCode':200,'message':'All OK!','data':data}
        else:
            response={'statusCode':404,'message':'Wrong Owner'}
    else:
        response={'statusCode':404,'message':'Invalid Turf/Owner Details'}
    return JsonResponse(response)

@csrf_exempt
def bookturf(request):
    data = json.loads(request.body)
    date=data['date']
    slot=data['slot']
    id=data['id']
    authToken=data['authToken']
    tid=data['tid']
    emp=Users.objects.filter(id=id, authToken__contains=[authToken]).first()
    if emp:
        emp.authToken=swaptoken(emp.authToken,authToken)
        emp.save()
        try:
            t=get_object_or_404(Turfs,id=tid)
            b=Bookings(date=date, slot=slot, user=emp, turf=t)
            b.save()
            response={'statusCode':200,'message':'Booking Successful'}
        except:
            response={'statusCode':404,'message':'Invalid Turf'}
    else:
        response={'statusCode':404,'message':'Invalid Id/AuthToken'}
    return JsonResponse(response)

def daychange(request):
    changeday()
    return "Done"