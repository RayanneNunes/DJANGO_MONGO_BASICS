from django.urls import path 
from . import views 


urlpatterns = [ 

    path('', views.lista, name='lista'), 

    path('nova/', views.nova, name='nova'), 

] 