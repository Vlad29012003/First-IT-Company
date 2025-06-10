from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import CashFlowRecord

class CashFlowListView(ListView):
    model = CashFlowRecord
    template_name = 'cashflow_records/cashflow_list.html'
    context_object_name = 'records'

class CashFlowCreateView(CreateView):
    model = CashFlowRecord
    fields = '__all__'
    template_name = 'cashflow_records/cashflow_form.html'
    success_url = reverse_lazy('cashflow_list')

class CashFlowUpdateView(UpdateView):
    model = CashFlowRecord
    fields = '__all__'
    template_name = 'cashflow_records/cashflow_form.html'
    success_url = reverse_lazy('cashflow_list')

class CashFlowDeleteView(DeleteView):
    model = CashFlowRecord
    template_name = 'cashflow_records/cashflow_confirm_delete.html'
    success_url = reverse_lazy('cashflow_list')
