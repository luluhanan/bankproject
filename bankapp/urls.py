from django.urls import path,include

from bankapp import views

urlpatterns = [

    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
    path('success', views.success, name='success'),
    path('myform', views.myform, name='myform'),
    path('account', views.accountcreated, name='account'),

    ]
