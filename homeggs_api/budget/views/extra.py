"""
Module of budget/views/extra.py
"""

from . import (
    APIView, permissions, Response, status, Http404,
    IsSuperuser, IsActive , 
    Extra, ExtraSerializer, CreateExtraSerializer, UpdateExtraSerializer
)


class ExtraList(APIView):
    """
    App: budget.\n
    View Type: APIView.\n
    List all extras, or create a new one.\n
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsSuperuser,
        IsActive,
    ]

    def get(self, request, format=None):

        extra = Extra.objects.all()

        serializer = ExtraSerializer(extra, many=True)

        return Response(serializer.data)


    def post(self, request, format=None):

        extra = CreateExtraSerializer(data=request.data)

        if extra.is_valid():
            extra = extra.save()
            serializer = ExtraSerializer(extra)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(extra.errors, status=status.HTTP_400_BAD_REQUEST)


class ExtraDetail(APIView):
    """
    App: budget.\n
    View Type: APIView.\n
    Retrieve, update or delete an extra.\n
    """

    permission_classes = [
        permissions.IsAuthenticated,
        IsSuperuser,
        IsActive,
    ]

    def get_object(self, pk):

        try:
            return Extra.objects.get(id=pk)

        except Extra.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):

        extra = self.get_object(pk)
        serializer = ExtraSerializer(extra)

        return Response(serializer.data)


    def put(self, request, pk, format=None):

        extra = self.get_object(pk)
        serializer = UpdateExtraSerializer(extra, data=request.data)

        if serializer.is_valid():
            serializer.save()
            extra = ExtraSerializer(extra)

            return Response(extra.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk, format=None):

        extra = self.get_object(pk)
        serializer = UpdateExtraSerializer(extra, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            extra = ExtraSerializer(extra)

            return Response(extra.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):

        extra = self.get_object(pk)

        try:
            extra.delete()

            return Response(status=status.STATUS_202_ACCEPTED)

        except PermissionError:

            return Response(status=status.HTTP_403_FORBIDDEN)