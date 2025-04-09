"""
Module for saving views.
"""


from . import (
    APIView, permissions, Response, status, Http404, 
    IsSuperuser, IsActive , 
    Saving, SavingSerializer, CreateSavingSerializer, UpdateSavingSerializer
)


class SavingList(APIView):
    """
    App: budget.\n
    View Type: APIView.\n
    List all savings, or create a new one.\n
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsSuperuser,
        IsActive,
    ]

    def get(self, request, format=None):

        saving = Saving.objects.all()

        serializer = SavingSerializer(saving, many=True)

        return Response(serializer.data)


    def post(self, request, format=None):

        saving = CreateSavingSerializer(data=request.data)

        if saving.is_valid():
            saving = saving.save()
            serializer = SavingSerializer(saving)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(saving.errors, status=status.HTTP_400_BAD_REQUEST)


class SavingDetail(APIView):
    """
    App: budget.\n
    View Type: APIView.\n
    Retrieve, update or delete a saving.\n
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsSuperuser,
        IsActive,
    ]

    def get_object(self, pk):

        try:
            return Saving.objects.get(id=pk)

        except Saving.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):

        saving = self.get_object(pk)
        serializer = SavingSerializer(saving)

        return Response(serializer.data)


    def put(self, request, pk, format=None):

        saving = self.get_object(pk)
        serializer = UpdateSavingSerializer(saving, data=request.data)

        if serializer.is_valid():
            serializer.save()
            saving = SavingSerializer(saving)

            return Response(saving.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):

        saving = self.get_object(pk)

        try:
            saving.delete()

            return Response(status=status.STATUS_202_ACCEPTED)

        except PermissionError:

            return Response(status=status.HTTP_403_FORBIDDEN)
