from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_company, name='register_company'),
    path('division/', views.add_division, name='add_division'),
    path('department/', views.add_department, name='add_department'),
    path('project/', views.add_project, name='add_project'),
    path('user/', views.add_user_to_company, name='add_user_to_company'),
]