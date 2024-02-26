from django.urls import path
from customers import views

urlpatterns = [
    path('', views.CustomerCreateAPIView.as_view(), name="create_customer"),
]
