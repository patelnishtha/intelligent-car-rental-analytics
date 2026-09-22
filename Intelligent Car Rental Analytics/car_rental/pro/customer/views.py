from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render,redirect
from app1.models import Car
from customer.models import Booking


# Create your views here.
def cusindex(request):
    s1 = Car.objects.filter(is_published=True)
    return render(request, template_name='cusindex.html',context={'s1':s1})
def cusabout(request):
    return render(request, template_name='cusabout.html')
def cusservices(request):
    return render(request, template_name='cusservices.html')
def cuspricing(request):
    return render(request, template_name='cuspricing.html')

def cuscar(request):
    s = Car.objects.all()
    user = request.user if request.user.is_authenticated else None
    booked = set(Booking.objects.filter(user=user).values_list('car_name', flat=True)) if user else set()
    return render(request, template_name='cuscar.html', context={'s1':s,'booked':booked})
def cuscar_single(request,id):
    s1 = Car.objects.get(id=id)
    # if request.method == 'POST':
    #     name = request.POST['name']
    #     location = request.POST['location']
    #     model = request.POST['model']
    #     per_day_price = request.POST['per_day_price']
    #     per_hour_price = request.POST['per_hour_price']
    #     company_name = request.POST['company_name']
    #     img = request.FILES['img']
    #     s1.name = name
    #     s1.location = location
    #     s1.model = model
    #     s1.per_day_price = per_day_price
    #     s1.per_hour_price = per_hour_price
    #     s1.company_name = company_name
    #     s1.save()
    #     if img:
    #         s1.img = img
        # return redirect('/car_single/')
    return render(request, template_name='cuscar_single.html',context={'s1':s1})
def cuscontact(request):
    return render(request, template_name='cuscontact.html')
def custrip_form(request,id):
    c = Car.objects.get(id=id)
    user = request.user
    if request.method == 'POST':
        plocation = request.POST['plocation']
        dlocation = request.POST['dlocation']
        pdate = request.POST['pdate']
        ddate = request.POST['ddate']
        time = request.POST['time']
        b = Booking.objects.create(user=user,car_name=c,plocation=plocation,dlocation=dlocation,pdate=pdate,ddate=ddate,time=time)
        return redirect('/cusdash/cusshowbooking/')
    return render(request, template_name='custrip_form.html')
def cus_dashboard(request):
    return render(request,template_name='cus_dashboard.html')
def Logout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully!')
    return redirect('/')

# Create your views here.
