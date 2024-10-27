"""
Module for company views.
"""

from . import (
    APIView, permissions, Response, status, 
    Company, CreateCompanySerializer, UpdateCompanySerializer, CompanySerializer
)
from ..permissions import IsSuperuser, IsActive


class CompanyList(APIView):
    """  
    List all companies, or create a new one.
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
    Retrieve, update or delete a client.
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

            return Response(company.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):

        client = self.get_object(pk)

        try:
            client.delete()

            return Response(status=status.STATUS_202_ACCEPTED)

        except PermissionError:

            return Response(status=status.HTTP_403_FORBIDDEN)
