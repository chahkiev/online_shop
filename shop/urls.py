"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='вход'),
    path('logout/', views.logout, name='выход'),
    path('register/', views.register, name='регистрация'),
    url(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),
    url(r'^basket_adding/$', views.basket_adding, name='basket_adding'),
    url(r'^confirm_order/(?P<order_id>\w+)/$', views.confirm_order, name='confirm_order'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^my_orders/$', views.my_orders, name='my_orders'),
]
