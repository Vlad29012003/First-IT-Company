from django.urls import path
from .views import CashFlowListView, CashFlowCreateView, CashFlowUpdateView, CashFlowDeleteView, get_categories, get_subcategories

urlpatterns = [
    path('', CashFlowListView.as_view(), name='cashflow_list'),
    path('add/', CashFlowCreateView.as_view(), name='cashflow_add'),
    path('edit/<int:pk>/', CashFlowUpdateView.as_view(), name='cashflow_edit'),
    path('delete/<int:pk>/', CashFlowDeleteView.as_view(), name='cashflow_delete'),
    path('ajax/get-categories/', get_categories, name='ajax_get_categories'),
    path('ajax/get-subcategories/', get_subcategories, name='ajax_get_subcategories'),
] 