from django.urls import path
from .import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.cusindex),
    path('cusabout/',views.cusabout),
    path('cusservices/',views.cusservices),
    path('cuspricing/', views.cuspricing),
    path('cuscar/', views.cuscar),
    path('cuscar_single/<int:id>/', views.cuscar_single),
    path('cuscontact/', views.cuscontact),
    path('custrip_form/<int:id>/', views.custrip_form),
    # path('cusbase/', views.cusbase),
    path('cus_dashboard/', views.cus_dashboard),
    path('Logout/', views.Logout)
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)