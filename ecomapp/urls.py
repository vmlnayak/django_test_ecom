from django.urls import path
from . import views
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('create-categories/', CreateCategory.as_view(), name='create-category'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='single_category'),
    path('categories/', ListCategory.as_view(), name='categories'),

    path('create-products/', CreateProduct.as_view(), name='create-category'),
    path('products/', ListProduct.as_view(), name='products'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='single_category'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
