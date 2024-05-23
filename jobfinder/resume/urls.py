from django.urls import path
from . import views

urlpatterns = [
    path('resume/', views.update_resume, name='resume'),
    path('resume-details/<int:pk>/', views.resume_details, name='resume-details'),
]
