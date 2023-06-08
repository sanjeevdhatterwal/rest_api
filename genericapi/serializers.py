from rest_framework import serializers
from genericapi import models
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Tag
        fields='__all__'
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Article
        fields='__all__'
