from django.urls import path
from .views import (
    StatusListView, StatusCreateView, StatusUpdateView, StatusDeleteView,
    TypeListView, TypeCreateView, TypeUpdateView, TypeDeleteView,
    CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    SubCategoryListView, SubCategoryCreateView, SubCategoryUpdateView, SubCategoryDeleteView,
)

urlpatterns = [
    path('status/', StatusListView.as_view(), name='status_list'),
    path('status/add/', StatusCreateView.as_view(), name='status_add'),
    path('status/edit/<int:pk>/', StatusUpdateView.as_view(), name='status_edit'),
    path('status/delete/<int:pk>/', StatusDeleteView.as_view(), name='status_delete'),

    path('type/', TypeListView.as_view(), name='type_list'),
    path('type/add/', TypeCreateView.as_view(), name='type_add'),
    path('type/edit/<int:pk>/', TypeUpdateView.as_view(), name='type_edit'),
    path('type/delete/<int:pk>/', TypeDeleteView.as_view(), name='type_delete'),

    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_add'),
    path('category/edit/<int:pk>/', CategoryUpdateView.as_view(), name='category_edit'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),

    path('subcategory/', SubCategoryListView.as_view(), name='subcategory_list'),
    path('subcategory/add/', SubCategoryCreateView.as_view(), name='subcategory_add'),
    path('subcategory/edit/<int:pk>/', SubCategoryUpdateView.as_view(), name='subcategory_edit'),
    path('subcategory/delete/<int:pk>/', SubCategoryDeleteView.as_view(), name='subcategory_delete'),
] 