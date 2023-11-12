from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.exceptions import ObjectDoesNotExist
from . import serializers
from . import models
# Create your views here.


class ProductViewset(viewsets.ViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def list(self, request):
        products = models.Product.objects.all()
        serializer = serializers.ProductSerializer(products, many=True)
        return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            product = self.get_product(pk=pk)
            serializer = serializers.ProductSerializer(product)
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'status': 'error', 'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['post'])
    def create_product(self, request):
        serializer = serializers.ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def create_category(self, request):
        serializer = serializers.CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def create_brand(self, request):
        serializer = serializers.BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'], url_path='place-order', serializer_class=serializers.OrderSerializer)
    def order(self, request, pk=None):
        serializer = serializers.OrderSerializer(data=request.data)
        if serializer.is_valid():
            try:
                product = self.get_product(pk)
                quantity_ordered = serializer.validated_data['quantity']

                # Calculate total amount based on quantity and product price
                total_amount = quantity_ordered * product.price

                if product.stock_level > quantity_ordered:
                    # Deduct quantity from stock level
                    product.stock_level -= quantity_ordered
                    product.save()

                    # Create and save the order object
                    order = models.Order(quantity=quantity_ordered,
                                         total_amount=total_amount)
                    order.save()

                    # Associate the product with the order
                    order.product.add(product)

                    return Response({'status': 'success', 'message': 'Order successfully sent'}, status=status.HTTP_201_CREATED)
                else:
                    return Response({'status': 'error', 'message': f'only {product.stock_level} remains'}, status=status.HTTP_409_CONFLICT)
            except ObjectDoesNotExist:
                return Response({'status': 'error', 'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get_product(self, pk):
        return models.Product.objects.get(pk=pk)
