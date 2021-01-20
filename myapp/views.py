from django.shortcuts import render
from django.http import HttpResponse,Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json

# Create your views here.

@api_view(["POST"])
def Add(data1):
    try:
        num1=json.loads(data1.body)
        num2=json.loads(data1.body)
        res=str(num1+num2)

        return JsonResponse("Sum is:"+res,safe=False)

    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)



