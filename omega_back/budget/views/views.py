# from rest_framework.views import APIView
# from rest_framework import permissions
# from rest_framework.response import Response
# from django.http import Http404
# from rest_framework import status

# from home.permissions import IsActive, IsNotClient
# from ..models import Client
# from ..permissions import IsCrudOnClientAllowed
# from ..serializers import LightClientSerializer, HeavyClientSerializer, CreateClientSerializer, UpdateClientSerializer



# class ClientList(APIView):
#     """  
#     List all clients, or create a new one.
#     """

#     permission_classes = [
#         permissions.IsAuthenticated,
#         IsActive,
#         IsNotClient,
#         IsCrudOnClientAllowed
#     ]

#     def get(self, request, format=None):

#         clients = Client.objects.filter(is_still_client=True)

#         if int(request.user.hightest_level) > 3:
#             serializer = HeavyClientSerializer(clients, many=True)
#         else:
#             serializer = LightClientSerializer(clients, many=True)

#         return Response(serializer.data)


#     def post(self, request, format=None):

#         client = CreateClientSerializer(data=request.data)

#         if client.is_valid():
#             client = client.save()
#             serializer = HeavyClientSerializer(client)

#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(client.errors, status=status.HTTP_400_BAD_REQUEST)



# class ClientDetail(APIView):
#     """
#     Retrieve, update or delete a client.
#     """

#     permission_classes = [
#         permissions.IsAuthenticated,
#         IsActive,
#         IsNotClient,
#         IsCrudOnClientAllowed
#     ]

#     def get_object(self, pk):

#         try:
#             client = Client.objects.get(id=pk)
#             if client.is_still_client:
#                 return Client.objects.get(id=pk)
#             else:
#                 raise Http404

#         except Client.DoesNotExist:
#             raise Http404


#     def get(self, request, pk, format=None):

#         client = self.get_object(pk)

#         if int(request.user.hightest_level) > 3:
#             serializer = HeavyClientSerializer(client)
#         else:
#             serializer = LightClientSerializer(client)

#         return Response(serializer.data)


#     def put(self, request, pk, format=None):

#         client = self.get_object(pk)
#         serializer = UpdateClientSerializer(client, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             client = HeavyClientSerializer(client)

#             return Response(client.data)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def delete(self, request, pk, format=None):

#         client = self.get_object(pk)

#         try:
#             client.is_still_client = False
#             # maybe we need to deactivate the contact user(s) ?
#             client.save()

#             return Response(status=status.HTTP_204_NO_CONTENT)

#         except PermissionError:
#             return Response(status=status.HTTP_403_FORBIDDEN)

