from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    #path('/show_system',views.show_system,name='show_system'),
]