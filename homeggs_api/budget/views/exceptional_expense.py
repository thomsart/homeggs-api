"""
Module of budget/views/exceptional_expense.py
"""

from . import (
    APIView, permissions, Response, status, Http404,
    IsSuperuser, IsActive , 
    ExceptionalExpense, ExceptionalExpenseSerializer, CreateExceptionalExpenseSerializer, UpdateExceptionalExpenseSerializer, 
)

class ExceptionalExpenseList(APIView):
    """
    App: budget.\n
    View Type: APIView.\n
    List all exceptional expenses, or create a new one.\n
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsSuperuser,
        IsActive,
    ]

    def get(self, request, format=None):

        exceptional_expense = ExceptionalExpense.objects.all()

        serializer = ExceptionalExpenseSerializer(exceptional_expense, many=True)

        return Response(serializer.data)


    def post(self, request, format=None):

        exceptional_expense = CreateExceptionalExpenseSerializer(data=request.data)

        if exceptional_expense.is_valid():
            exceptional_expense = exceptional_expense.save()
            serializer = ExceptionalExpenseSerializer(exceptional_expense)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(exceptional_expense.errors, status=status.HTTP_400_BAD_REQUEST)


class ExceptionalExpenseDetail(APIView):
    """
    App: budget.\n
    View Type: APIView.\n
    Retrieve, update or delete a company.\n
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsSuperuser,
        IsActive,
    ]

    def get_object(self, pk):

        try:
            return ExceptionalExpense.objects.get(id=pk)

        except ExceptionalExpense.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):

        exceptional_expense = self.get_object(pk)
        serializer = ExceptionalExpenseSerializer(exceptional_expense)

        return Response(serializer.data)


    def put(self, request, pk, format=None):

        exceptional_expense = self.get_object(pk)
        serializer = UpdateExceptionalExpenseSerializer(exceptional_expense, data=request.data)

        if serializer.is_valid():
            serializer.save()
            exceptional_expense = ExceptionalExpenseSerializer(exceptional_expense)

            return Response(exceptional_expense.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk, format=None):

        exceptional_expense = self.get_object(pk)
        serializer = UpdateExceptionalExpenseSerializer(
                        exceptional_expense, data=request.data, partial=True
                    )

        if serializer.is_valid():
            serializer.save()
            exceptional_expense = ExceptionalExpenseSerializer(exceptional_expense)

            return Response(exceptional_expense.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):

        exceptional_expense = self.get_object(pk)

        try:
            exceptional_expense.delete()

            return Response(status=status.STATUS_202_ACCEPTED)

        except PermissionError:

            return Response(status=status.HTTP_403_FORBIDDEN)