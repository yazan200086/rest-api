from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from first_api import serializers
from rest_framework import viewsets


class hello(APIView):
    '''test'''
    serializer_class=serializers.hello_serializier
    def get(self,request,format=None):
        apiView=['uses HTTP methods as function(get,post,patch,put delete)','give the most control over the application','is mapped manullay to URLs']
        return Response({'apiView':apiView})
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,pk=None):
        '''handle update an object'''
        return Response({'message':'put'})

    def patch(self,request,pk=None):
        '''handle partial update an object'''
        return Response({'message':'Patch'})

    def delete(self,request,pk=None):
        '''handle delete an object'''
        return Response({'message':'Delete'})



class helloViewsets(viewsets.ViewSet):
    '''test VIewSet'''
    serializer_class=serializers.hello_serializier

    def list(self,request):
        ViewSet=[
        'uses action (list,create,update,partil_update,destroy)',
        'Automaticlly maps to URLSs using Routers',
        'more functionality with less code',
        'good for simple DB interaction'

        ]

        return Response({'ViewSet':ViewSet})

    def create(self, request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self,request,pk=None):
        return Response({"method":"GET"})


    def update(self,request,pk=None):
        return Response({"method":"PUT"})


    def patial_update(self,request,pk=None):
        return Response({"method":"PATCH"})

    def destroy(self,request,pk=None):
        return Response({"method":"DELETE"})
