from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from first_api import serializers


class hello(APIView):
    '''test'''
    serializer_class=serializers.hello_serializier
    def get(self,request,format=None):
        apiView=['uses HTTP methods as function(get,post,patch,put delete)','give the most control over the application','is mappesd manullt to URLs']
        return Response({'message':'hello','apiView':apiView})
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
