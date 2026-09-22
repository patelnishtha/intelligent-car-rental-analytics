from django.contrib.auth import logout
from django.shortcuts import render, redirect

from app1.models import Car
from customer.models import Booking


# Create your views here.
def cusdash(request):
    a2 = Booking.objects.filter(user=request.user.id).count()
    a1 = Booking.objects.filter(user=request.user.id,is_status='pending').count()
    a = Booking.objects.filter(user=request.user.id, is_status='Approve').count()
    context={
        'b':a2,
        'b1':a1,
        'b2':a
    }
    return render(request,'cusdashindex.html',context)

# def cuscar(request):
#     user = request.user
#     print(user)
#     if request.method == 'POST':
#         car_name = request.POST['name']
#         company = request.POST['company']
#         img = request.FILES['img']
#         pardprice = request.POST['per_day_price']
#         parhprice = request.POST['per_hour_price']
#         pub = request.POST['pub']
#         location = request.POST['location']
#         c = Car.objects.create(user=user,name=car_name,company_name=company,img=img,per_day_price=pardprice,per_hour_price=parhprice,is_published=pub,location=location)
#         return redirect('/cusdash/cusmanagecar')
#     return render(request,'cuscar.html')

def Logout(request):
    logout(request)
    return redirect('/')

def cusmanagebooking(request):
    # user = request.user
    # j = Car.objects.filter(user=user)
    # al = []
    # for i in j:
    #     a = Booking.objects.filter(name = i.id)
    #     # print(a)
    #     al.append(a)
    # print(al)
    b = Booking.objects.filter(user=request.user.id)
    return render(request,'cusshowbookings.html',{'b': b})
def app_approve(request,id):
    a = Booking.objects.get(id=id)
    a.is_status = 'Approve'
    a.save()
    return redirect('/cusdash/showbooking/')

def app_reject(request,id):
    a = Booking.objects.get(id=id)
    a.is_status = 'Pending'
    a.save()
    return redirect('/cusdash/showbooking/')


