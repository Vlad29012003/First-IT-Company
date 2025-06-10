from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import CashFlowRecord
from .forms import CashFlowRecordForm
from django.http import JsonResponse
from directories.models import Category, SubCategory

class CashFlowListView(ListView):
    model = CashFlowRecord
    template_name = 'cashflow_records/cashflow_list.html'
    context_object_name = 'records'

class CashFlowCreateView(CreateView):
    model = CashFlowRecord
    form_class = CashFlowRecordForm
    template_name = 'cashflow_records/cashflow_form.html'
    success_url = reverse_lazy('cashflow_list')

class CashFlowUpdateView(UpdateView):
    model = CashFlowRecord
    form_class = CashFlowRecordForm
    template_name = 'cashflow_records/cashflow_form.html'
    success_url = reverse_lazy('cashflow_list')

class CashFlowDeleteView(DeleteView):
    model = CashFlowRecord
    template_name = 'cashflow_records/cashflow_confirm_delete.html'
    success_url = reverse_lazy('cashflow_list')

def get_categories(request):
    type_id = request.GET.get('type_id')
    categories = Category.objects.filter(type_id=type_id).values('id', 'name')
    return JsonResponse(list(categories), safe=False)

def get_subcategories(request):
    category_id = request.GET.get('category_id')
    subcategories = SubCategory.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse(list(subcategories), safe=False)
