from api import models
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
import json
# Create your views here.
from api import serializers
class Student():
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
@api_view()
def userdata(request):
    s1=Student('abc',1,100)
    s2=Student('def',2,1000)
    s3=Student('ghi',3,300)
    student=serializers.StudentSerializer(s1)
    students=serializers.StudentSerializer([
        s1,s2,s3
    ], many=True)
    return Response(students.data)

@api_view()
def articleApi(request):
    articles=models.Article.objects.all()
    response=serializers.ArticleSerializer(articles,many=True)
    return Response(response.data)
@api_view(['POST'])
def createArticleApi(request):
    body=json.loads(request.body)
    response=serializers.ArticleSerializer(data=body)
    if(response.is_valid()):
        inst=response.save()
        response=serializers.ArticleSerializer(inst)
        return Response(response.data)
    return Response(response.errors)