from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Status, Type, Category, SubCategory
from django.contrib import messages
from django.db.models import ProtectedError

# Create your views here.

class StatusListView(ListView):
    model = Status
    template_name = 'directories/status_list.html'
    context_object_name = 'statuses'

class StatusCreateView(CreateView):
    model = Status
    fields = '__all__'
    template_name = 'directories/status_form.html'
    success_url = reverse_lazy('status_list')
    def form_valid(self, form):
        messages.success(self.request, 'Статус успешно создан!')
        return super().form_valid(form)

class StatusUpdateView(UpdateView):
    model = Status
    fields = '__all__'
    template_name = 'directories/status_form.html'
    success_url = reverse_lazy('status_list')
    def form_valid(self, form):
        messages.success(self.request, 'Статус успешно обновлён!')
        return super().form_valid(form)

class StatusDeleteView(DeleteView):
    model = Status
    template_name = 'directories/status_confirm_delete.html'
    success_url = reverse_lazy('status_list')
    def form_valid(self, form):
        try:
            response = super().form_valid(form)
            messages.success(self.request, 'Статус успешно удалён!')
            return response
        except ProtectedError:
            messages.error(self.request, 'Нельзя удалить статус, так как он используется в записях ДДС.')
            return redirect('status_list')

class TypeListView(ListView):
    model = Type
    template_name = 'directories/type_list.html'
    context_object_name = 'types'

class TypeCreateView(CreateView):
    model = Type
    fields = '__all__'
    template_name = 'directories/type_form.html'
    success_url = reverse_lazy('type_list')
    def form_valid(self, form):
        messages.success(self.request, 'Тип успешно создан!')
        return super().form_valid(form)

class TypeUpdateView(UpdateView):
    model = Type
    fields = '__all__'
    template_name = 'directories/type_form.html'
    success_url = reverse_lazy('type_list')
    def form_valid(self, form):
        messages.success(self.request, 'Тип успешно обновлён!')
        return super().form_valid(form)

class TypeDeleteView(DeleteView):
    model = Type
    template_name = 'directories/type_confirm_delete.html'
    success_url = reverse_lazy('type_list')
    def form_valid(self, form):
        try:
            response = super().form_valid(form)
            messages.success(self.request, 'Тип успешно удалён!')
            return response
        except ProtectedError:
            messages.error(self.request, 'Нельзя удалить тип, так как он используется в категориях или записях ДДС.')
            return redirect('type_list')

class CategoryListView(ListView):
    model = Category
    template_name = 'directories/category_list.html'
    context_object_name = 'categories'

class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'directories/category_form.html'
    success_url = reverse_lazy('category_list')
    def form_valid(self, form):
        messages.success(self.request, 'Категория успешно создана!')
        return super().form_valid(form)

class CategoryUpdateView(UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'directories/category_form.html'
    success_url = reverse_lazy('category_list')
    def form_valid(self, form):
        messages.success(self.request, 'Категория успешно обновлена!')
        return super().form_valid(form)

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'directories/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')
    def form_valid(self, form):
        try:
            response = super().form_valid(form)
            messages.success(self.request, 'Категория успешно удалена!')
            return response
        except ProtectedError:
            messages.error(self.request, 'Нельзя удалить категорию, так как она используется в подкатегориях или записях ДДС.')
            return redirect('category_list')

class SubCategoryListView(ListView):
    model = SubCategory
    template_name = 'directories/subcategory_list.html'
    context_object_name = 'subcategories'

class SubCategoryCreateView(CreateView):
    model = SubCategory
    fields = '__all__'
    template_name = 'directories/subcategory_form.html'
    success_url = reverse_lazy('subcategory_list')
    def form_valid(self, form):
        messages.success(self.request, 'Подкатегория успешно создана!')
        return super().form_valid(form)

class SubCategoryUpdateView(UpdateView):
    model = SubCategory
    fields = '__all__'
    template_name = 'directories/subcategory_form.html'
    success_url = reverse_lazy('subcategory_list')
    def form_valid(self, form):
        messages.success(self.request, 'Подкатегория успешно обновлена!')
        return super().form_valid(form)

class SubCategoryDeleteView(DeleteView):
    model = SubCategory
    template_name = 'directories/subcategory_confirm_delete.html'
    success_url = reverse_lazy('subcategory_list')
    def form_valid(self, form):
        try:
            response = super().form_valid(form)
            messages.success(self.request, 'Подкатегория успешно удалена!')
            return response
        except ProtectedError:
            messages.error(self.request, 'Нельзя удалить подкатегорию, так как она используется в записях ДДС.')
            return redirect('subcategory_list')
