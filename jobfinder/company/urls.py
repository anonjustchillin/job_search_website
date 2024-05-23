from django.urls import path
from . import views

urlpatterns = [
    path('company/', views.update_company, name='company'),
    path('company-details/<int:pk>/', views.company_details, name='company-details'),
]
