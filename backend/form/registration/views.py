from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *

class ReactView(APIView):

    serializer_class = ReactSerializer

    def get(self, request):
        data = [ {"name": data.name, "mobile": data.mobile, "city": data.city, "state": data.state} 
        for data in React.objects.all()]
        return Response(data)

    def post(self, request):

        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return  Response(serializer.data) 