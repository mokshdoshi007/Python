from turfs.models import Turfs
import datetime

def ntime(mt):
    y=mt.split(' - ')
    x1=y[0].split(':')
    x2=y[1].split(':')
    t1=int(x1[0])*60+int(x1[1])
    t2=int(x2[0])*60+int(x2[1])
    return(str(t1)+' - '+str(t2))

def changeday():
        date=datetime.date.today().strftime('%Y-%m-%d')
        day=datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
        turfs=Turfs.objects.all()
        if turfs:
            for t in turfs:
                a=t.slots
                b=t.price
                x=t.sourceslots
                y=t.sourceprice
                del a[0]
                del b[0]
                a.append(x[day])
                b.append(y[day])
                t.slots=a
                t.price=b
                t.save()