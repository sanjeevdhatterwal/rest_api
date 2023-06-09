from rest_framework import serializers
from api import models
class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=256)
    roll=serializers.IntegerField()
    marks=serializers.IntegerField()
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Tag
        fields='__all__'
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Article
        fields='__all__'
