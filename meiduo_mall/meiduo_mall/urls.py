"""meiduo_mall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # haystack
    url(r'^search/', include('haystack.urls')),

    # users
    url(r'^',include(('users.url s', "users"),namespace='users')),
    # contents
    url(r'^',include(('contents.url s', "contents"),namespace='contents')),
    # verifications
    url(r'^',include('verifications.url s')),
    # oauth
    url(r'^',include('oauth.url s')),
    # areas
    url(r'^',include('areas.url s')),
    # goods
    url(r'^',include(('goods.url s', "goods"), namespace='goods')),
    # carts
    url(r'^',include(('carts.url s', "carts"), namespace='carts')),
    # orders
    url(r'^',include(('orders.url s',"orders"), namespace='orders')),
    # payment
    url(r'^',include(('payment.url s',"payment"), namespace='payment')),
]
