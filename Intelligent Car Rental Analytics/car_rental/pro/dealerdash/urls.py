from django.urls import path
from .import views
urlpatterns = [
    path('adindex/',views.dealerdash),
    path('addcar/',views.car),
    path('managecar/',views.managecar),
    path('manageedit/<int:id>/',views.manageedit),
    path('managedelete/<int:id>/',views.managedelete),
    path('showbooking/',views.managebooking),
    path('application_approve/<int:id>/', views.app_approve),
    path('application_pending/<int:id>/', views.app_reject),
    path('adlogout/',views.Logout)
    ]