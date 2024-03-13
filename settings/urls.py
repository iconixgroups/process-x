from django.urls import path
from . import views

urlpatterns = [
    path('add_module/', views.add_module, name='add_module'),
    path('update_module/<int:moduleId>/', views.update_module, name='update_module'),
]