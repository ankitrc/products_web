"""products_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
from blogs import urls
from admin_content import urls as adminurl

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.home),
    # url(r'^blog/',include(blogs.urls)),
    # path('admin-contents/', include(admin_content.urls)),
    path('blogs/', include(urls)),
    # path('admin-content-add/',views.product_add),
    # path('admin-content/',views.product_add_show),
    path('admin-content/', include(adminurl)),
]
