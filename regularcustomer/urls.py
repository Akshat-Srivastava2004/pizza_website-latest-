from django.contrib import admin
from django.urls import path,include

from.import views
 
urlpatterns=[
    path("",views.Blog,name="Blog"),
    path("chat",views.chat,name="chat"),
 
]