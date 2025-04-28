"""
Module of shop/views/product.py
"""

from . import (
    APIView, permissions, Response, status, Http404,
    IsSuperuser, IsActive , 
    Product, CreateProductSerializer, UpdateProductSerializer, ProductSerializer
)


class ProductList(APIView):
    """
    App: shop.\n
    View Type: APIView.\n
    List all products, or create a new one.\n
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsSuperuser,
        IsActive,
    ]

    def get(self, request, format=None):

        product = Product.objects.all()

        serializer = ProductSerializer(product, many=True)

        return Response(serializer.data)


    def post(self, request, format=None):

        product = CreateProductSerializer(data=request.data)

        if product.is_valid():
            product = product.save()
            serializer = ProductSerializer(product)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(product.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    """
    App: shop.\n
    View Type: APIView.\n
    Retrieve, update or delete a product.\n
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsSuperuser,
        IsActive,
    ]

    def get_object(self, pk):

        try:
            return Product.objects.get(id=pk)

        except Product.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):

        product = self.get_object(pk)
        serializer = ProductSerializer(product)

        return Response(serializer.data)


    def put(self, request, pk, format=None):

        product = self.get_object(pk)
        serializer = UpdateProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            product = ProductSerializer(product)

            return Response(product.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk, format=None):

        product = self.get_object(pk)
        serializer = UpdateProductSerializer(product, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            product = ProductSerializer(product)

            return Response(product.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):

        product = self.get_object(pk)

        try:
            product.delete()

            return Response(status=status.HTTP_202_ACCEPTED)

        except PermissionError:

            return Response(status=status.HTTP_403_FORBIDDEN)
