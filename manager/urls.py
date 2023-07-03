from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name='home'),
    path('customer/<str:pk_test>/',customer, name='customer'),
    path('product/',products,name='products'),
    path('create/<str:pk>/',create_order,name='create'),
    path('update/<str:pk>/', update, name='update'),
    path('delete/<str:pk>/', delete, name='delete'),
    path('login/', loginPage, name='login'),
    path('register/', registerPage, name='register'),
    path('logout/',logoutPage,name='logout'),
    path('user/',userPage,name='user'),
    path('settings/',settingsPage,name='settings')

]