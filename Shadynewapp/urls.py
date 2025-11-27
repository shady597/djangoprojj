from django.urls import path
from . import views 

urlpatterns = [
    path('', views.runtemplate, name='runtemplate'),
    path('hi/', views.say_hi, name='say_hi'),
]