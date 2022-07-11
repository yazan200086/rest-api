from rest_framework import serializers

class hello_serializier(serializers.Serializer):
    '''serializer name field for APIView'''
    name= serializers.CharField(max_length=10)
