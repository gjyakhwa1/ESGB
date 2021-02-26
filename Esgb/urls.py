from django.urls import path
from . import views

urlpatterns=[
    path('home',views.index,name='home'),
    path('contact',views.contact,name="contact"),
    path('addData',views.addData,name="addData"),
    path('displayData',views.displayData,name="displayData")
    ]
