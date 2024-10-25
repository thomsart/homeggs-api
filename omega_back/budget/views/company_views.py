from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

from ..permissions import IsSuperuser, IsActive
from ..models import Company
from ..serializers import CompanySerializer



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


    # def post(self, request, format=None):

    #     company = CompanySerializer(data=request.data)

    #     if company.is_valid():
    #         company = company.save()
    #         serializer = CompanySerializer(company)

    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    #     return Response(company.errors, status=status.HTTP_400_BAD_REQUEST)


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


    # def put(self, request, pk, format=None):

    #     client = self.get_object(pk)
    #     serializer = UpdateClientSerializer(client, data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         client = HeavyClientSerializer(client)

    #         return Response(client.data)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # def delete(self, request, pk, format=None):

    #     client = self.get_object(pk)

    #     try:
    #         client.is_still_client = False
    #         # maybe we need to deactivate the contact user(s) ?
    #         client.save()

    #         return Response(status=status.HTTP_204_NO_CONTENT)

    #     except PermissionError:
    #         return Response(status=status.HTTP_403_FORBIDDEN)
