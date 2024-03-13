from django.urls import path
from . import views

urlpatterns = [
    path('module/<str:moduleId>/publish', views.publish_module, name='publish_module'),
]