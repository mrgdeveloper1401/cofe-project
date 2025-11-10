from django.urls import path

from .views import ShoppingView

app_name = "order_app"

urlpatterns = [
    path("shopping/", ShoppingView.as_view(), name="shopping")
]
