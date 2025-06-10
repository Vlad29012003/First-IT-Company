from django_filters.views import FilterView
from .models import CashFlowRecord
from .filters import CashFlowRecordFilter



class CashFlowListView(FilterView):
    model = CashFlowRecord
    template_name = 'cashflow_records/cashflow_list.html'
    context_object_name = 'records'
    filterset_class = CashFlowRecordFilter
    ordering = ['-created_at']
