from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.generics import (
    RetrieveAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView
)
from genericapi import models, serializers
# this class retrieves the list view of all the articles.
# if the incoming request is a search request it sends the output by filtering out the result accordingly.

class ArticleListView(ListAPIView):
    # queryset=models.Article.objects.all()
    serializer_class=serializers.ArticleSerializer
    def get_queryset(self):
        query={}
        for key,value in self.request.GET.items():
            query["{}__icontains".format(key)]=value
        return models.Article.objects.all(**query)


#     used to create the article from the incoming request
# the function get_queryset refreshes  queryset everytime the request is called
class ArticleListCreateView(ListCreateAPIView):
    serializer_class=serializers.ArticleSerializer
    def get_queryset(self):
        return models.Article.objects.all()
#     used to find the details of any particular article
class ArticleDetailView(RetrieveAPIView):
    queryset=models.Article.objects.all()
    serializer_class=serializers.ArticleSerializer
    def post(self,request,pk):
        return Response(request.body)

# used to update the article with the incoming request.
# make sure to use the patch request for the same
class ArticleDetailUpdateView(RetrieveUpdateAPIView):
    queryset=models.Article.objects.all()
    serializer_class=serializers.ArticleSerializer
