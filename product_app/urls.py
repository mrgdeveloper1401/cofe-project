from django.urls import path

from .views import DetailProductView, ListProductView


app_name = "product_app"

urlpatterns = [
    path("p/<int:id>/", DetailProductView.as_view(), name='detail-product-view'),
    path("search-product/", ListProductView.as_view(), name='list-product')
]
