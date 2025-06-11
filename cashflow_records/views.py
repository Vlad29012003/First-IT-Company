from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import CashFlowRecord
from .forms import CashFlowRecordForm
from django.http import JsonResponse
from directories.models import Category, SubCategory
from django.contrib import messages

class CashFlowListView(ListView):
    model = CashFlowRecord
    template_name = 'cashflow_records/cashflow_list.html'
    context_object_name = 'records'

class CashFlowCreateView(CreateView):
    model = CashFlowRecord
    form_class = CashFlowRecordForm
    template_name = 'cashflow_records/cashflow_form.html'
    success_url = reverse_lazy('cashflow_list')
    def form_valid(self, form):
        messages.success(self.request, 'Запись успешно создана!')
        return super().form_valid(form)

class CashFlowUpdateView(UpdateView):
    model = CashFlowRecord
    form_class = CashFlowRecordForm
    template_name = 'cashflow_records/cashflow_form.html'
    success_url = reverse_lazy('cashflow_list')
    def form_valid(self, form):
        messages.success(self.request, 'Запись успешно обновлена!')
        return super().form_valid(form)

class CashFlowDeleteView(DeleteView):
    model = CashFlowRecord
    template_name = 'cashflow_records/cashflow_confirm_delete.html'
    success_url = reverse_lazy('cashflow_list')
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Запись успешно удалена!')
        return super().delete(request, *args, **kwargs)

def get_categories(request):
    type_id = request.GET.get('type_id')
    categories = Category.objects.filter(type_id=type_id).values('id', 'name')
    return JsonResponse(list(categories), safe=False)

def get_subcategories(request):
    category_id = request.GET.get('category_id')
    subcategories = SubCategory.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse(list(subcategories), safe=False)
