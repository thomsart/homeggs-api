"""
Module of budget/views/fee_or_expense.py
"""

from . import (
    APIView, permissions, Response, status, Http404, 
    IsSuperuser, IsActive , 
    FeeOrExpense, FeeOrExpenseSerializer, CreateFeeOrExpenseSerializer, UpdateFeeOrExpenseSerializer
)


class FeeOrExpenseList(APIView):
    """
    App: budget.\n
    View Type: APIView.\n
    List all fee-expenses, or create a new one.\n
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsSuperuser,
        IsActive,
    ]

    def get(self, request, format=None):

        fee_or_expense = FeeOrExpense.objects.all()

        serializer = FeeOrExpenseSerializer(fee_or_expense, many=True)

        return Response(serializer.data)


    def post(self, request, format=None):

        fee_or_expense = CreateFeeOrExpenseSerializer(data=request.data)

        if fee_or_expense.is_valid():
            fee_or_expense = fee_or_expense.save()
            serializer = FeeOrExpenseSerializer(fee_or_expense)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(fee_or_expense.errors, status=status.HTTP_400_BAD_REQUEST)


class FeeOrExpenseDetail(APIView):
    """
    App: budget.\n
    View Type: APIView.\n
    Retrieve, update or delete fee-expenses.\n
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsSuperuser,
        IsActive,
    ]

    def get_object(self, pk):

        try:
            return FeeOrExpense.objects.get(id=pk)

        except FeeOrExpense.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):

        fee_or_expense = self.get_object(pk)
        serializer = FeeOrExpenseSerializer(fee_or_expense)

        return Response(serializer.data)


    def put(self, request, pk, format=None):

        fee_or_expense = self.get_object(pk)
        serializer = UpdateFeeOrExpenseSerializer(fee_or_expense, data=request.data)

        if serializer.is_valid():
            serializer.save()
            fee_or_expense = FeeOrExpenseSerializer(fee_or_expense)

            return Response(fee_or_expense.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk, format=None):

        fee_or_expense = self.get_object(pk)
        serializer = UpdateFeeOrExpenseSerializer(
                        fee_or_expense, data=request.data, partial=True
                    )

        if serializer.is_valid():
            serializer.save()
            fee_or_expense = FeeOrExpenseSerializer(fee_or_expense)

            return Response(fee_or_expense.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):

        fee_or_expense = self.get_object(pk)

        try:
            fee_or_expense.delete()

            return Response(status=status.STATUS_202_ACCEPTED)

        except PermissionError:

            return Response(status=status.HTTP_403_FORBIDDEN)