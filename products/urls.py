from django.urls import path
from .views import ProductViewset

urlpatterns = [
    path('', ProductViewset.as_view({'get': 'list'}), name='product-list'),
    path('<int:pk>/',
         ProductViewset.as_view({'get': 'retrieve'}), name='id'),
    path(
        'create-product/', ProductViewset.as_view({'post': 'create_product'}), name='create-product'),
    path(
        'create-category/', ProductViewset.as_view({'post': 'create_category'}), name='create-product'),
    path(
        'create-brand/', ProductViewset.as_view({'post': 'create_brand'}), name='create-brand'),
    path(
        '<int:pk>/place-order/', ProductViewset.as_view({'post': 'order'}), name='place-order'),
    path(
        '<int:pk>/delete-order/', ProductViewset.as_view({'post': 'create_brand'}), name='delete-order'),
]
