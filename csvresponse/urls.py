from django.urls import path, include
from . import views

urlpatterns = [
    path('csv/', views.CsvResponseAPIView.as_view()),
    path('top/', views.TopCustomerAPIView.as_view())
]
