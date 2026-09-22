from django.urls import path
from .import views
urlpatterns = [
    path('cusdashindex/', views.cusdash),
    # path('cusaddcar/', views.cuscar),
    # path('cusmanagecar/', views.cusmanagecar),
    # path('cusmanageedit/<int:id>/', views.cusmanageedit),
    # path('cusmanagedelete/<int:id>/', views.cusmanagedelete),
    path('cusshowbooking/', views.cusmanagebooking),
    path('application_approve/<int:id>/', views.app_approve),
    path('application_pending/<int:id>/', views.app_reject),
    path('cuslogout/', views.Logout)
    ]