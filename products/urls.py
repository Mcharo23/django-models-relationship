from django.urls import path
from .views import ProductViewset

urlpatterns = [
    path('', ProductViewset.as_view({'get': 'list'}), name='product-list'),
    path('<int:pk>/',
         ProductViewset.as_view({'get': 'retrieve'}), name='product-retrieve'),
    path(
        'create-product/', ProductViewset.as_view({'post': 'create_product'}), name='product-create'),
    path(
        'create-category/', ProductViewset.as_view({'post': 'create_category'}), name='category-create'),
    path(
        'create-brand/', ProductViewset.as_view({'post': 'create_brand'}), name='brand-create'),
    path(
        '<int:pk>/place-order/', ProductViewset.as_view({'post': 'order'}), name='place-order'),
    path(
        '<int:pk>/delete-product/', ProductViewset.as_view({'post': 'create_brand'}), name='brand-create'),
]
