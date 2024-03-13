from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/<str:moduleId>/', views.fetch_dashboard_data, name='fetch_dashboard_data'),
    path('reports/<str:moduleId>/', views.generate_report, name='generate_report'),
]