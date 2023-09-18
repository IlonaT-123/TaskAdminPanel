from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('fuel-types/', views.FuelTypeList.as_view(), name='fuel-types-list'),
    path('create-order/', views.OrderCreate.as_view(), name='create-order'),
    path('success-page/', views.success, name='success-page')
]
