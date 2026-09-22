from django.contrib.auth import logout
from django.shortcuts import render, redirect

from app1.models import Car
from customer.models import Booking


# Create your views here.
def dealerdash(request):
    b2 = 0
    j = Car.objects.filter(user=request.user.id)
    for i in j:
        bb = Booking.objects.filter(car_name=i.id).count()
        b2 += bb

    b1 = Car.objects.filter(user=request.user.id).count()
    b3 = Booking.objects.filter(user=request.user.id, is_status='pending').count()
    context = {
        'b':b2,
        'b1':b1,
        'b3':b3
    }
    return render(request,'adindex.html',context)

def car(request):
    user = request.user
    print(user)
    if request.method == 'POST':
        car_name = request.POST['name']
        company = request.POST['company_name']
        img = request.FILES['img']
        per_day_price = request.POST['per_day_price']
        per_hour_price = request.POST['per_hour_price']
        pub = request.POST['pub']
        location = request.POST['location']
        c = Car.objects.create(user=user,name=car_name,company_name=company,img=img,per_day_price=per_day_price,per_hour_price=per_hour_price,is_published=pub,location=location)
        return redirect('/dealerdash/managecar')
    return render(request,'adcar.html')

def managecar(request):
    c = Car.objects.filter(user=request.user)
    return render(request,'managecar.html',{'c2':c})

def manageedit(request,id):
    c = Car.objects.get(id=id)
    if request.method == 'POST':
        car_name = request.POST['name']
        company = request.POST['company_name']
        img = request.POST.get('img')
        pardprice = request.POST['per_day_price']
        parhprice = request.POST['per_hour_price']
        pub = request.POST['pub']
        location = request.POST['location']
        c.car_name = car_name
        c.company = company
        if img:
            c.car_img = img
        c.pardprice=pardprice
        c.parhprice=parhprice
        c.is_published = pub
        c.location = location
        c.save()
        return redirect('/dealerdash/managecar')
    return render(request,'manageedit.html',{'c1':c})

def managedelete(request,id):
    c1 = Car.objects.get(id=id)
    c1.delete()
    return redirect('/dealerdash/managecar')

def Logout(request):
    logout(request)
    return redirect('/')

def managebooking(request):
    user = request.user
    j = Car.objects.filter(user=user)
    al = []
    for i in j:
        a = Booking.objects.filter(car_name = i.id)
        # print(a)
        al.append(a)
    print(al)
    return render(request,'showbookings.html',{'s':al})

def app_approve(request,id):
    a = Booking.objects.get(id=id)
    a.is_status = 'Approve'
    a.save()
    return redirect('/dealerdash/showbooking/')

def app_reject(request,id):
    a = Booking.objects.get(id=id)
    a.is_status = 'Pending'
    a.save()
    return redirect('/dealerdash/showbooking/')

