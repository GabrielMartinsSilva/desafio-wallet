from django.urls import path

from . import views

urlpatterns = [path("cashback", views.cashback, name="cashback")]
