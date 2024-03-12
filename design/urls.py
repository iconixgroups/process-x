from django.urls import path
from . import views

urlpatterns = [
    path('process/design', views.design_process, name='design_process'),
    path('form/create', views.create_form, name='create_form'),
    path('workflow/create', views.create_workflow, name='create_workflow'),
]