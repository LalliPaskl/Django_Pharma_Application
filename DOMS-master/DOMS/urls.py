"""DOMS URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from Items import views
from django.contrib.auth import views as auth
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='home'),
    url(r'^Items$', views.index, name='home'),
    url(r'^item/(?P<order_id>\d+)/$', views.show, name='show'),
    url(r'^item/new/$', views.new, name='new'),
    url(r'^item/edit/(?P<order_id>\d+)/$', views.edit, name='edit'),
    url(r'^item/delete/(?P<order_id>\d+)/$', views.destroy, name='delete'),
    url(r'^users/login/$', auth.login, {'template_name': 'login.html'}, name='login'),
    url(r'^users/logout/$', auth.logout, {'next_page': '/'}, name='logout'),
    url(r'^users/add_customer/$', views.customer, name='add_customer'),
    url(r'^Customers$', views.customer_index, name='Customers'),
    url(r'^users/change_password/$', login_required(auth.password_change), {'post_change_redirect' : '/','template_name': 'change_password.html'}, name='change_password'),
]
