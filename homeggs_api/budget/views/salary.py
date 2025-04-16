"""
Module of budget/views/salary.py
"""

from . import (
    APIView, permissions, Response, status, Http404, 
    IsSuperuser, IsActive, 
    Salary, CreateSalarySerializer, UpdateSalarySerializer, SalarySerializer
)


class SalaryList(APIView):
    """  
    List all salaries, or create a new one.
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsSuperuser,
        IsActive,
    ]

    def get(self, request, format=None):

        salary = Salary.objects.all()

        serializer = SalarySerializer(salary, many=True)

        return Response(serializer.data)


    def post(self, request, format=None):

        salary = CreateSalarySerializer(data=request.data)

        if salary.is_valid():
            salary = salary.save()
            serializer = SalarySerializer(salary)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SalaryDetail(APIView):
    """
    Retrieve, update or delete a salary.
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsSuperuser,
        IsActive,
    ]

    def get_object(self, pk):

        try:
            return Salary.objects.get(id=pk)

        except Salary.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):

        salary = self.get_object(pk)

        serializer = SalarySerializer(salary)

        return Response(serializer.data)


    def put(self, request, pk, format=None):

        salary = self.get_object(pk)
        salary = UpdateSalarySerializer(salary, data=request.data)

        if salary.is_valid():
            salary.save()
            serializer = SalarySerializer(salary)

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(salary.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk, format=None):

        salary = self.get_object(pk)
        salary = UpdateSalarySerializer(salary, data=request.data, partial=True)

        if salary.is_valid():
            salary.save()
            serializer = SalarySerializer(salary)

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(salary.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):

        salary = self.get_object(pk)

        try:
            salary.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except PermissionError:

            return Response(status=status.HTTP_403_FORBIDDEN)
