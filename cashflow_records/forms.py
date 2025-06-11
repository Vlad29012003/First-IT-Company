from django import forms
from .models import CashFlowRecord
from directories.models import Category, SubCategory

class CashFlowRecordForm(forms.ModelForm):
    class Meta:
        model = CashFlowRecord
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'type' in self.data:
            try:
                type_id = int(self.data.get('type'))
                self.fields['category'].queryset = Category.objects.filter(type_id=type_id)
            except (ValueError, TypeError):
                self.fields['category'].queryset = Category.objects.none()
        elif self.instance.pk:
            self.fields['category'].queryset = Category.objects.filter(type=self.instance.type)
        else:
            self.fields['category'].queryset = Category.objects.none()

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = SubCategory.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                self.fields['subcategory'].queryset = SubCategory.objects.none()
        elif self.instance.pk:
            self.fields['subcategory'].queryset = SubCategory.objects.filter(category=self.instance.category)
        else:
            self.fields['subcategory'].queryset = SubCategory.objects.none()

        required_fields = ['type', 'category', 'subcategory', 'amount']
        for field_name in required_fields:
            if field_name in self.fields:
                self.fields[field_name].required = True
                self.fields[field_name].widget.attrs['required'] = 'required'
        if 'amount' in self.fields:
            self.fields['amount'].widget.attrs['min'] = '0.01'
            self.fields['amount'].widget.attrs['step'] = '0.01'
            self.fields['amount'].widget.attrs['max'] = '1000000000' 