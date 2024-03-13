from django.urls import path
from . import views

urlpatterns = [
    path('fetch/<str:moduleId>/', views.fetch_dashboard_data, name='fetch_dashboard_data'),
    path('generate/<str:moduleId>/', views.generate_report, name='generate_report'),
]