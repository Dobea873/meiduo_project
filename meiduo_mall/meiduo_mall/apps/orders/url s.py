from django.conf.urls import url

from . import views


urlpatterns = [
    # 结算订单
    url(r'^order/settlement/$', views.OrderSettlementView.as_view(), name='settlement'),
]