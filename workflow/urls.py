from django.urls import path
from . import views

urlpatterns = [
    path('design/process', views.design_process, name='design_process'),
    path('design/form', views.create_form, name='create_form'),
    path('design/workflow', views.create_workflow, name='create_workflow'),
]