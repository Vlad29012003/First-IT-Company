from django.urls import path
from .views import CashFlowListView, CashFlowCreateView, CashFlowUpdateView, CashFlowDeleteView

urlpatterns = [
    path('', CashFlowListView.as_view(), name='cashflow_list'),
    path('add/', CashFlowCreateView.as_view(), name='cashflow_add'),
    path('edit/<int:pk>/', CashFlowUpdateView.as_view(), name='cashflow_edit'),
    path('delete/<int:pk>/', CashFlowDeleteView.as_view(), name='cashflow_delete'),
] 