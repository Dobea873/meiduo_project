from django.shortcuts import render
from meiduo_mall.utils.views import LoginRequiredJSONMixin
from django.views import View

# Create your views here.


class OrderSettlementView(LoginRequiredJSONMixin, View):
    """结算订单"""

    def get(self, request):
        """查询并展示要结算的订单数据"""
        return render(request, 'palce_order.html')