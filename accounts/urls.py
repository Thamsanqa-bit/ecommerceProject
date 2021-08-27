from django.urls import path

from . import views

urlpatterns = [
    path('customer/', views.customer, name='customer'),
    path('become-customer/', views.become_customer, name='become_customer'),
    # path('customer-admin/', views.customer_admin, name='customer_admin'),
    path('', views.home, name='home'),
]