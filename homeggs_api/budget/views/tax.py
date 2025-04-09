"""
Module for tax views.
"""


from . import (
    APIView, permissions, Response, status, Http404, 
    IsSuperuser, IsActive , 
    Tax, TaxSerializer, CreateTaxSerializer, UpdateTaxSerializer
)


class TaxList(APIView):
    """
    App: budget.\n
    View Type: APIView.\n
    List all taxes, or create a new one.\n
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsSuperuser,
        IsActive,
    ]

    def get(self, request, format=None):

        tax = Tax.objects.all()

        serializer = TaxSerializer(tax, many=True)

        return Response(serializer.data)


    def post(self, request, format=None):

        tax = CreateTaxSerializer(data=request.data)

        if tax.is_valid():
            tax = tax.save()
            serializer = TaxSerializer(tax)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(tax.errors, status=status.HTTP_400_BAD_REQUEST)


class TaxDetail(APIView):
    """
    App: budget.\n
    View Type: APIView.\n
    Retrieve, update or delete a tax.\n
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsSuperuser,
        IsActive,
    ]

    def get_object(self, pk):

        try:
            return Tax.objects.get(id=pk)

        except Tax.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):

        tax = self.get_object(pk)
        serializer = TaxSerializer(tax)

        return Response(serializer.data)


    def put(self, request, pk, format=None):

        tax = self.get_object(pk)
        serializer = UpdateTaxSerializer(tax, data=request.data)

        if serializer.is_valid():
            serializer.save()
            tax = TaxSerializer(tax)

            return Response(tax.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):

        tax = self.get_object(pk)

        try:
            tax.delete()

            return Response(status=status.STATUS_202_ACCEPTED)

        except PermissionError:

            return Response(status=status.HTTP_403_FORBIDDEN)
