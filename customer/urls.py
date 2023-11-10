from django.contrib import admin
from django.urls import path

from.import views
 

urlpatterns=[
    path("",views.index,name="index"),
    path("signup",views.signup, name="signup"),
    path("login",views.login,name="login"),
    path("Home",views.Home,name="Home"),
    path("payment",views.payment,name="payment"),
    path("gallery",views.gallery,name="gallery"),
    path("Order",views.Order,name="Order"),
    path("ordersummary",views.ordersummary,name="ordersummary"),
    path('logout',views.logout,name='logout'),
    path('contact',views.contact,name='contact'),
]