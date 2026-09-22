from django.urls import path
from .import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('services/',views.services),
    path('pricing/', views.pricing),
    path('car/', views.car),
    path('car_single/<int:id>/', views.car_single),
    path('contact/', views.contact),
    path('trip_form/', views.trip_form),
    path('dealerlogin/', views.logindemo),
    # path('cusbase/', views.cusbase),
    path('admin_dashboard/',views.admin_dashboard),
    path('registration/', views.registration),
    path('Logout/', views.Logout),
    path('cusregistration/', views.cusregistration),
    path('cusdealerlogin/', views.cuslogindemo),
    path('ml-analytics/', views.ml_analytics, name='ml_analytics'),
    path('api/predict-price/', views.api_predict_price, name='api_predict_price'),
    path('api/recommend-cars/', views.api_recommend_cars, name='api_recommend_cars'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)