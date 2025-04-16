"""
Module of budget/views/company.py
"""

from . import (
    APIView, permissions, Response, status, Http404, 
    IsSuperuser, IsActive , 
    Company, CreateCompanySerializer, UpdateCompanySerializer, CompanySerializer
)


class CompanyList(APIView):
    """
    App: budget.\n
    View Type: APIView.\n
    List all companies, or create a new one.\n
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsSuperuser,
        IsActive,
    ]

    def get(self, request, format=None):

        company = Company.objects.all()

        serializer = CompanySerializer(company, many=True)

        return Response(serializer.data)


    def post(self, request, format=None):

        company = CreateCompanySerializer(data=request.data)

        if company.is_valid():
            company = company.save()
            serializer = CompanySerializer(company)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(company.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyDetail(APIView):
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
            return Company.objects.get(id=pk)

        except Company.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):

        company = self.get_object(pk)
        serializer = CompanySerializer(company)

        return Response(serializer.data)


    def put(self, request, pk, format=None):

        company = self.get_object(pk)
        serializer = UpdateCompanySerializer(company, data=request.data)

        if serializer.is_valid():
            serializer.save()
            company = CompanySerializer(company)

            return Response(company.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk, format=None):

        company = self.get_object(pk)
        serializer = UpdateCompanySerializer(company, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            company = CompanySerializer(company)

            return Response(company.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):

        company = self.get_object(pk)

        try:
            company.delete()

            return Response(status=status.STATUS_202_ACCEPTED)

        except PermissionError:

            return Response(status=status.HTTP_403_FORBIDDEN)
