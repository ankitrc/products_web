from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.adminHome),

    path('add/show/',views.addcontentdb),
    path('add/',views.addcontent),
]
