from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render,redirect
from app1.models import Car
# Create your views here.
def index(request):
    s1 = Car.objects.filter(is_published=True)
    return render(request, template_name='index.html',context={'s1':s1})
def about(request):
    return render(request, template_name='about.html')
def services(request):
    return render(request, template_name='services.html')
def pricing(request):
    return render(request, template_name='pricing.html')

def car(request):
    s = Car.objects.all()
    return render(request, template_name='car.html', context={'s1':s})
def car_single(request,id):
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
    return render(request, template_name='car_single.html',context={'s1':s1})
def contact(request):
    return render(request, template_name='contact.html')

@login_required(login_url='/cusdealerlogin/')
def trip_form(request):
    return render(request, template_name='trip_form.html')
def logindemo(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request,"Bad Credentials")
            return redirect('/dealerlogindemo/')
    return render(request, 'dealerlogin.html')

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.firstname = fname
        myuser.lastname = lname

        myuser.save()

        messages.success(request, "Your Account has been successfully created.")

        return redirect('/dealerlogin/')
    return render(request, 'registration.html')
def cuslogindemo(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            return redirect('/customer/')
        else:
            messages.error(request,"Bad Credentials")
            return redirect('/app1/cusdealerlogin/')
    return render(request, 'cusdealerlogin.html')

def cusregistration(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.firstname = fname
        myuser.lastname = lname

        myuser.save()

        messages.success(request, "Your Account has been successfully created.")

        return redirect('/cusdealerlogin/')
    return render(request, 'cusregistration.html')

from django.http import JsonResponse
from .ml_engine import predict_rental_price, recommend_cars, get_fleet_analytics_data, SAMPLE_BRANDS, BODY_TYPES, FUEL_TYPES, TRANSMISSIONS, SEASONS
import json

def admin_dashboard(request):
    return render(request,'admin_dashboard.html')

def Logout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully!')
    return redirect('/')

def ml_analytics(request):
    """
    Data Science and Machine Learning page:
    Provides interactive ML price prediction, AI car recommendation, and data analytics dashboard.
    """
    analytics = get_fleet_analytics_data()
    cars = Car.objects.all()

    # Pre-calculate sample prediction for initial display
    sample_prediction = predict_rental_price(
        brand='Toyota',
        body_type='SUV',
        fuel_type='Diesel',
        transmission='Automatic',
        seats=5,
        duration_days=3,
        season='Regular'
    )

    # Initial recommendation
    initial_recommendations = recommend_cars(budget_per_day=2500)

    # Available brands in fleet
    fleet_brands = list(Car.objects.values_list('company_name', flat=True).distinct())
    all_brands = sorted(list(set(SAMPLE_BRANDS + fleet_brands)))

    context = {
        'analytics': analytics,
        'analytics_json': json.dumps(analytics),
        'sample_prediction': sample_prediction,
        'initial_recommendations': initial_recommendations[:6],
        'brands': all_brands,
        'body_types': BODY_TYPES,
        'fuel_types': FUEL_TYPES,
        'transmissions': TRANSMISSIONS,
        'seasons': SEASONS,
    }
    return render(request, 'ml_analytics.html', context)

def api_predict_price(request):
    """
    AJAX endpoint for real-time ML Rental Price Prediction.
    """
    if request.method in ['POST', 'GET']:
        data = request.POST if request.method == 'POST' else request.GET
        brand = data.get('brand', 'Toyota')
        body_type = data.get('body_type', 'SUV')
        fuel_type = data.get('fuel_type', 'Diesel')
        transmission = data.get('transmission', 'Automatic')
        seats = int(data.get('seats', 5))
        duration_days = int(data.get('duration_days', 3))
        season = data.get('season', 'Regular')

        prediction = predict_rental_price(
            brand=brand,
            body_type=body_type,
            fuel_type=fuel_type,
            transmission=transmission,
            seats=seats,
            duration_days=duration_days,
            season=season
        )
        return JsonResponse({'status': 'success', 'data': prediction})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

def api_recommend_cars(request):
    """
    AJAX endpoint for AI-powered Car Recommendation based on user budget and criteria.
    """
    data = request.POST if request.method == 'POST' else request.GET
    budget = float(data.get('budget', 2500))
    brand = data.get('brand', 'Any')

    recommendations = recommend_cars(budget_per_day=budget, preferred_brand=brand)

    output = []
    for item in recommendations[:6]:
        car = item['car']
        output.append({
            'id': car.id,
            'name': car.name,
            'brand': car.company_name,
            'model': car.model,
            'location': car.location,
            'per_day_price': car.per_day_price,
            'per_hour_price': car.per_hour_price,
            'img_url': car.img.url if car.img else '',
            'match_score': item['match_score'],
            'badge': item['badge'],
            'badge_class': item['badge_class'],
            'price_diff': item['price_diff']
        })

    return JsonResponse({'status': 'success', 'data': output})

