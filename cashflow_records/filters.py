import django_filters
from .models import CashFlowRecord

class CashFlowRecordFilter(django_filters.FilterSet):
    date_from = django_filters.DateFilter(field_name='created_at', lookup_expr='gte', label='Дата с')
    date_to = django_filters.DateFilter(field_name='created_at', lookup_expr='lte', label='Дата по')

    class Meta:
        model = CashFlowRecord
        fields = ['status', 'type', 'category', 'subcategory'] 