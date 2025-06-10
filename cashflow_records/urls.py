from django.urls import path
from .views import CashFlowListView

urlpatterns = [
    path('', CashFlowListView.as_view(), name='cashflow_list'),
] 